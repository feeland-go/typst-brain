#!/usr/bin/env bash
# Utility script to deploy the TYPST_NAVIGATOR to other projects.
# Usage: ./sync_navigator.sh /path/to/other/project

if [ -z "$1" ]; then
    echo "Usage: $0 <target_directory>"
    exit 1
fi

TARGET_DIR="$1"
BRAIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAVIGATOR="$BRAIN_DIR/TYPST_NAVIGATOR.md"

if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Target directory '$TARGET_DIR' does not exist."
    exit 1
fi

# Copy the navigator
cp "$NAVIGATOR" "$TARGET_DIR/TYPST_NAVIGATOR.md"
echo "Successfully deployed TYPST_NAVIGATOR.md to $TARGET_DIR"
