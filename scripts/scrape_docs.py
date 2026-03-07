#!/usr/bin/env python3
"""Scrape detailed Typst documentation and create an index logic map.
Usage: python3 scripts/scrape_docs.py"""

import sys, os, time, re, json, hashlib
from pathlib import Path
import urllib.request, urllib.error
from html.parser import HTMLParser

# --- Configurations ---
BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
DOCS_DIR = os.path.join(BRAIN, "chunks", "docs")
CACHE_DIR = os.path.join(BRAIN, ".cache")
CACHE_TTL = 86400 * 7 # 7 days caching for docs
BASE_URL = "https://typst.app"
START_URL = "https://typst.app/docs/reference/"

# Clean previous docs directory to avoid stale chunks, but keep cache
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)


def fetch_url(url, max_retries=2):
    cache_key = hashlib.md5(url.encode()).hexdigest()
    cache_file = os.path.join(CACHE_DIR, cache_key)
    if os.path.exists(cache_file):
        age = time.time() - os.path.getmtime(cache_file)
        if age < CACHE_TTL:
            with open(cache_file, 'r') as f:
                return f.read()

    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "typst-brain-scraper/2.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8')
                with open(cache_file, 'w') as f:
                    f.write(html)
                return html
        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
            else:
                print(f"Failed to fetch {url}: {e}", file=sys.stderr)
    return None


class TypstDocParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.content_chunks = []
        self.current_tag = ""
        self.in_code = False
        self.code_lang = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "main":
            self.in_main = True
        
        if not self.in_main:
            return
            
        self.current_tag = tag

        if tag in ["h1", "h2", "h3"]:
            level = tag[1]
            self.content_chunks.append(f"\n\n{'#' * int(level)} ")
        elif tag == "pre":
            # Start of code block
            self.in_code = True
            lang = attrs_dict.get("data-language", "")
            self.code_lang = lang
            self.content_chunks.append(f"\n```{lang}\n")
        elif tag == "code" and not self.in_code:
            self.content_chunks.append("`")
        elif tag == "p":
            self.content_chunks.append("\n\n")
        elif tag == "a" and "href" in attrs_dict:
            href = attrs_dict["href"]
            if href.startswith('/'):
                href = BASE_URL + href
            self.content_chunks.append("[")
            # We will append the URL in handle_endtag

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False
        if not self.in_main:
            return

        if tag == "pre":
            self.content_chunks.append("\n```\n")
            self.in_code = False
        elif tag == "code" and not self.in_code:
            self.content_chunks.append("`")
        elif tag == "a":
            # The closing bracket for the link text is handled here, 
            # but we need to know the href. HTMLParser is too simple to keep a stack natively
            # so we just close the bracket. Absolute markdown link might be lost if we don't track it,
            # but for our LLM context, text content is typically enough. 
            self.content_chunks.append("]")
        elif tag in ["p", "li"]:
            self.content_chunks.append("\n")

    def handle_data(self, data):
        if self.in_main:
            # Clean up excessive whitespace in normal text
            if not self.in_code:
                data = re.sub(r'\s+', ' ', data)
            self.content_chunks.append(data)


def clean_markdown(md_text):
    # Condense multiple newlines
    md_text = re.sub(r'\n{3,}', '\n\n', md_text)
    # Remove leading/trailing
    return md_text.strip()


def scrape_index():
    print(f"Scraping Index: {START_URL}")
    html = fetch_url(START_URL)
    if not html: return []
    
    # Use regex to find all reference links to crawl
    # e.g., href="/docs/reference/math/frac/"
    links = re.findall(r'href="(/docs/reference/[^"]+)"', html)
    # Deduplicate and remove the base /docs/reference/ link itself
    unique_links = sorted(list(set(l for l in links if l != '/docs/reference/')))
    return unique_links


def process_page(path):
    url = BASE_URL + path
    html = fetch_url(url)
    if not html: return None

    parser = TypstDocParser()
    parser.feed(html)
    
    raw_md = "".join(parser.content_chunks)
    md = clean_markdown(raw_md)
    
    if not md: return None

    # Derive logical name and category
    # path like: /docs/reference/math/frac/
    parts = [p for p in path.split('/') if p]
    if len(parts) >= 3:
        category = parts[2]
        topic = parts[3] if len(parts) > 3 else "index"
    else:
        category = "general"
        topic = "overview"

    # Extract a short summary for the index
    summary = ""
    # Usually the first paragraph after the H1
    m = re.search(r'#(?:.*?)\n+(.*?)(?:\n\n|\Z)', md, re.DOTALL)
    if m:
        summary = m.group(1).strip()[:150].replace('\n', ' ')

    return {
        "url": url,
        "category": category,
        "topic": topic,
        "content": md,
        "summary": summary
    }


def main():
    links = scrape_index()
    print(f"Found {len(links)} reference pages to scrape. This may take a minute...")

    index_map = []
    
    for i, path in enumerate(links):
        print(f"[{i+1}/{len(links)}] Scraping {path}...")
        data = process_page(path)
        if not data:
            continue
            
        # Create category dir if needed
        cat_dir = os.path.join(DOCS_DIR, data['category'])
        os.makedirs(cat_dir, exist_ok=True)
        
        # Save markdown file
        filepath = os.path.join(cat_dir, f"{data['topic']}.md")
        
        # Add frontmatter to markdown
        md_content = f"---\nurl: {data['url']}\ncategory: {data['category']}\ntopic: {data['topic']}\n---\n\n{data['content']}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        # Add to index mapping
        index_map.append({
            "category": data['category'],
            "topic": data['topic'],
            "summary": data['summary'],
            "file": f"chunks/docs/{data['category']}/{data['topic']}.md"
        })
        
        # Sleep slightly to avoid overwhelming
        time.sleep(0.1)

    # Write the index JSON
    index_path = os.path.join(DOCS_DIR, 'index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_map, f, indent=2)

    print(f"\nDone! Scraped {len(index_map)} documentation chunks.")
    print(f"Index mapped to: {index_path}")

if __name__ == "__main__":
    main()
