---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
license: "MIT"
---

# polylux (v0.4.0)

Presentation slides creation with Typst

## Import
```typst
#import "@preview/polylux:0.4.0": *
```

## Example
```typst
// Get Polylux from the official package repository
#import "@preview/polylux:0.4.0": *

// Make the paper dimensions fit for a presentation and the text larger
#set page(paper: "presentation-16-9")
#set text(size: 25pt, font: "Lato")

// Use #slide to create a slide and style it using your favourit
```

**Full docs:** https://typst.app/universe/package/polylux