---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
license: "MIT"
---

# polylux (v0.4.0)

Polylux is a package for creating presentations in Typst with a focus on simplicity and flexibility.

## Import
```typst
#import "@preview/polylux:0.4.0": *
```

## Example
```typst
#import "@preview/polylux:0.4.0": *
#show: polylux.with(
  aspect-ratio: "16-9",
)
#slide[
  = My Presentation
  Welcome to polylux!
]
```

## Key Features
- Simple slide creation
- Customizable themes
- Progress indicators
- Logo support

**Full docs:** https://typst.app/universe/package/polylux
