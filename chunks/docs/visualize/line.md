---
url: https://typst.app/docs/reference/visualize/line/
category: visualize
topic: line
---


# line (visualize)

A line from one point to another.

## Signature

`line(start: array, end: nonearray, length: relative, angle: angle, stroke: lengthcolorgradientstroketilingdictionary) -> content`

## Parameters

- `start` (array, optional): The start point of the line.

- `end` (none | array, optional): The point where the line ends.

- `length` (relative, optional): The line's length. This is only respected if end is none.

- `angle` (angle, optional): The angle at which the line points away from the origin. This is only respected if end is none.

- `stroke` (length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the line.

## Examples

```typst
#set page(height: 100pt)

#line(length: 100%)
#line(end: (50%, 50%))
#line(
  length: 4cm,
  stroke: 2pt + maroon,
)
```

```typst
#set line(length: 100%)
#stack(
  spacing: 1em,
  line(stroke: 2pt + red),
  line(stroke: (paint: blue, thickness: 4pt, cap: "round")),
  line(stroke: (paint: blue, thickness: 1pt, dash: "dashed")),
  line(stroke: (paint: blue, thickness: 1pt, dash: ("dot", 2pt, 4pt, 2pt))),
)
```