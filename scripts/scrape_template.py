#!/usr/bin/env python3
"""Scrape Typst Universe package docs → compressed .md (<600 tok).
Usage: scrape_template.py <package-name>"""

import sys, os, time, re, json, hashlib
from pathlib import Path

BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
PKG_DIR = os.path.join(BRAIN, "templates")
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

def extract_package_info(html, name):
    """Extract key info from Universe package page."""
    info = {"name": name, "version": "", "description": "", "license": "",
            "import_stmt": "", "examples": [], "link": f"https://typst.app/universe/package/{name}"}

    # Version
    m = re.search(r'<h1[^>]*>\s*' + re.escape(name) + r'\s*</h1>\s*<[^>]*>([0-9.]+)', html)
    if m: info["version"] = m.group(1)

    # Try to find version from badge or other pattern
    if not info["version"]:
        m = re.search(r'version["\s:-]*(\d+\.\d+\.\d+)', html)
        if m: info["version"] = m.group(1)

    # License
    m = re.search(r'License:\s*</dt>\s*<dd[^>]*>\s*([^<]+)', html, re.DOTALL)
    if m: info["license"] = m.group(1).strip()

    # Import statement
    info["import_stmt"] = f'#import "@preview/{name}:{info["version"]}": *'

    # Code examples (first 2)
    examples = re.findall(r'<code[^>]*>(.*?)</code>', html, re.DOTALL)
    for ex in examples[:2]:
        clean = re.sub(r'<[^>]+>', '', ex).strip()
        if len(clean) > 20 and ('#' in clean or name in clean.lower()):
            info["examples"].append(clean[:300])

    # Description: first paragraph after h1
    m = re.search(r'<p[^>]*>([^<]{20,300})', html)
    if m: info["description"] = re.sub(r'<[^>]+>', '', m.group(1)).strip()[:200]

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
        print("Usage: scrape_template.py <package-name>", file=sys.stderr)
        sys.exit(1)

    name = sys.argv[1].lower().strip()
    if not re.match(r'^[a-z0-9-]+$', name):
        print(f"ERROR: Invalid package name: {name}", file=sys.stderr)
        sys.exit(1)

    url = f"https://typst.app/universe/package/{name}"
    print(f"Scraping {url}...")
    html = fetch_url(url)

    info = extract_package_info(html, name)

    # License check
    if info["license"] and not is_license_permissive(info["license"]):
        print(f"WARNING: Non-permissive license '{info['license']}'. Skipping.", file=sys.stderr)
        sys.exit(1)

    md = generate_md(info)
    output_path = os.path.join(PKG_DIR, f"{name}.md")
    with open(output_path, 'w') as f:
        f.write(md)

    update_index(name, info["version"], info["description"])
    chars = len(md)
    print(f"✓ Saved {output_path} (~{chars//4} tokens)")
