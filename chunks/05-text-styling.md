---
typst_min_version: "0.11"
typst_max_version: null
updated_at: "2025-03-07"
token_count: 650
see_also:
  - 02-layout-page.md
---

# Text Styling

## Basic Formatting
```typst
*bold*                // strong
_italic_              // emphasis
`code`                // raw inline
```typ block```       // raw block
#super[superscript]   // or x^super in math
#sub[subscript]       // or x_sub in math
#strike[strikethrough]
#underline[underlined]
#overline[overlined]
#highlight[highlighted]
```

## Text Properties
```typst
#set text(
  font: "Helvetica",
  size: 12pt,
  weight: "bold",
  style: "italic",
  fill: blue,
  tracking: 0.5pt,     // letter spacing
  baseline: 2pt,
  top-edge: "bounds",
  bottom-edge: "bounds",
)
```

## Color
```typst
#text(fill: red)[Red text]
#text(fill: rgb("#FF5500"))[Custom]
#text(fill: rgb(255, 85, 0))[RGB]
#text(fill: luma(128))[Gray]
#text(fill: cmyk(0.5, 0.3, 0, 0.2))[CMYK]
```

## Gradient
```typst
#rect(
  width: 100%,
  height: 20pt,
  fill: gradient.linear(red, blue),
)
#rect(fill: gradient.linear(..(red, blue), angle: 45deg))
#circle(fill: gradient.radial(red, blue))
```

## Tiling Pattern
```typst
#let pattern = pattern((
  size: (10pt, 10pt),
  square(size: 8pt, fill: gray),
))
#rect(fill: pattern)
```

## Stroke (Borders)
```typst
#rect(stroke: 2pt + black)
#rect(stroke: (x: 1pt, y: 2pt, top: red))
#line(stroke: (paint: blue, thickness: 2pt, dash: "dashed"))
```

## Link Styling
```typst
#set link(fill: blue)
#set link(underline: true)
```

---
See also: [02-layout-page](02-layout-page.md)
