---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
license: "LGPL-3.0-or-later"
---

# cetz (v0.4.2)

Drawing with Typst made easy, providing an API inspired by TikZ and Processing. Includes modules for plotting, charts and tree layout.

## Import
```typst
#import "@preview/cetz:0.4.2": *
```

## Example
```typst
#import "@preview/cetz:0.4.2"

#cetz.canvas({
  import cetz.draw: *
  // Your drawing code goes here
})
```

**Full docs:** https://typst.app/universe/package/cetz