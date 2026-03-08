---
url: https://typst.app/docs/reference/pdf/header-cell/
category: pdf
topic: header-cell
---


# header-cell (pdf)

Explicitly defines a cell as a header cell.

## Signature

`pdf.header-cell(level: int, scope: str, content) -> content`

## Parameters

- `level` (int, optional): The nesting level of this header cell.

- `scope` (str, optional): What track of the table this header cell applies to.

- `cell` (content, required): The table cell.

## Examples

```typst
#show table.cell.where(x: 0): set text(weight: "medium")
#show table.cell.where(y: 0): set text(weight: "bold")

#table(
  columns: 3,
  align: (start, end, end),

  table.header(
    // Top-left cell: Labels both the nutrient rows
    // and the serving size columns.
    pdf.header-cell(scope: "both")[Nutrient],
    [Per 100g],
    [Per Serving],
  ),

  // First column cells are row headers
  pdf.header-cell(scope: "row")[Calories],
  [250 kcal], [375 kcal],
  pdf.header-cell(scope: "row")[Protein],
  [8g], [12g],
  pdf.header-cell(scope: "row")[Fat],
  [12g], [18g],
  pdf.header-cell(scope: "row")[Carbs],
  [30g], [45g],
)
```