---
url: https://typst.app/docs/reference/model/table/
category: model
topic: table
---


# table (model)

A table of items.

## Signature

`table(columns: autointrelativefractionarray, rows: autointrelativefractionarray, gutter: autointrelativefractionarray, column-gutter: autointrelativefractionarray, row-gutter: autointrelativefractionarray, inset: relativearraydictionaryfunction, align: autoarrayalignmentfunction, fill: nonecolorgradientarraytilingfunction, stroke: nonelengthcolorgradientarraystroketilingdictionaryfunction, ..content) -> content`

## Parameters

- `columns` (auto | int | relative | fraction | array, optional): The column sizes. See the grid documentation for more information on track sizing.

- `rows` (auto | int | relative | fraction | array, optional): The row sizes. See the grid documentation for more information on track sizing.

- `gutter` (auto | int | relative | fraction | array, optional): The gaps between rows and columns. This is a shorthand for setting column-gutter and row-gutter to the same value. See the grid documentation for more information on gutters.

- `column-gutter` (auto | int | relative | fraction | array, optional): The gaps between columns. Takes precedence over gutter. See the grid documentation for more information on gutters.

- `row-gutter` (auto | int | relative | fraction | array, optional): The gaps between rows. Takes precedence over gutter. See the grid documentation for more information on gutters.

- `inset` (relative | array | dictionary | function, optional): How much to pad the cells' content.

- `align` (auto | array | alignment | function, optional): How to align the cells' content.

- `fill` (none | color | gradient | array | tiling | function, optional): How to fill the cells.

- `stroke` (none | length | color | gradient | array | stroke | tiling | dictionary | function, optional): How to stroke the cells.

- `children` (content, required): The contents of the table cells, plus any extra table lines specified with the table.hline and table.vline elements.

## Examples

```typst
#table(
  columns: (1fr, auto, auto),
  inset: 10pt,
  align: horizon,
  table.header(
    [], [*Volume*], [*Parameters*],
  ),
  image("cylinder.svg"),
  $ pi h (D^2 - d^2) / 4 $,
  [
    $h$: height \
    $D$: outer radius \
    $d$: inner radius
  ],
  image("tetrahedron.svg"),
  $ sqrt(2) / 12 a^3 $,
  [$a$: edge length]
)
```

```typst
#set table(
  stroke: none,
  gutter: 0.2em,
  fill: (x, y) =>
    if x == 0 or y == 0 { gray },
  inset: (right: 1.5em),
)

#show table.cell: it => {
  if it.x == 0 or it.y == 0 {
    set text(white)
    strong(it)
  } else if it.body == [] {
    // Replace empty cells with 'N/A'
    pad(..it.inset)[_N/A_]
  } else {
    it
  }
}

#let a = table.cell(
  fill: green.lighten(60%),
)[A]
#let b = table.cell(
  fill: aqua.lighten(60%),
)[B]

#table(
  columns: 4,
  [], [Exam 1], [Exam 2], [Exam 3],

  [John], [], a, [],
  [Mary], [], a, a,
  [Robert], b, a, b,
)
```

```typst
#table(
  columns: 2,
  inset: 10pt,
  [Hello],
  [World],
)

#table(
  columns: 2,
  inset: (x: 20pt, y: 10pt),
  [Hello],
  [World],
)
```