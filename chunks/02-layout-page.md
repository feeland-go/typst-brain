---
typst_min_version: "0.11"
typst_max_version: null
updated_at: "2025-03-07"
token_count: 620
see_also:
  - 03-table-figure.md
  - 05-text-styling.md
---

# Layout & Page

## Page Setup
```typst
#set page(
  paper: "a4",
  margin: (x: 1cm, y: 1.5cm),
  columns: 2,
  column-gutter: 1em,
  header: [Header],
  footer: [Page #counter(page).display()],
)
#set page(width: 200pt, height: auto)  // custom size
```

## Grid Layout
```typst
#grid(
  columns: (1fr, 2fr, 1fr),  // flexible widths
  rows: (auto, 1fr),
  gutter: 10pt,
  [Cell 1], [Cell 2], [Cell 3],
  [Row 2], [Spans], [Here],
)
```

## Columns
```typst
#columns(2, gutter: 12pt)[
  Content flows between columns automatically.
]
#colbreak()  // force column break
```

## Spacing
```typst
#h(1em)      // horizontal space
#v(2em)      // vertical space
#h(1fr)      // fill remaining space
#v(1fr, weak: true)  // collapse at page breaks
```

## Shapes & Drawing
```typst
#rect(width: 100%, height: 2pt, fill: blue)
#square(size: 20pt, fill: red)
#circle(radius: 15pt)
#polygon((0%, 0%), (100%, 50%), (0%, 100%))
#line(start: (0, 0), end: (100%, 0), stroke: 2pt)
```

## Transforms
```typst
#rotate(45deg)[Rotated text]
#scale(1.5)[Larger]
#move(dx: 10pt, dy: 5pt)[Shifted]
#skew(ax: 10deg)[Slanted]
#hide[Invisible but takes space]
```

## Place (Absolute Positioning)
```typst
#place(center)[Centered overlay]
#place(top + right)[Corner]
#place(dx: 50pt, dy: 30pt)[Offset]
```

---
See also: [03-table-figure](03-table-figure.md), [05-text-styling](05-text-styling.md)
