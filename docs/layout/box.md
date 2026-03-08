---
url: https://typst.app/docs/reference/layout/box/
category: layout
topic: box
---


# box (layout)

An inline-level container that sizes content.

## Signature

`box(width: autorelativefraction, height: autorelative, baseline: relative, fill: nonecolorgradienttiling, stroke: nonelengthcolorgradientstroketilingdictionary, radius: relativedictionary, inset: relativedictionary, outset: relativedictionary, clip: bool, nonecontent) -> content`

## Parameters

- `width` (auto | relative | fraction, optional): The width of the box.

- `height` (auto | relative, optional): The height of the box.

- `baseline` (relative, optional): An amount to shift the box's baseline by.

- `fill` (none | color | gradient | tiling, optional): The box's background color. See the rectangle's documentation for more details.

- `stroke` (none | length | color | gradient | stroke | tiling | dictionary, optional): The box's border color. See the rectangle's documentation for more details.

- `radius` (relative | dictionary, optional): How much to round the box's corners. See the rectangle's documentation for more details.

- `inset` (relative | dictionary, optional): How much to pad the box's content.

- `outset` (relative | dictionary, optional): How much to expand the box's size without affecting the layout.

- `clip` (bool, optional): Whether to clip the content inside the box.

- `body` (none | content, optional): The contents of the box.

## Examples

```typst
Refer to the docs
#box(
  height: 9pt,
  image("docs.svg")
)
for more information.
```

```typst
Line in #box(width: 1fr, line(length: 100%)) between.
```

```typst
Image: #box(baseline: 40%, image("tiger.jpg", width: 2cm)).
```