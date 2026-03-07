#!/usr/bin/env python3
"""Scrape Typst Universe package docs → compressed .md (<600 tok).
Usage: scrape_package.py <package-name>"""

import sys, os, time, re, json, hashlib
from pathlib import Path

BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
PKG_DIR = os.path.join(BRAIN, "packages")
CACHE_DIR = os.path.join(BRAIN, ".cache")
CACHE_TTL = 86400  # 24 hours

# Permissive licenses
PERMISSIVE_BASES = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause",
              "ISC", "Unlicense", "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0",
              "MPL-2.0", "0BSD", "LGPL-2.1", "LGPL-3.0", "LGPL-3.0-or-later", "GPL-2.0", "GPL-3.0"}

def is_license_permissive(lic_str):
    if not lic_str: return False
    # Handle dual licenses e.g., "MIT OR Apache-2.0"
    parts = re.split(r'\s+OR\s+|\s+AND\s+', lic_str)
    for part in parts:
        if part.strip() in PERMISSIVE_BASES:
            return True
    return False

def fetch_url(url, max_retries=2):
    """Fetch URL with retry and cache."""
    import urllib.request, urllib.error
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_key = hashlib.md5(url.encode()).hexdigest()
    cache_file = os.path.join(CACHE_DIR, cache_key)

    # Check cache
    if os.path.exists(cache_file):
        age = time.time() - os.path.getmtime(cache_file)
        if age < CACHE_TTL:
            with open(cache_file, 'r') as f:
                return f.read()

    # Fetch with retry
    for attempt in range(max_retries + 1):
        try:
            time.sleep(2)  # Rate limit
            req = urllib.request.Request(url, headers={"User-Agent": "typst-brain-scraper/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8')
                with open(cache_file, 'w') as f:
                    f.write(html)
                return html
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"ERROR: Package not found: {url}", file=sys.stderr)
                sys.exit(1)
            if attempt < max_retries:
                wait = 2 ** (attempt + 1)
                print(f"HTTP {e.code}, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
            else:
                raise
    return None

import html

def html_to_md(h):
    # Remove scripts, svgs, a few noise classes
    h = re.sub(r'<script.*?</script>', '', h, flags=re.DOTALL)
    h = re.sub(r'<svg.*?</svg>', '', h, flags=re.DOTALL)
    h = re.sub(r'class="[^"]+"', '', h)
    
    # Pre blocks (code blocks)
    def repl_pre(m):
        code_html = m.group(1)
        code = re.sub(r'<[^>]+>', '', code_html)
        return f"\n```typst\n{html.unescape(code).strip()}\n```\n"
    h = re.sub(r'<pre(?:[^>]*)><code>(.*?)</code></pre>', repl_pre, h, flags=re.DOTALL)
    
    # Inline code
    h = re.sub(r'<code[^>]*>(.*?)</code>', lambda m: f"`{html.unescape(m.group(1))}`", h)
    
    # Headings
    h = re.sub(r'<h1[^>]*>(.*?)</h1\s*>', lambda m: f"\n\n# {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
    h = re.sub(r'<h2[^>]*>(.*?)</h2\s*>', lambda m: f"\n\n## {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
    h = re.sub(r'<h3[^>]*>(.*?)</h3\s*>', lambda m: f"\n\n### {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
    h = re.sub(r'<h4[^>]*>(.*?)</h4\s*>', lambda m: f"\n\n#### {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h)
    
    # Lists
    h = re.sub(r'<li[^>]*>(.*?)</li>', lambda m: f"* {html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n", h, flags=re.DOTALL)
    
    # Paragraphs (just strip tags and add newlines)
    h = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: f"{html.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())}\n\n", h, flags=re.DOTALL)
    
    # Strip all remaining tags
    h = re.sub(r'<[^>]+>', '', h)
    
    # Clean whitespace
    h = re.sub(r'\n{3,}', '\n\n', h)
    return h.strip()

def extract_package_info(html_str, name):
    """Extract key info from Universe package page."""
    info = {"name": name, "version": "", "description": "", "license": "",
            "import_stmt": "", "examples": [], "link": f"https://typst.app/universe/package/{name}", "repo": ""}

    # Version
    m = re.search(r'<h1[^>]*>\s*' + re.escape(name) + r'\s*</h1>\s*<[^>]*>([0-9.]+)', html_str)
    if m: info["version"] = m.group(1)

    # Try to find version from badge or other pattern
    if not info["version"]:
        m = re.search(r'version["\s:-]*(\d+\.\d+\.\d+)', html_str)
        if m: info["version"] = m.group(1)

    # License
    m = re.search(r'License:\s*</dt>\s*<dd[^>]*>\s*([^<]+)', html_str, re.DOTALL)
    if m: info["license"] = m.group(1).strip()

    # Import statement
    info["import_stmt"] = f'#import "@preview/{name}:{info["version"]}": *'

    # Code examples (first 2)
    examples = re.findall(r'<code[^>]*>(.*?)</code>', html_str, re.DOTALL)
    for ex in examples[:2]:
        clean = re.sub(r'<[^>]+>', '', ex).strip()
        if len(clean) > 20 and ('#' in clean or name in clean.lower()):
            info["examples"].append(clean[:300])

    # Repository string
    m_repo = re.search(r'Repository:\s*</dt>\s*<dd[^>]*>\s*<a[^>]*href="([^"]+)"', html_str, re.DOTALL)
    if m_repo:
        info["repo"] = m_repo.group(1).strip()

    return info

def generate_md(info):
    """Generate compressed .md from package info."""
    lines = [
        f"---",
        f"typst_min_version: \"0.12.0\"",
        f"typst_max_version: \"0.14.x\"",
        f"updated_at: \"{time.strftime('%Y-%m-%d')}\"",
        f"token_count: 0",
        f"license: \"{info['license']}\"",
        f"---",
        f"",
        f"# {info['name']} (v{info['version']})",
        f"",
        f"{info['description']}",
        f"",
        f"## Import",
        f"```typst",
        f"{info['import_stmt']}",
        f"```",
    ]
    if info["examples"]:
        lines.extend(["", "## Example"])
        for ex in info["examples"][:2]:
            lines.extend(["```typst", ex, "```"])
    lines.extend(["", f"**Full docs:** {info['link']}"])
    return "\n".join(lines)

def update_index(name, version, description):
    """Add entry to _index.md."""
    index_path = os.path.join(PKG_DIR, "_index.md")
    with open(index_path, 'r') as f:
        content = f.read()
    if name not in content:
        entry = f"| {name} | {version} | {description[:60]} |\n"
        content = content.rstrip() + "\n" + entry
        with open(index_path, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scrape_package.py <package-name>", file=sys.stderr)
        sys.exit(1)

    name = sys.argv[1].lower().strip()
    if not re.match(r'^[a-z0-9-]+$', name):
        print(f"ERROR: Invalid package name: {name}", file=sys.stderr)
        sys.exit(1)

    url = f"https://typst.app/universe/package/{name}"
    print(f"Scraping {url}...")
    html_text = fetch_url(url)
    if not html_text:
        print(f"ERROR: Could not fetch {url}", file=sys.stderr)
        sys.exit(1)

    info = extract_package_info(html_text, name)

    # License check
    if info["license"] and not is_license_permissive(info["license"]):
        print(f"WARNING: Non-permissive license '{info['license']}'. Skipping.", file=sys.stderr)
        sys.exit(1)

    update_index(name, info["version"], info["description"])

    # --- Hierarchical Chunking Architecture ---
    
    # Create required directories
    pkg_root = os.path.join(PKG_DIR, name)
    chunks_dir = os.path.join(pkg_root, "chunks")
    os.makedirs(chunks_dir, exist_ok=True)
    
    # 1) Reformat and Splitting Logic
    m_readme = re.search(r'<div class="readme.*?(?=</main>|<aside)', html_text, re.DOTALL)
    if not m_readme:
        m_readme = re.search(r'<main.*?>(.*?)</main>', html_text, re.DOTALL)
        
    chunk_list = []
    if m_readme:
        readme_md = html_to_md(m_readme.group(1))
        
        # Split by ## Header
        parts = re.split(r'\n##\s+', readme_md)
        overview_text = parts[0].strip()
        
        # Write overview chunk
        if overview_text:
            out_file = "00-overview.md"
            with open(os.path.join(chunks_dir, out_file), 'w', encoding='utf-8') as f:
                f.write(overview_text)
            chunk_list.append((out_file, "Overview & Basic Info"))
            
        # Write subsequent chunks
        for i, part in enumerate(parts[1:]):
            if not part.strip(): continue
            lines = part.split('\n')
            title = lines[0].strip()
            content = "\n".join(lines[1:]).strip()
            
            # Create a safe filename out of the title
            safe_title = re.sub(r'[^a-zA-Z0-9-]', '-', title.lower()[:30]).strip('-')
            if not safe_title: safe_title = f"section-{i}"
            out_file = f"{i+1:02d}-{safe_title}.md"
            
            with open(os.path.join(chunks_dir, out_file), 'w', encoding='utf-8') as f:
                f.write(f"## {title}\n\n{content}")
                
            chunk_list.append((out_file, title))

    # 2) Generate the specific _index.md for this package
    idx_lines = [
        f"---",
        f"package: \"{name}\"",
        f"version: \"{info['version']}\"",
        f"updated_at: \"{time.strftime('%Y-%m-%d')}\"",
        f"---",
        f"# {name} ({info['version']})",
        f"",
        f"{info['description']}",
        f"",
        f"- **Import:** `#import \"@preview/{name}:{info['version']}\": *`",
        f"- **Official:** {info['link']}"
    ]
    if info['repo']:
        idx_lines.append(f"- **Repository:** {info['repo']}")
        
    idx_lines.extend([
        f"",
        f"## Documentation Chunks",
        f"> **LLM INSTRUCTION:** Do NOT read the entire package. Select ONLY 1 or 2 chunks from the list below that match your current task and load them using `view_file`.",
        f""
    ])
    
    for filename, title in chunk_list:
        idx_lines.append(f"- `packages/{name}/chunks/{filename}` — {title}")
        
    if not chunk_list:
        idx_lines.append(f"*No detailed documentation found for this package.*")

    with open(os.path.join(pkg_root, "_index.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(idx_lines))
        
    print(f"✓ Created {pkg_root}/_index.md with {len(chunk_list)} chunks")
