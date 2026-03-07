#!/usr/bin/env python3
"""Scrape mdBook documentations recursively into modular Typst Brain chunks.
Usage: python3 scrape_mdbook.py <package_name> <base_url>"""

import sys, os, time, re, html
from urllib.parse import urljoin
from pathlib import Path

# --- Config ---
BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
PKG_DIR = os.path.join(BRAIN, "packages")

def fetch_html(url):
    import urllib.request, urllib.error
    req = urllib.request.Request(url, headers={"User-Agent": "typst-brain-scraper/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def html_to_md(h):
    # Same cleaned markdown converter from scrape_package
    h = re.sub(r'<script.*?</script>', '', h, flags=re.DOTALL)
    h = re.sub(r'<style.*?</style>', '', h, flags=re.DOTALL)
    h = re.sub(r'<svg.*?</svg>', '', h, flags=re.DOTALL)
    h = re.sub(r'class="[^"]+"', '', h)
    
    def repl_pre(m):
        code_html = m.group(1)
        code = re.sub(r'<[^>]+>', '', code_html)
        return f"\n```typst\n{html.unescape(code).strip()}\n```\n"
    h = re.sub(r'<pre(?:[^>]*)><code>(.*?)</code></pre>', repl_pre, h, flags=re.DOTALL)
    h = re.sub(r'<code[^>]*>(.*?)</code>', lambda m: f"`{html.unescape(m.group(1))}`", h)
    
    h = re.sub(r'<h1[^>]*>(.*?)</h1\s*>', lambda m: f"\n\n# {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
    h = re.sub(r'<h2[^>]*>(.*?)</h2\s*>', lambda m: f"\n\n## {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
    h = re.sub(r'<h3[^>]*>(.*?)</h3\s*>', lambda m: f"\n\n### {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
    
    h = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', lambda m: f"[{html.unescape(re.sub(r'<[^>]+>', '', m.group(2)).strip())}]({m.group(1)})", h)
    h = re.sub(r'<li[^>]*>(.*?)</li>', lambda m: f"* {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h, flags=re.DOTALL)
    h = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: f"{html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n\n", h, flags=re.DOTALL)
    h = re.sub(r'<[^>]+>', '', h)
    h = re.sub(r'\n{3,}', '\n\n', h)
    return h.strip()

def process_page(url, idx, title):
    print(f"[{idx:02d}] Fetching: {title} ({url})")
    raw_html = fetch_html(url)
    if not raw_html: return None
    
    m_main = re.search(r'<main.*?>(.*?)</main>', raw_html, re.DOTALL)
    if not m_main:
        m_main = re.search(r'<div id="content".*?>(.*?)</div>\s*<nav', raw_html, re.DOTALL)
        
    if not m_main: return None
    main_html = m_main.group(1)
    
    # Strip intra-page navigation buttons usually found at the bottom of mdBooks
    main_html = re.sub(r'<nav class="nav-wrapper.*?</nav>', '', main_html, flags=re.DOTALL)
    
    return html_to_md(main_html)

def main():
    if len(sys.argv) < 3:
        print("Usage: scrape_mdbook.py <package_name> <base_url>")
        sys.exit(1)
        
    pkg = sys.argv[1].lower()
    base_url = sys.argv[2]
    
    pkg_root = os.path.join(PKG_DIR, pkg)
    chunks_dir = os.path.join(pkg_root, "chunks")
    idx_file = os.path.join(pkg_root, "_index.md")
    
    if not os.path.exists(idx_file):
        print(f"Error: {pkg} is not initialized. Run scrape_package.py {pkg} first.")
        sys.exit(1)
        
    print(f"Crawl target: {base_url}")
    root_html = fetch_html(base_url)
    if not root_html: sys.exit(1)
    
    m_nav = re.search(r'<nav.*?id="sidebar".*?>(.*?)</nav>', root_html, re.DOTALL)
    if not m_nav:
        print("Could not find mdBook sidebar navigation.")
        sys.exit(1)
        
    links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', m_nav.group(1), re.DOTALL)
    
    # Prune existing chunks
    print("Clearing existing chunks...")
    for f in os.listdir(chunks_dir):
        os.remove(os.path.join(chunks_dir, f))
        
    chunk_list = []
    
    # Keep track of seen URLs because mdBooks sometimes duplicate links in nav
    seen = set()
    counter = 1
    
    for href, raw_text in links:
        safe_url = href.split('#')[0] # ignore anchors
        if safe_url in seen or not safe_url: continue
        seen.add(safe_url)
        
        full_url = urljoin(base_url, safe_url)
        clean_title = re.sub(r'<[^>]+>', '', raw_text).strip()
        
        # Clean title for filename e.g. "1. Getting started" -> "getting-started"
        fs_title = re.sub(r'^[\d\.]+\s*', '', clean_title).lower()
        fs_title = re.sub(r'[^a-z0-9]', '-', fs_title).strip('-')
        fs_title = re.sub(r'-+', '-', fs_title)
        
        filename = f"{counter:02d}-{fs_title}.md"
        
        md_content = process_page(full_url, counter, clean_title)
        if md_content:
            with open(os.path.join(chunks_dir, filename), 'w', encoding='utf-8') as f:
                f.write(md_content)
            chunk_list.append((filename, clean_title))
            counter += 1
            
        time.sleep(0.5)
        
    # Inject into _index.md
    print(f"Injecting {len(chunk_list)} new chunks into _index.md...")
    with open(idx_file, 'r', encoding='utf-8') as f:
        idx_content = f.read()
        
    # Replace the chunks list
    head, _ = idx_content.split('## Documentation Chunks', 1)
    
    new_idx = head.strip() + "\n\n## Documentation Chunks\n> **LLM INSTRUCTION:** Do NOT read the entire package. Select ONLY 1 or 2 chunks from the list below that match your current task and load them using `view_file`.\n\n"
    
    for filename, title in chunk_list:
        new_idx += f"- `packages/{pkg}/chunks/{filename}` — {title}\n"
        
    with open(idx_file, 'w', encoding='utf-8') as f:
        f.write(new_idx)
        
    print(f"Successfully migrated {pkg} to massive mdBook docs!")

if __name__ == "__main__":
    main()
