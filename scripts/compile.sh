#!/bin/bash
# compile.sh — Typst compile wrapper with auto font-path
# Exit: 0=success, 1=compile error, 2=typst not found, 3=brain path fail

# Resolve TYPST_BRAIN_HOME
BRAIN="${TYPST_BRAIN_HOME:-}"
if [ -z "$BRAIN" ]; then
  BRAIN="$(cd "$(dirname "$0")/.." && pwd)"
  echo "WARNING: \$TYPST_BRAIN_HOME not set. Using: $BRAIN" >&2
fi
if [ ! -d "$BRAIN" ]; then
  echo "ERROR: typst-brain directory not found at: $BRAIN" >&2
  echo "Set \$TYPST_BRAIN_HOME or run from typst-brain/scripts/" >&2
  exit 3
fi

# Check typst
if ! command -v typst &>/dev/null; then
  echo "ERROR: typst CLI not found. Install: cargo install typst-cli" >&2
  exit 2
fi

INPUT="$1"
OUTPUT="${2:-${INPUT%.typ}.pdf}"
FONT_DIR="$BRAIN/fonts"

if [ -z "$INPUT" ]; then
  echo "Usage: compile.sh <input.typ> [output.pdf]" >&2
  exit 1
fi

# Compile with font-path if fonts/ exists and is non-empty
if [ -d "$FONT_DIR" ] && [ "$(ls -A "$FONT_DIR" 2>/dev/null)" ]; then
  typst compile --font-path "$FONT_DIR" "$INPUT" "$OUTPUT"
else
  typst compile "$INPUT" "$OUTPUT"
fi
