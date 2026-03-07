#!/usr/bin/env python3
"""syntax_validator.py — Lightweight .typ syntax validator

Checks:
  - Bracket balance ((), [], {})
  - Import format (@preview/name:X.Y.Z)
  - File path existence for #include and image paths

Exit codes:
  0 = no issues found
  1 = issues found
"""

import re
import sys
import os
from pathlib import Path
from typing import List, Tuple


def check_bracket_balance(content: str) -> List[str]:
    """Check if brackets are balanced."""
    issues = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    
    for i, char in enumerate(content):
        if char in brackets:
            stack.append((char, i))
        elif char in brackets.values():
            if not stack:
                issues.append(f"Unmatched closing '{char}' at position {i}")
            else:
                open_char, pos = stack.pop()
                if brackets[open_char] != char:
                    issues.append(f"Mismatched bracket: '{open_char}' at {pos} closed by '{char}' at {i}")
    
    for open_char, pos in stack:
        issues.append(f"Unclosed '{open_char}' at position {pos}")
    
    return issues


def check_import_format(content: str) -> List[str]:
    """Check if @preview imports use correct format."""
    issues = []
    # Pattern: @preview/name:version or #import "@preview/name:version"
    pattern = r'@preview/([a-zA-Z0-9_-]+):([0-9]+\.[0-9]+\.[0-9]+)'
    
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if '@preview/' in line:
            matches = re.findall(pattern, line)
            if not matches:
                # Check for common mistakes
                if re.search(r'@preview/[a-zA-Z0-9_-]+$', line):
                    issues.append(f"Line {i}: Missing version in @preview import")
                elif re.search(r'@preview/[a-zA-Z0-9_-]+:[^0-9]', line):
                    issues.append(f"Line {i}: Invalid version format (expected X.Y.Z)")
    
    return issues


def check_file_paths(content: str, base_dir: Path) -> List[str]:
    """Check if referenced file paths exist."""
    issues = []
    
    # Pattern for #include "path" or image("path")
    patterns = [
        r'#include\s*"([^"]+)"',
        r'image\s*\(\s*"([^"]+)"',
        r'read\s*\(\s*"([^"]+)"',
    ]
    
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        for pattern in patterns:
            matches = re.findall(pattern, line)
            for match in matches:
                # Skip URLs
                if match.startswith('http://') or match.startswith('https://'):
                    continue
                # Check relative path
                file_path = base_dir / match
                if not file_path.exists():
                    issues.append(f"Line {i}: File not found: {match}")
    
    return issues


def validate_file(filepath: str) -> Tuple[bool, List[str]]:
    """Validate a .typ file."""
    all_issues = []
    path = Path(filepath)
    
    if not path.exists():
        return False, [f"File not found: {filepath}"]
    
    if not path.suffix == '.typ':
        return False, [f"Not a .typ file: {filepath}"]
    
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        return False, [f"Cannot read file: {e}"]
    
    all_issues.extend(check_bracket_balance(content))
    all_issues.extend(check_import_format(content))
    all_issues.extend(check_file_paths(content, path.parent))
    
    return len(all_issues) == 0, all_issues


def main():
    if len(sys.argv) < 2:
        print("Usage: syntax_validator.py <file.typ> [file2.typ ...]", file=sys.stderr)
        sys.exit(1)
    
    all_passed = True
    for filepath in sys.argv[1:]:
        passed, issues = validate_file(filepath)
        if issues:
            print(f"\n{filepath}:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"{filepath}: OK")
        
        if not passed:
            all_passed = False
    
    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
