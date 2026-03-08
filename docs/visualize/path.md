---
url: https://typst.app/docs/reference/visualize/path/
category: visualize
topic: path
---


# path (visualize)

## Signature

`path(fill: nonecolorgradienttiling, fill-rule: str, stroke: noneautolengthcolorgradientstroketilingdictionary, closed: bool, ..array) -> content`

## Parameters

- `fill` (none | color | gradient | tiling, optional): How to fill the path.

- `fill-rule` (str, optional): The drawing rule used to fill the path.

- `stroke` (none | auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the path.

- `closed` (bool, optional): Whether to close this path with one last Bézier curve. This curve will take into account the adjacent control points. If you want to close with a straight line, simply add one last point that's the same as the start point.

- `vertices` (array, required): The vertices of the path.

## Examples

```typst
// We use `.with` to get a new
// function that has the common
// arguments pre-applied.
#let star = path.with(
  fill: red,
  closed: true,
  (25pt, 0pt),
  (10pt, 50pt),
  (50pt, 20pt),
  (0pt, 20pt),
  (40pt, 50pt),
)

#star(fill-rule: "non-zero")
#star(fill-rule: "even-odd")
```