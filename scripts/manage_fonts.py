#!/usr/bin/env python3
"""
manage_fonts.py — Manage fonts for Typst projects

Usage:
    python3 manage_fonts.py list              # List all available fonts
    python3 manage_fonts.py install <font>    # Install a font
    python3 manage_fonts.py check             # Check font availability
"""

import sys
import os
import subprocess
from pathlib import Path

BRAIN = os.environ.get("TYPST_BRAIN_HOME", str(Path(__file__).parent.parent))
FONT_DIR = os.path.join(BRAIN, "fonts")


def get_typst_fonts():
    """Get list of fonts known to Typst."""
    try:
        result = subprocess.run(
            ["typst", "fonts"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
        return []
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []


def list_fonts():
    """List all available fonts."""
    print("=== Typst System Fonts ===")
    fonts = get_typst_fonts()
    if fonts:
        for font in sorted(fonts):
            print(f"  • {font}")
        print(f"\nTotal: {len(fonts)} fonts")
    else:
        print("  Could not retrieve font list (typst not available)")
    
    print("\n=== Local Font Directory ===")
    if os.path.exists(FONT_DIR):
        local_fonts = []
        for root, dirs, files in os.walk(FONT_DIR):
            for f in files:
                if f.endswith(('.ttf', '.otf', '.woff', '.woff2')):
                    local_fonts.append(os.path.join(root, f))
        if local_fonts:
            for f in local_fonts:
                print(f"  • {os.path.basename(f)}")
            print(f"\nTotal: {len(local_fonts)} local fonts")
        else:
            print("  (empty)")
    else:
        print("  (directory does not exist)")


def check_font(font_name):
    """Check if a specific font is available."""
    fonts = get_typst_fonts()
    matches = [f for f in fonts if font_name.lower() in f.lower()]
    
    if matches:
        print(f"✓ Font '{font_name}' found:")
        for m in matches:
            print(f"  • {m}")
    else:
        print(f"✗ Font '{font_name}' not found")
        print("\nAvailable fonts containing similar names:")
        similar = [f for f in fonts if any(part in f.lower() for part in font_name.lower().split())]
        for s in similar[:5]:
            print(f"  • {s}")


def install_font(font_path):
    """Install a font to local font directory."""
    if not os.path.exists(font_path):
        print(f"ERROR: Font file not found: {font_path}", file=sys.stderr)
        sys.exit(1)
    
    os.makedirs(FONT_DIR, exist_ok=True)
    
    import shutil
    dest = os.path.join(FONT_DIR, os.path.basename(font_path))
    shutil.copy2(font_path, dest)
    print(f"✓ Installed font to: {dest}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "list":
        list_fonts()
    elif command == "check":
        if len(sys.argv) < 3:
            print("Usage: manage_fonts.py check <font-name>", file=sys.stderr)
            sys.exit(1)
        check_font(sys.argv[2])
    elif command == "install":
        if len(sys.argv) < 3:
            print("Usage: manage_fonts.py install <font-file>", file=sys.stderr)
            sys.exit(1)
        install_font(sys.argv[2])
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
