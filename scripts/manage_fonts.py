#!/usr/bin/env python3
"""Typst font manager wrapper.
check/list/search local fonts vs typst fonts"""

import sys, os, subprocess

BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
FONT_DIR = os.path.join(BRAIN, "fonts")

def run_typst_fonts():
    try:
        cmd = ["typst", "fonts", "--font-path", FONT_DIR]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return []
    except FileNotFoundError:
        print("ERROR: typst CLI not found", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    os.makedirs(FONT_DIR, exist_ok=True)
    if len(sys.argv) < 2:
        print("Usage: manage_fonts.py [list|search <query>]")
        sys.exit(0)
    
    cmd = sys.argv[1]
    
    if cmd == "list":
        fonts = run_typst_fonts()
        print(f"Found {len(fonts)} fonts in {FONT_DIR}")
        for f in fonts[:10]:
            print(f"  {f}")
        if len(fonts) > 10:
            print(f"  ... and {len(fonts)-10} more")
            
    elif cmd == "search" and len(sys.argv) > 2:
        query = sys.argv[2].lower()
        fonts = run_typst_fonts()
        matches = [f for f in fonts if query in f.lower()]
        print(f"Found {len(matches)} matches for '{query}'")
        for m in matches:
            print(f"  {m}")
