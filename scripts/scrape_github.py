#!/usr/bin/env python3
"""Scrape raw GitHub READMEs directly and integrate them as packages.
Usage: python3 scrape_github.py <package_name> <version> <github_repo_url>"""

import sys, os, time, re, html
import urllib.request
from urllib.error import URLError
from pathlib import Path

# --- Config ---
BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
PKG_DIR = os.path.join(BRAIN, "packages")

def fetch_raw_readme(repo_url):
    """Converts a standard github URL to its raw content URL and fetches it."""
    # Convert https://github.com/user/repo to https://raw.githubusercontent.com/user/repo/main/README.md
    if not repo_url.startswith("https://github.com/"):
        return None
        
    parts = repo_url.rstrip('/').split('/')
    if len(parts) < 5: return None
    
    user, repo = parts[-2], parts[-1]
    
    # Try main, then master
    branches = ['main', 'master']
    for b in branches:
        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{b}/README.md"
        try:
            req = urllib.request.Request(raw_url, headers={"User-Agent": "typst-brain-scraper/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"✓ Found README on branch '{b}'")
                return resp.read().decode('utf-8')
        except URLError:
            continue
            
    return None

def main():
    if len(sys.argv) < 4:
        print("Usage: scrape_github.py <package_name> <version> <github_repo_url>")
        sys.exit(1)
        
    pkg = sys.argv[1].lower()
    version = sys.argv[2]
    repo_url = sys.argv[3]
    
    print(f"Scraping GitHub Repository: {repo_url} for package '{pkg}' v{version}")
    readme_md = fetch_raw_readme(repo_url)
    
    if not readme_md:
        print("Error: Could not fetch README.md from the provided GitHub URL.")
        sys.exit(1)
        
    # Create required directories
    pkg_root = os.path.join(PKG_DIR, pkg)
    chunks_dir = os.path.join(pkg_root, "chunks")
    os.makedirs(chunks_dir, exist_ok=True)
    
    # Prune existing chunks
    for f in os.listdir(chunks_dir):
        os.remove(os.path.join(chunks_dir, f))
        
    # --- Splitting Logic ---
    parts = re.split(r'\n##\s+', readme_md)
    overview_text = parts[0].strip()
    chunk_list = []
    
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
        
        safe_title = re.sub(r'[^a-zA-Z0-9-]', '-', title.lower()[:30]).strip('-')
        if not safe_title: safe_title = f"section-{i}"
        out_file = f"{i+1:02d}-{safe_title}.md"
        
        with open(os.path.join(chunks_dir, out_file), 'w', encoding='utf-8') as f:
            f.write(f"## {title}\n\n{content}")
            
        chunk_list.append((out_file, title))

    # --- Generate Index ---
    idx_lines = [
        f"---",
        f"package: \"{pkg}\"",
        f"version: \"{version}\"",
        f"updated_at: \"{time.strftime('%Y-%m-%d')}\"",
        f"---",
        f"# {pkg} ({version})",
        f"",
        f"- **Import:** `#import \"@preview/{pkg}:{version}\": *`",
        f"- **Repository:** {repo_url}"
    ]
        
    idx_lines.extend([
        f"",
        f"## Documentation Chunks",
        f"> **LLM INSTRUCTION:** Do NOT read the entire package. Select ONLY 1 or 2 chunks from the list below that match your current task and load them using `view_file`.",
        f""
    ])
    
    for filename, title in chunk_list:
        idx_lines.append(f"- `packages/{pkg}/chunks/{filename}` — {title}")

    with open(os.path.join(pkg_root, "_index.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(idx_lines))
        
    print(f"✓ Created {pkg_root}/_index.md with {len(chunk_list)} chunks directly from GitHub Repo")

if __name__ == "__main__":
    main()
