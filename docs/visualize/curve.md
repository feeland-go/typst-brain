---
url: https://typst.app/docs/reference/visualize/curve/
category: visualize
topic: curve
---


# curve (visualize)

A curve consisting of movements, lines, and Bézier segments.

## Signature

`curve(fill: nonecolorgradienttiling, fill-rule: str, stroke: noneautolengthcolorgradientstroketilingdictionary, ..content) -> content`

## Parameters

- `fill` (none | color | gradient | tiling, optional): How to fill the curve.

- `fill-rule` (str, optional): The drawing rule used to fill the curve.

- `stroke` (none | auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the curve.

- `components` (content, required): The components of the curve, in the form of moves, line and Bézier segment, and closes.

## Examples

```typst
#curve(
  fill: blue.lighten(80%),
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.cubic(none, (90pt, 0pt), (50pt, 0pt)),
  curve.close(),
)
```

```typst
// We use `.with` to get a new
// function that has the common
// arguments pre-applied.
#let star = curve.with(
  fill: red,
  curve.move((25pt, 0pt)),
  curve.line((10pt, 50pt)),
  curve.line((50pt, 20pt)),
  curve.line((0pt, 20pt)),
  curve.line((40pt, 50pt)),
  curve.close(),
)

#star(fill-rule: "non-zero")
#star(fill-rule: "even-odd")
```

```typst
#let down = curve.line((40pt, 40pt), relative: true)
#let up = curve.line((40pt, -40pt), relative: true)

#curve(
  stroke: 4pt + gradient.linear(red, blue),
  down, up, down, up, down,
)
```