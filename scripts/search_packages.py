#!/usr/bin/env python3
"""Semantic Search specifically for Typst Universe Package Documentation.
Usage: python3 scripts/search_packages.py <package_name> <query_keywords>"""

import sys, os, re
from pathlib import Path

# --- Configuration ---
BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
PKG_DOCS_DIR = os.path.join(BRAIN, "packages", "docs")

def score_section(title, content, query_words):
    """Simple term-frequency scoring."""
    score = 0
    text = (title + " " + content).lower()
    for w in query_words:
        score += text.count(w) * (3 if w in title.lower() else 1)
    return score

def search_package(pkg_name, query_str):
    doc_path = os.path.join(PKG_DOCS_DIR, f"{pkg_name}.md")
    
    if not os.path.exists(doc_path):
        print(f"Error: Detailed docs for package '{pkg_name}' not found.")
        print("Please run `python3 scripts/scrape_package.py " + pkg_name + "` first to fetch the detailed documentation layer.")
        return

    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by markdown headers (#, ##, ###)
    # We find all matches of ^#+ Header text and the content until the next header
    sections = []
    current_title = "Overview"
    current_content = []
    
    lines = content.split('\n')
    for line in lines:
        if re.match(r'^#{1,6}\s+', line):
            if current_content:
                sections.append({"title": current_title, "text": "\n".join(current_content).strip()})
            current_title = line.strip()
            current_content = []
        else:
            current_content.append(line)
            
    if current_content:
        sections.append({"title": current_title, "text": "\n".join(current_content).strip()})

    query_words = [w.lower() for w in query_str.split()]
    
    scored_sections = []
    for sec in sections:
        score = score_section(sec["title"], sec["text"], query_words)
        if score > 0 or not query_words: # If no query words or score > 0
            scored_sections.append((score, sec))
            
    # Sort by score descending
    scored_sections.sort(key=lambda x: x[0], reverse=True)
    
    print(f"=== Search Results for '{query_str}' in package '{pkg_name}' ===\n")
    if not scored_sections:
        print("No specific sections matched your query. Returning the top 2 sections instead:\n")
        scored_sections = [(0, s) for s in sections[:2]]
        
    for score, sec in scored_sections[:3]: # Return top 3 blocks max to save tokens
        print(f"{sec['title']}")
        print(f"{sec['text']}")
        print("-" * 40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 search_packages.py <package_name> '<query keywords>'", file=sys.stderr)
        sys.exit(1)
        
    pkg_name = sys.argv[1].lower()
    query = " ".join(sys.argv[2:])
    search_package(pkg_name, query)
