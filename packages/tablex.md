---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
license: "MIT"
---

# tablex (v0.0.9)

An enhanced table package for Typst with advanced features like cell spanning, rotation, and more.

## Import
```typst
#import "@preview/tablex:0.0.9": *
```

## Example
```typst
#import "@preview/tablex:0.0.9": *
#tablex(
  columns: 3,
  rows: 2,
  [A], [B], [C],
  [D], [E], [F],
)
```

## Key Features
- Cell spanning (colspan/rowspan)
- Cell rotation
- Custom borders
- Header rows

**Full docs:** https://typst.app/universe/package/tablex
