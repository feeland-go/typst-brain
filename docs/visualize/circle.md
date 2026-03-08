---
url: https://typst.app/docs/reference/visualize/circle/
category: visualize
topic: circle
---


# circle (visualize)

A circle with optional content.

## Signature

`circle(radius: length, width: autorelative, height: autorelativefraction, fill: nonecolorgradienttiling, stroke: noneautolengthcolorgradientstroketilingdictionary, inset: relativedictionary, outset: relativedictionary, nonecontent) -> content`

## Parameters

- `radius` (length, optional): The circle's radius. This is mutually exclusive with width and height.

- `width` (auto | relative, optional): The circle's width. This is mutually exclusive with radius and height.

- `height` (auto | relative | fraction, optional): The circle's height. This is mutually exclusive with radius and width.

- `fill` (none | color | gradient | tiling, optional): How to fill the circle. See the rectangle's documentation for more details.

- `stroke` (none | auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the circle. See the rectangle's documentation for more details.

- `inset` (relative | dictionary, optional): How much to pad the circle's content. See the box's documentation for more details.

- `outset` (relative | dictionary, optional): How much to expand the circle's size without affecting the layout. See the box's documentation for more details.

- `body` (none | content, optional): The content to place into the circle. The circle expands to fit this content, keeping the 1-1 aspect ratio.

## Examples

```typst
// Without content.
#circle(radius: 25pt)

// With content.
#circle[
  #set align(center + horizon)
  Automatically \
  sized to fit.
]
```