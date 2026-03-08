#!/usr/bin/env python3
"""Search the scraped Typst documentation chunks.
Outputs the file paths of the best matching chunks based on the keyword.
Usage: python3 scripts/search_docs.py <keyword>"""

import sys, os, json
from pathlib import Path
import re

BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
INDEX_FILE = os.path.join(BRAIN, "docs", "index.json")

def search(query, top_n=3):
    if not os.path.exists(INDEX_FILE):
        print(f"ERROR: Index file not found at {INDEX_FILE}", file=sys.stderr)
        print("Run scripts/scrape_docs.py first.", file=sys.stderr)
        sys.exit(1)

    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    query_lower = query.lower()
    
    # Simple scoring mechanism with simple stemming/substring leniency
    # If the user types "fractions", we want to also match "frac"
    # A simple approach for this CLI is checking if the query starts with the topic or vice versa
    scored_results = []
    for item in index_data:
        score = 0
        topic = item.get("topic", "").lower()
        category = item.get("category", "").lower()
        summary = item.get("summary", "").lower()

        # Exact/Partial topic match
        if query_lower == topic:
            score += 100
        elif query_lower in topic or topic in query_lower:
            score += 50
        
        # Category match
        if query_lower == category:
            score += 30
        elif query_lower in category or category in query_lower:
            score += 10
            
        # Summary keyword match
        if query_lower in summary:
            # Add weight for multiple occurrences
            score += summary.count(query_lower) * 5

        if score > 0:
            scored_results.append((score, item))

    # Sort descending by score
    scored_results.sort(key=lambda x: x[0], reverse=True)

    if not scored_results:
        print(f"No documentation found matching '{query}'.")
        sys.exit(0)

    print(f"Found {len(scored_results)} matching documents for '{query}'. Top results:")
    for score, item in scored_results[:top_n]:
        # Print path formatted so LLM can easily copy it
        filepath = os.path.join(BRAIN, item['file'])
        print(f"\n--- {item['topic']} ({item['category']}) ---")
        print(f"Path: {filepath}")
        print(f"Summary: {item['summary'][:150]}...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/search_docs.py <keyword>")
        sys.exit(1)
        
    keyword = " ".join(sys.argv[1:])
    search(keyword)
