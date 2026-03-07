---
url: https://typst.app/docs/reference/visualize/stroke/
category: visualize
topic: stroke
---


# stroke (visualize)

Defines how to draw a line.

## Signature

`stroke(autocolorgradienttiling, autolength, autostr, autostr, noneautostrarraydictionary, autofloat) -> stroke paint auto or color or gradient or tiling Required Positional`

## Examples

```typst
#set line(length: 100%)
#stack(
  spacing: 1em,
  line(stroke: 2pt + red),
  line(stroke: (paint: blue, thickness: 4pt, cap: "round")),
  line(stroke: (paint: blue, thickness: 1pt, dash: "dashed")),
  line(stroke: 2pt + gradient.linear(..color.map.rainbow)),
)
```

```typst
#let my-func(x) = {
    x = stroke(x) // Convert to a stroke
    [Stroke has thickness #x.thickness.]
}
#my-func(3pt) \
#my-func(red) \
#my-func(stroke(cap: "round", thickness: 1pt))
```

```typst
#set line(length: 100%, stroke: 2pt)
#stack(
  spacing: 1em,
  line(stroke: (dash: "dashed")),
  line(stroke: (dash: (10pt, 5pt, "dot", 5pt))),
  line(stroke: (dash: (array: (10pt, 5pt, "dot", 5pt), phase: 10pt))),
)
```