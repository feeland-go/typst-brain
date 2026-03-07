---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
license: "MIT"
---

# fletcher (v0.5.3)

A package for drawing diagrams with Typst. Create flowcharts, sequence diagrams, and other visual diagrams using a simple syntax.

## Import
```typst
#import "@preview/fletcher:0.5.3": *
```

## Example
```typst
#import "@preview/fletcher:0.5.3": *
#diagram({
  node("Start")
  edge("->")
  node("Process")
})
```

## Key Features
- Flowchart diagrams
- Sequence diagrams
- Node and edge customization
- Automatic layout

**Full docs:** https://typst.app/universe/package/fletcher
