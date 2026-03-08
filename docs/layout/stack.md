---
url: https://typst.app/docs/reference/layout/stack/
category: layout
topic: stack
---


# stack (layout)

Arranges content and spacing horizontally or vertically.

## Signature

`stack(dir: direction, spacing: nonerelativefraction, ..relativefractioncontent) -> content`

## Parameters

- `dir` (direction, optional): The direction along which the items are stacked. Possible values are:

- `spacing` (none | relative | fraction, optional): Spacing to insert between items where no explicit spacing was provided.

- `children` (relative | fraction | content, required): The children to stack along the axis.

## Examples

```typst
#stack(
  dir: ttb,
  rect(width: 40pt),
  rect(width: 120pt),
  rect(width: 90pt),
)
```