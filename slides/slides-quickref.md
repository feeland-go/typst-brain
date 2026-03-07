---
id: slides-quickref
title: Typst Slides Quick Reference
type: quickref
created: 2026-03-07
updated: 2026-03-07
version: "1.0"
tags: [slides, presentation, quickref]
---

# Typst Slides Quick Reference

## Presentation Packages

### Touying (Recommended)
```typst
#import "@preview/touying:0.5.0": *

#show: touying-slides.with(
  theme: "simple",
  aspect-ratio: "16-9",
)

= Title Slide
== Section Title
Content here
```

### Polylux
```typst
#import "@preview/polylux:0.4.0": *

#show: polylux.with(
  aspect-ratio: "16-9",
)

#slide[
  = Title
  Content
]
```

## Common Slide Patterns

### Title Slide
```typst
= Presentation Title
#align(center)[
  Author Name
  Date
]
```

### Bullet Points
```typst
== Key Points
- First point
- Second point
  - Sub-point
- Third point
```

### Two Columns
```typst
#grid(
  columns: (1fr, 1fr),
  [
    Left column content
  ],
  [
    Right column content
  ],
)
```

### Code Block
```typst
```typst
#let x = 5
#calc.pow(x, 2)
```
```

### Image
```typst
#align(center)[
  #image("diagram.png", width: 80%)
]
```

### Math
```typst
$ integral_0^infinity e^(-x^2) dif x = sqrt(pi)/2 $
```

## Themes

### Touying Themes
- `simple` - Clean, minimal
- `metropolis` - Modern, flat
- `university` - Academic style

### Custom Colors
```typst
#set text(fill: rgb("#2c3e50"))
#set page(fill: rgb("#ecf0f1"))
```

## Slide Layout Tips

| Element | Syntax |
|---------|--------|
| Section | `= Title` |
| Subsection | `== Title` |
| Page break | `#pagebreak()` |
| Center | `#align(center)[...]` |
| Columns | `#grid(columns: (1fr, 1fr), ...)` |

## Export to PDF
```bash
typst compile slides.typ slides.pdf
```

## Best Practices
1. Keep slides simple - one idea per slide
2. Use consistent formatting
3. Limit text - use bullet points
4. Test on projector before presenting
5. Export backup PDF
