#!/bin/bash
# compile.sh — Typst compile wrapper with auto font-path
# Exit: 0=success, 1=compile error, 2=typst not found, 3=brain path fail

set -euo pipefail

BRAIN="${TYPST_BRAIN_HOME:-}"
if [ -z "$BRAIN" ]; then
  BRAIN="$(cd "$(dirname "$0")/.." && pwd)"
fi

if [ ! -d "$BRAIN" ]; then
  echo "ERROR: Brain path not found: $BRAIN" >&2
  exit 3
fi

if ! command -v typst &> /dev/null; then
  echo "ERROR: typst not found in PATH" >&2
  exit 2
fi

INPUT="${1:-}"
OUTPUT="${2:-}"

if [ -z "$INPUT" ]; then
  echo "Usage: compile.sh <input.typ> [output.pdf]" >&2
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "ERROR: Input file not found: $INPUT" >&2
  exit 1
fi

FONT_PATH=""
if [ -d "$BRAIN/fonts" ]; then
  FONT_PATH="$BRAIN/fonts"
fi

TYPOST_ARGS=()
if [ -n "$FONT_PATH" ]; then
  TYPOST_ARGS+=(--font-path "$FONT_PATH")
fi

if [ -n "$OUTPUT" ]; then
  TYPOST_ARGS+=("$INPUT" "$OUTPUT")
else
  TYPOST_ARGS+=("$INPUT")
fi

echo "Compiling: $INPUT"
if [ -n "$OUTPUT" ]; then
  echo "Output: $OUTPUT"
fi

typst compile "${TYPOST_ARGS[@]}"

echo "Done."
