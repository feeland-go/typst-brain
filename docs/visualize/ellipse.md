---
url: https://typst.app/docs/reference/visualize/ellipse/
category: visualize
topic: ellipse
---


# ellipse (visualize)

An ellipse with optional content.

## Signature

`ellipse(width: autorelative, height: autorelativefraction, fill: nonecolorgradienttiling, stroke: noneautolengthcolorgradientstroketilingdictionary, inset: relativedictionary, outset: relativedictionary, nonecontent) -> content`

## Parameters

- `width` (auto | relative, optional): The ellipse's width, relative to its parent container.

- `height` (auto | relative | fraction, optional): The ellipse's height, relative to its parent container.

- `fill` (none | color | gradient | tiling, optional): How to fill the ellipse. See the rectangle's documentation for more details.

- `stroke` (none | auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the ellipse. See the rectangle's documentation for more details.

- `inset` (relative | dictionary, optional): How much to pad the ellipse's content. See the box's documentation for more details.

- `outset` (relative | dictionary, optional): How much to expand the ellipse's size without affecting the layout. See the box's documentation for more details.

- `body` (none | content, optional): The content to place into the ellipse.

## Examples

```typst
// Without content.
#ellipse(width: 35%, height: 30pt)

// With content.
#ellipse[
  #set align(center)
  Automatically sized \
  to fit the content.
]
```