---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
license: "LGPL-3.0"
---

# cetz (v0.3.0)

Cetz is a library for drawing coordinate-based vector graphics in Typst. Think of it as TikZ for Typst.

## Import
```typst
#import "@preview/cetz:0.3.0": *
```

## Example
```typst
#import "@preview/cetz:0.3.0": *
#canvas({
  import cetz.draw: *
  line((0, 0), (2, 1))
  circle((1, 0.5), radius: 0.3)
})
```

## Key Features
- Vector graphics drawing
- Coordinate system
- Lines, circles, polygons
- Transformations and styling

**Full docs:** https://typst.app/universe/package/cetz
