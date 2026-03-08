---
url: https://typst.app/docs/reference/layout/grid/
category: layout
topic: grid
---


# grid (layout)

Arranges content in a grid.

## Signature

`grid(columns: autointrelativefractionarray, rows: autointrelativefractionarray, gutter: autointrelativefractionarray, column-gutter: autointrelativefractionarray, row-gutter: autointrelativefractionarray, inset: relativearraydictionaryfunction, align: autoarrayalignmentfunction, fill: nonecolorgradientarraytilingfunction, stroke: nonelengthcolorgradientarraystroketilingdictionaryfunction, ..content) -> content`

## Parameters

- `columns` (auto | int | relative | fraction | array, optional): The column sizes.

- `rows` (auto | int | relative | fraction | array, optional): The row sizes.

- `gutter` (auto | int | relative | fraction | array, optional): The gaps between rows and columns. This is a shorthand to set column-gutter and row-gutter to the same value.

- `column-gutter` (auto | int | relative | fraction | array, optional): The gaps between columns.

- `row-gutter` (auto | int | relative | fraction | array, optional): The gaps between rows.

- `inset` (relative | array | dictionary | function, optional): How much to pad the cells' content.

- `align` (auto | array | alignment | function, optional): How to align the cells' content.

- `fill` (none | color | gradient | array | tiling | function, optional): How to fill the cells.

- `stroke` (none | length | color | gradient | array | stroke | tiling | dictionary | function, optional): How to stroke the cells.

- `children` (content, required): The contents of the grid cells, plus any extra grid lines specified with the grid.hline and grid.vline elements.

## Examples

```typst
// We use `rect` to emphasize the
// area of cells.
#set rect(
  inset: 8pt,
  fill: rgb("e4e5ea"),
  width: 100%,
)

#grid(
  columns: (60pt, 1fr, 2fr),
  rows: (auto, 60pt),
  gutter: 3pt,
  rect[Fixed width, auto height],
  rect[1/3 of the remains],
  rect[2/3 of the remains],
  rect(height: 100%)[Fixed height],
  grid.cell(
    colspan: 2,
    image("tiger.jpg", width: 100%),
  ),
)
```

```typst
#grid(
  columns: 5,
  gutter: 5pt,
  ..range(25).map(str)
)
```

```typst
#grid(
  columns: 5,

  // By a single value
  align: center,
  // By a single but more complicated value
  inset: (x: 2pt, y: 3pt),
  // By an array of values (cycling)
  fill: (rgb("#239dad50"), none),
  // By a function that returns a value
  stroke: (x, y) => if calc.rem(x + y, 3) == 0 { 0.5pt },

  ..range(5 * 3).map(n => numbering("A", n + 1))
)
```