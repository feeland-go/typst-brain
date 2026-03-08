---
url: https://typst.app/docs/reference/visualize/polygon/
category: visualize
topic: polygon
---


# polygon (visualize)

A closed polygon.

## Signature

`polygon(fill: nonecolorgradienttiling, fill-rule: str, stroke: noneautolengthcolorgradientstroketilingdictionary, ..array) -> content`

## Parameters

- `fill` (none | color | gradient | tiling, optional): How to fill the polygon.

- `fill-rule` (str, optional): The drawing rule used to fill the polygon.

- `stroke` (none | auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the polygon.

- `vertices` (array, required): The vertices of the polygon. Each point is specified as an array of two relative lengths.

## Examples

```typst
#polygon(
  fill: blue.lighten(80%),
  stroke: blue,
  (20%, 0pt),
  (60%, 0pt),
  (80%, 2cm),
  (0%,  2cm),
)
```

```typst
#polygon.regular(
  fill: blue.lighten(80%),
  stroke: blue,
  size: 30pt,
  vertices: 3,
)
```