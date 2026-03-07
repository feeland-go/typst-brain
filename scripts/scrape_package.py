#!/usr/bin/env python3
"""
scrape_package.py — Scrape Typst Universe package docs → compressed .md

Usage:
    python3 scrape_package.py <package-name> [--version X.Y.Z]
    
Exit codes:
    0 = success
    1 = usage error / package not found
    2 = network error
    3 = license not permissive
"""

import sys
import os
import json
import re
import time
import hashlib
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests module required. Install with: pip install requests")
    sys.exit(1)

BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
PKG_DIR = os.path.join(BRAIN, "packages")
CACHE_DIR = os.path.join(BRAIN, ".cache")
CACHE_TTL = 86400  # 24 hours

# Permissive licenses only
PERMISSIVE = {
    "MIT", "Apache-2.0", "Apache-2.0 WITH LLVM-exception",
    "BSD-2-Clause", "BSD-3-Clause", "0BSD",
    "ISC", "Unlicense", "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0",
    "MPL-2.0", "LGPL-2.1", "LGPL-3.0"
}

UNIVERSE_API = "https://typst.app/universe/search"
UNIVERSE_PKG = "https://typst.app/universe/package"


def fetch_url(url, max_retries=2):
    """Fetch URL with retry and cache."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_key = hashlib.md5(url.encode()).hexdigest()
    cache_file = os.path.join(CACHE_DIR, cache_key)

    # Check cache
    if os.path.exists(cache_file):
        age = time.time() - os.path.getmtime(cache_file)
        if age < CACHE_TTL:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return f.read()

    # Fetch with retry
    headers = {"User-Agent": "typst-brain-scraper/1.0"}
    for attempt in range(max_retries + 1):
        try:
            time.sleep(1)  # Rate limit
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            html = resp.text
            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(html)
            return html
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"ERROR: Package not found: {url}", file=sys.stderr)
                sys.exit(1)
            if attempt < max_retries:
                wait = 2 ** (attempt + 1)
                print(f"HTTP {e.response.status_code}, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
            else:
                print(f"ERROR: Network error: {e}", file=sys.stderr)
                sys.exit(2)
        except requests.exceptions.RequestException as e:
            if attempt < max_retries:
                wait = 2 ** (attempt + 1)
                print(f"Network error, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
            else:
                print(f"ERROR: Network error: {e}", file=sys.stderr)
                sys.exit(2)
    return None


def fetch_json(url):
    """Fetch JSON API endpoint."""
    headers = {"User-Agent": "typst-brain-scraper/1.0", "Accept": "application/json"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: API request failed: {e}", file=sys.stderr)
        return None


def extract_package_info(html, name):
    """Extract key info from Universe package page."""
    info = {
        "name": name,
        "version": "",
        "description": "",
        "license": "",
        "import_stmt": "",
        "examples": [],
        "link": f"https://typst.app/universe/package/{name}"
    }

    # Version from various patterns
    m = re.search(r'version["\s:-]*(\d+\.\d+\.\d+)', html, re.IGNORECASE)
    if m:
        info["version"] = m.group(1)

    # Alternative: from badge
    if not info["version"]:
        m = re.search(r'<h1[^>]*>\s*' + re.escape(name) + r'[^<]*</h1>[\s\S]*?(\d+\.\d+\.\d+)', html)
        if m:
            info["version"] = m.group(1)

    # License
    m = re.search(r'License:\s*</dt>\s*<dd[^>]*>\s*([^<]+)', html, re.DOTALL)
    if m:
        info["license"] = m.group(1).strip()
    
    # Alternative license patterns
    if not info["license"]:
        m = re.search(r'license["\s:-]*([A-Za-z0-9.+-]+)', html, re.IGNORECASE)
        if m:
            info["license"] = m.group(1)

    # Import statement
    if info["version"]:
        info["import_stmt"] = f'#import "@preview/{name}:{info["version"]}": *'
    else:
        info["import_stmt"] = f'#import "@preview/{name}: *"'

    # Code examples (first 2)
    examples = re.findall(r'<code[^>]*>(.*?)</code>', html, re.DOTALL)
    for ex in examples[:2]:
        clean = re.sub(r'<[^>]+>', '', ex).strip()
        clean = re.sub(r'\s+', ' ', clean)
        if len(clean) > 20 and ('#' in clean or name in clean.lower()):
            info["examples"].append(clean[:300])

    # Description: first paragraph after h1
    m = re.search(r'<p[^>]*>([^<]{20,300})', html)
    if m:
        info["description"] = re.sub(r'<[^>]+>', '', m.group(1)).strip()[:200]

    return info


def generate_md(info):
    """Generate compressed .md from package info."""
    lines = [
        "---",
        f'typst_min_version: "0.12.0"',
        f'typst_max_version: "0.14.x"',
        f'updated_at: "{time.strftime("%Y-%m-%d")}"',
        f'token_count: 0',
        f'license: "{info["license"]}"',
        "---",
        "",
        f"# {info['name']}" + (f" (v{info['version']})" if info['version'] else ""),
        "",
        info['description'] if info['description'] else "No description available.",
        "",
        "## Import",
        "```typst",
        info['import_stmt'],
        "```",
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
    
    # Create index if doesn't exist
    if not os.path.exists(index_path):
        os.makedirs(PKG_DIR, exist_ok=True)
        header = "# Typst Packages Index\n\n| Package | Version | Description |\n|---------|---------|-------------|\n"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(header)
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if name not in content:
        entry = f"| {name} | {version or 'latest'} | {description[:60]} |\n"
        content = content.rstrip() + "\n" + entry
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)


def main():
    if len(sys.argv) < 2:
        print("Usage: scrape_package.py <package-name> [--version X.Y.Z]", file=sys.stderr)
        print("", file=sys.stderr)
        print("Exit codes:", file=sys.stderr)
        print("  0 = success", file=sys.stderr)
        print("  1 = usage error / package not found", file=sys.stderr)
        print("  2 = network error", file=sys.stderr)
        print("  3 = license not permissive", file=sys.stderr)
        sys.exit(1)

    name = sys.argv[1].lower().strip()
    
    # Validate package name
    if not re.match(r'^[a-z0-9_-]+$', name):
        print(f"ERROR: Invalid package name: {name}", file=sys.stderr)
        sys.exit(1)

    # Build URL
    url = f"{UNIVERSE_PKG}/{name}"
    print(f"Scraping {url}...")
    
    html = fetch_url(url)
    if not html:
        sys.exit(2)

    info = extract_package_info(html, name)

    # License check
    if info["license"]:
        license_check = info["license"].upper()
        # Normalize license name
        if not any(p in license_check for p in PERMISSIVE):
            print(f"WARNING: Non-permissive license '{info['license']}'. Skipping.", file=sys.stderr)
            print(f"Permissive licenses: {', '.join(sorted(PERMISSIVE))}", file=sys.stderr)
            sys.exit(3)

    # Generate and save markdown
    md = generate_md(info)
    os.makedirs(PKG_DIR, exist_ok=True)
    output_path = os.path.join(PKG_DIR, f"{name}.md")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

    update_index(name, info["version"], info["description"])
    
    chars = len(md)
    tokens = chars // 4  # Rough estimate
    print(f"✓ Saved {output_path} (~{tokens} tokens, {chars} chars)")


if __name__ == "__main__":
    main()
