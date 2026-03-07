#!/usr/bin/env python3
"""Fetch a package from Typst Universe for LLM processing.
Usage: python3 fetch_package.py <package_name>"""

import sys, os, urllib.request, json, re, shutil

def fetch_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": "typst-brain-fetcher/1.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def install_package(name, version):
    """Force Typst to download the package to the local cache."""
    print(f"Installing {name}:{version} to local cache...")
    import subprocess, tempfile
    try:
        with tempfile.NamedTemporaryFile(suffix=".typ", mode="w", delete=False) as f:
            f.write(f'#import "@preview/{name}:{version}": *\nHello')
            tmp_path = f.name
        
        pdf_path = tmp_path.replace('.typ', '.pdf')
        result = subprocess.run(["typst", "compile", tmp_path, pdf_path], capture_output=True, text=True, timeout=15)
        
        if os.path.exists(tmp_path): os.remove(tmp_path)
        if os.path.exists(pdf_path): os.remove(pdf_path)
        
        if result.returncode == 0:
            print("✓ Package cached locally.")
        else:
            print("⚠ Package cache install failed.")
    except Exception as e:
        print(f"⚠ Could not auto-install package: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_package.py <package_name>", file=sys.stderr)
        sys.exit(1)
        
    name = sys.argv[1].lower()
    url = f"https://typst.app/universe/package/{name}"
    
    print(f"Fetching metadata from {url}...")
    html_text = fetch_html(url)
    if not html_text:
        sys.exit(1)

    # Basic Info Extraction
    info = {
        "name": name, 
        "version": "", 
        "repo": "",
        "url": url
    }
    
    m_ver = re.search(r'<h1[^>]*>\s*' + re.escape(name) + r'\s*</h1>\s*<[^>]*>([0-9.]+)', html_text)
    if m_ver: info["version"] = m_ver.group(1).strip()
    
    m_repo = re.search(r'Repository:\s*</dt>\s*<dd[^>]*>\s*<a[^>]*href="([^"]+)"', html_text, re.DOTALL)
    if m_repo: info["repo"] = m_repo.group(1).strip()

    # Create Dump Dir
    out_dir = f"/tmp/raw_universe_dump/{name}"
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    
    # Save Metadata JSON
    with open(os.path.join(out_dir, "metadata.json"), 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2)

    # Extract README markdown chunk (very rough string dump, LLM will parse it later)
    # Reusing the existing html_to_md regex logic is okay, but we don't chunk it.
    import html
    def html_to_md(h):
        h = re.sub(r'<script.*?</script>', '', h, flags=re.DOTALL)
        h = re.sub(r'<style.*?</style>', '', h, flags=re.DOTALL)
        def repl_pre(m):
            code = re.sub(r'<[^>]+>', '', m.group(1))
            return f"\n```typst\n{html.unescape(code).strip()}\n```\n"
        h = re.sub(r'<pre(?:[^>]*)><code>(.*?)</code></pre>', repl_pre, h, flags=re.DOTALL)
        h = re.sub(r'<code[^>]*>(.*?)</code>', lambda m: f"`{html.unescape(m.group(1))}`", h)
        h = re.sub(r'<h1[^>]*>(.*?)</h1\s*>', lambda m: f"\n\n# {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
        h = re.sub(r'<h2[^>]*>(.*?)</h2\s*>', lambda m: f"\n\n## {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
        h = re.sub(r'<h3[^>]*>(.*?)</h3\s*>', lambda m: f"\n\n### {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
        h = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', lambda m: f"[{html.unescape(re.sub(r'<[^>]+>', '', m.group(2)).strip())}]({m.group(1)})", h)
        h = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: f"{html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n\n", h, flags=re.DOTALL)
        h = re.sub(r'<[^>]+>', '', h)
        return re.sub(r'\n{3,}', '\n\n', h).strip()

    m_readme = re.search(r'<div class="readme.*?(?=</main>|<aside)', html_text, re.DOTALL)
    if not m_readme:
        m_readme = re.search(r'<main.*?>(.*?)</main>', html_text, re.DOTALL)
        
    readme_content = html_to_md(m_readme.group(1)) if m_readme else "*No README found*"
    
    with open(os.path.join(out_dir, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme_content)

    if info["version"]:
        install_package(name, info["version"])
        
    print(f"Successfully dumped raw Typst Universe README to {out_dir}. LLM can now process it.")

if __name__ == "__main__":
    main()
