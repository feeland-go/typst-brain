---
typst_min_version: "0.11"
typst_max_version: null
updated_at: "2025-03-07"
token_count: 680
see_also:
  - 02-layout-page.md
  - 06-introspection.md
---

# Table, Figure & References

## Table Basics
```typst
#table(
  columns: (auto, 1fr, auto),
  rows: (auto, auto),
  [*Header*], [*Data*], [*Value*],
  [Row1], [Content], [100],
  [Row2], [More], [200],
)
```

## Table Styling
```typst
#set table(
  stroke: none,
  fill: (col, row) => if row == 0 { gray },
  inset: 8pt,
  align: center,
)
#show table.cell: set text(size: 10pt)
```

## Figure
```typst
#figure(
  image("photo.jpg", width: 80%),
  caption: [A sample image],
  kind: "image",
  supplement: "Figure",
) <fig:photo>

See @fig:photo for details.
```

## Cross-References
```typst
@label           // reference with prefix
@label.display() // customize display
#ref(label, form: "ordinal")  // numbering style

<label>          // define label after element
```

## Bibliography
```typst
#bibliography("refs.bib", style: "apa")
#cite(<key>)     // citation
#cite(<key>, form: "prose")  // narrative citation
```

## Table Advanced
```typst
#table(
  columns: 3,
  stroke: (x, y) => if y == 0 { 2pt },
  table.header([A], [B], [C]),   // repeat header
  table.footer([X], [Y], [Z]),   // repeat footer
  table.hline(),                 // horizontal line
  table.vline(),                 // vertical line
)
```

## Outline
```typst
#outline(title: "Contents")
#outline(title: "Figures", target: figure.where(kind: "image"))
```

---
See also: [02-layout-page](02-layout-page.md), [06-introspection](06-introspection.md)
