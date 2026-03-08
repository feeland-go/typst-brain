#!/usr/bin/env python3
"""Deep Clean Scraper for Typst Documentation.
Extracts only structured, token-minimal data: Signature, Parameters, Examples.
Usage: python3 scripts/scrape_docs.py"""

import sys, os, time, re, json, hashlib, html
from pathlib import Path
import urllib.request

# --- Configurations ---
BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
DOCS_DIR = os.path.join(BRAIN, "docs")
CACHE_DIR = os.path.join(BRAIN, ".cache")
CACHE_TTL = 86400 * 7 # 7 days
BASE_URL = "https://typst.app"
START_URL = "https://typst.app/docs/reference/"

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
            req = urllib.request.Request(url, headers={"User-Agent": "typst-brain-scraper/3.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                text = resp.read().decode('utf-8')
                with open(cache_file, 'w') as f:
                    f.write(text)
                return text
        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
            else:
                print(f"Failed to fetch {url}: {e}", file=sys.stderr)
    return None

def extract_text(html_str):
    if not html_str: return ""
    text = re.sub(r'<[^>]+>', '', html_str)
    text = re.sub(r'\s+', ' ', text).strip()
    return html.unescape(text)

def scrape_index():
    print(f"Scraping Index: {START_URL}")
    raw_html = fetch_url(START_URL)
    if not raw_html: return []
    links = re.findall(r'href="(/docs/reference/[^"]+)"', raw_html)
    return sorted(list(set(l for l in links if l != '/docs/reference/')))

def process_page(path):
    url = BASE_URL + path
    raw_html = fetch_url(url)
    if not raw_html: return None

    # Derive logical names
    parts = [p for p in path.split('/') if p]
    category = parts[2] if len(parts) >= 3 else "general"
    topic = parts[3] if len(parts) > 3 else "index"

    m = re.search(r'<main.*?>(.*?)</main>', raw_html, re.DOTALL)
    if not m: return None
    main_html = m.group(1)

    # Erase visual noise chunks
    main_html = re.sub(r'<script.*?</script>', '', main_html, flags=re.DOTALL)
    main_html = re.sub(r'<div class="tooltip-context".*?</div>\s*</div>', '', main_html, flags=re.DOTALL)
    main_html = re.sub(r'<div role="tooltip".*?</div>', '', main_html, flags=re.DOTALL)
    main_html = re.sub(r'<svg.*?</svg>', '', main_html, flags=re.DOTALL)
    main_html = re.sub(r'<nav.*?</nav>', '', main_html, flags=re.DOTALL)
    main_html = re.sub(r'<div class="page-end-buttons.*', '', main_html, flags=re.DOTALL)

    # 1. Title & Desc
    title = topic
    desc = ""
    m_title = re.search(r'<h1[^>]*>(.*?)</h1\s*>\s*<p>(.*?)</p>', main_html, re.DOTALL)
    if m_title:
        title = extract_text(m_title.group(1)).replace("Element", "").replace("Function", "").strip()
        desc = extract_text(m_title.group(2))

    # 2. Signature
    sig = ""
    m_sig_block = re.search(r'<div class="code code-definition.*?(?=<h2|<h3|<p|<details)', main_html, re.DOTALL)
    if m_sig_block:
        sig = extract_text(m_sig_block.group(0))
        sig = re.sub(r',\s*\)', ')', sig) # fix trailing commas in args
        sig = re.sub(r',\s*', ', ', sig)  # spacing

    # 3. Parameters
    params = []
    # format: <h3 id="parameters-x"><code>name</code> ...</h3> <p>desc</p>
    for p_m in re.finditer(r'<h3[^>]*id="parameters-[^>]*>(.*?)</h3>\s*<p>(.*?)</p>', main_html, re.DOTALL):
        h3_content = p_m.group(1)
        p_desc = extract_text(p_m.group(2))
        
        # Name
        name_m = re.search(r'<code[^>]*>(.*?)</code>', h3_content)
        name = extract_text(name_m.group(1)) if name_m else "unknown"
        
        # Types
        types = []
        for t_m in re.finditer(r'<a[^>]*class="pill[^>]*>(.*?)</a>', h3_content):
            types.append(extract_text(t_m.group(1)))
        
        req = "required" if "Required" in h3_content else "optional"
        type_str = " | ".join(types) if types else "any"
        params.append(f"- `{name}` ({type_str}, {req}): {p_desc}")

    # 4. Examples
    examples = []
    for ex_m in re.finditer(r'<div class="previewed-code">\s*<pre><code>(.*?)</code></pre>', main_html, re.DOTALL):
        raw_code = re.sub(r'<[^>]+>', '', ex_m.group(1))
        clean_code = html.unescape(raw_code).strip()
        if clean_code:
            examples.append(clean_code)

    # 5. Fallback for non-functional pages (like syntax/index)
    # If no sig and no params, just extract headings and paragraphs up to 1000 chars
    fallback_text = ""
    if not sig and not params:
        # Just strip all tags from main_html
        fallback_text = extract_text(main_html)
        if len(fallback_text) > 2000:
            fallback_text = fallback_text[:2000] + "..."

    # Build Output
    out = []
    out.append(f"---\nurl: {url}\ncategory: {category}\ntopic: {topic}\n---\n")
    out.append(f"# {title} ({category})")
    if desc: out.append(desc)
    
    if sig:
        out.append("## Signature")
        out.append(f"`{sig}`")
    
    if params:
        out.append("## Parameters")
        out.extend(params)
        
    if examples:
        out.append("## Examples")
        for ex in examples[:3]: # Limit to top 3 examples to save tokens
            out.append(f"```typst\n{ex}\n```")

    if fallback_text and not sig and not params:
        out.append("## Overview")
        out.append(fallback_text)

    final_md = "\n\n".join(out)

    return {
        "url": url,
        "category": category,
        "topic": topic,
        "content": final_md,
        "summary": desc[:150] if desc else fallback_text[:150]
    }

def main():
    links = scrape_index()
    print(f"Cleaning and re-scraping {len(links)} reference pages...")

    index_map = []
    for i, path in enumerate(links):
        data = process_page(path)
        if not data: continue
        
        cat_dir = os.path.join(DOCS_DIR, data['category'])
        os.makedirs(cat_dir, exist_ok=True)
        filepath = os.path.join(cat_dir, f"{data['topic']}.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(data['content'])
            
        index_map.append({
            "category": data['category'],
            "topic": data['topic'],
            "summary": data['summary'],
            "file": f"docs/{data['category']}/{data['topic']}.md"
        })
        time.sleep(0.01)

    index_path = os.path.join(DOCS_DIR, 'index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_map, f, indent=2)

    print(f"Done! Saved {len(index_map)} surgical docs to {DOCS_DIR}")

if __name__ == "__main__":
    main()
