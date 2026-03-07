---
url: https://typst.app/docs/reference/math/mat/
category: math
topic: mat
---


# mat (math)

A matrix.

## Signature

`math.mat(delim: nonestrarraysymbol, align: alignment, augment: noneintdictionary, gap: relative, row-gap: relative, column-gap: relative, ..array) -> content`

## Parameters

- `delim` (none | str | array | symbol, optional): The delimiter to use.

- `align` (alignment, optional): The horizontal alignment that each cell should have.

- `augment` (none | int | dictionary, optional): Draws augmentation lines in a matrix.

- `gap` (relative, optional): The gap between rows and columns.

- `row-gap` (relative, optional): The gap between rows.

- `column-gap` (relative, optional): The gap between columns.

- `rows` (array, required): An array of arrays with the rows of the matrix.

## Examples

```typst
$ mat(
  1, 2, ..., 10;
  2, 2, ..., 10;
  dots.v, dots.v, dots.down, dots.v;
  10, 10, ..., 10;
) $
```

```typst
#set math.mat(delim: "[")
$ mat(1, 2; 3, 4) $
```

```typst
#set math.mat(align: right)
$ mat(-1, 1, 1; 1, -1, 1; 1, 1, -1) $
```