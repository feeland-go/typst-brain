#!/usr/bin/env python3
"""Fetch an mdBook to a local directory for LLM processing.
Usage: python3 fetch_book.py <package_name> <base_url>"""

import sys, os, time, re, html, shutil
from urllib.parse import urljoin
from pathlib import Path

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

def process_page(url, title):
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
        print("Usage: fetch_book.py <package_name> <base_url>")
        sys.exit(1)
        
    pkg = sys.argv[1].lower()
    base_url = sys.argv[2]
    
    out_dir = f"/tmp/raw_mdbook_dump/{pkg}"
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir, exist_ok=True)
        
    print(f"Crawl target: {base_url}")
    root_html = fetch_html(base_url)
    if not root_html: sys.exit(1)
    
    m_nav = re.search(r'<nav.*?id="sidebar".*?>(.*?)</nav>', root_html, re.DOTALL)
    if not m_nav:
        print("Could not find mdBook sidebar navigation.")
        sys.exit(1)
        
    links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', m_nav.group(1), re.DOTALL)
    
    seen = set()
    counter = 1
    
    for href, raw_text in links:
        safe_url = href.split('#')[0] 
        if safe_url in seen or not safe_url: continue
        seen.add(safe_url)
        
        full_url = urljoin(base_url, safe_url)
        clean_title = re.sub(r'<[^>]+>', '', raw_text).strip()
        
        fs_title = re.sub(r'^[\d\.]+\s*', '', clean_title).lower()
        fs_title = re.sub(r'[^a-z0-9]', '-', fs_title).strip('-')
        fs_title = re.sub(r'-+', '-', fs_title)
        filename = f"{counter:02d}-{fs_title}.md"
        
        print(f"[{counter:02d}] Fetching: {clean_title} -> {filename}")
        
        md_content = process_page(full_url, clean_title)
        if md_content:
            with open(os.path.join(out_dir, filename), 'w', encoding='utf-8') as f:
                f.write(f"# {clean_title}\n\n{md_content}")
            counter += 1
            
        time.sleep(0.5)
        
    print(f"Successfully dumped raw mdBook to {out_dir}. LLM can now process it.")

if __name__ == "__main__":
    main()
