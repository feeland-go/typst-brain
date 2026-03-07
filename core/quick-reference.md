---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
---

# Typst Quick Reference (L1)

## Document Setup
```typst
#set page(paper: "a4", margin: (x: 2.5cm, y: 2cm), numbering: "1")
#set text(font: "Libertinus Serif", size: 11pt, lang: "id")
#set heading(numbering: "1.1.")
#set par(justify: true, leading: 0.65em)
```

## Headings
```typst
= Heading 1
== Heading 2
=== Heading 3
```

## Text Formatting
```typst
*bold*  _italic_  `code`  #underline[text]  #highlight[text]
#text(fill: blue, weight: "bold")[colored bold]
```

## Set Rules & Show Rules
```typst
// Set rule: configure element properties
#set text(font: "Arial", size: 12pt)
#set page(margin: 2cm)

// Show rule: redefine element appearance
#show heading.where(level: 1): it => [
  #set text(size: 18pt, fill: navy)
  #block(above: 1.5em, below: 0.8em)[#it.body]
]
```

## Lists
```typst
- Bullet item        // unordered
  - Nested item
+ Numbered item      // ordered
  + Nested number
/ Term: Description  // definition list
```

## Images & Figures
```typst
#figure(
  image("path/to/image.png", width: 80%),
  caption: [Caption text],
) <label>
// Reference: @label
```

## Tables (Basic)
```typst
#table(
  columns: (1fr, 2fr, 1fr),
  inset: 8pt,
  align: center,
  table.header[*Col A*][*Col B*][*Col C*],
  [Row 1A], [Row 1B], [Row 1C],
  [Row 2A], [Row 2B], [Row 2C],
)
```

## Links & References
```typst
#link("https://example.com")[Click here]
See @heading-label or @figure-label
```

## Outline (TOC)
```typst
#outline(indent: auto)
```

## Page Break
```typst
#pagebreak()
```

## Import (Universe Packages)
```typst
#import "@preview/package-name:0.1.0": *
// Example: #import "@preview/fletcher:0.5.8": diagram, node, edge
```

## File Paths
```typst
// Relative (from current .typ file location):
#image("images/photo.png")
// Absolute (from project root):
#image("/assets/logo.png")
```

## Block & Box
```typst
#block(fill: luma(240), inset: 12pt, radius: 4pt)[
  Block content with background
]
#box(width: 1fr)[Inline box]
```

## Spacing
```typst
#v(1em)  // vertical space
#h(2cm)  // horizontal space
```

## Color
```typst
#text(fill: rgb("#1B4F72"))[Colored]
#text(fill: red)[Red]
#rect(fill: blue.lighten(80%), stroke: blue)
```

## Raw Code Block
```typst
#raw(lang: "python", block: true)[
  def hello():
      print("world")
]
// Or: ```python ... ```
```

## Footnote
```typst
This has a footnote#footnote[Footnote text here.]
```

## Bibliography
```typst
#bibliography("refs.bib", style: "ieee")
// Cite: @key or #cite(<key>)
```

## CLI Commands
```bash
typst compile file.typ                    # → file.pdf
typst compile file.typ output.pdf         # custom output
typst compile --font-path ./fonts file.typ # custom fonts
typst watch file.typ                      # auto-recompile
typst init @preview/template-name         # init from template
typst fonts                               # list available fonts
typst fonts --font-path ./fonts           # list with custom dir
```
