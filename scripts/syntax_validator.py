#!/usr/bin/env python3
"""Lightweight .typ syntax validator (no Typst dependency).
Catches ~60% common errors: bracket balance, import format, path existence.
Exit: 0=no issues, 1=issues found."""

import sys, re, os

def validate(filepath):
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    # 1. Bracket/parenthesis balance
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for i, line in enumerate(lines, 1):
        in_string = False
        for ch in line:
            if ch == '"': in_string = not in_string
            if in_string: continue
            if ch in pairs: stack.append((ch, i))
            elif ch in pairs.values():
                if not stack:
                    issues.append(f"Line {i}: Unmatched closing '{ch}'")
                else:
                    open_ch, _ = stack.pop()
                    if pairs.get(open_ch) != ch:
                        issues.append(f"Line {i}: Mismatched '{open_ch}' and '{ch}'")
    for ch, line in stack:
        issues.append(f"Line {line}: Unclosed '{ch}'")

    # 2. Import format check
    for i, line in enumerate(lines, 1):
        m = re.search(r'#import\s+"(@preview/[^"]+)"', line)
        if m:
            pkg = m.group(1)
            if not re.match(r'@preview/[a-z0-9-]+:\d+\.\d+\.\d+', pkg):
                issues.append(f"Line {i}: Import format should be @preview/name:X.Y.Z, got: {pkg}")

    # 3. File path existence (images, data)
    base_dir = os.path.dirname(os.path.abspath(filepath))
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r'(?:image|csv|json|yaml|toml|xml|read)\s*\(\s*"([^"]+)"', line):
            path = m.group(1)
            if path.startswith('/'):
                continue  # absolute, can't check project root
            full = os.path.join(base_dir, path)
            if not os.path.exists(full):
                issues.append(f"Line {i}: File not found: {path} (resolved: {full})")

    return issues

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: syntax_validator.py <file.typ>", file=sys.stderr)
        sys.exit(1)
    issues = validate(sys.argv[1])
    if issues:
        print(f"Found {len(issues)} issue(s):", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        sys.exit(1)
    else:
        print("No issues found.")
        sys.exit(0)
