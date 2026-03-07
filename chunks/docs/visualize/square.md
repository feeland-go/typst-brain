---
url: https://typst.app/docs/reference/visualize/square/
category: visualize
topic: square
---


# square (visualize)

A square with optional content.

## Signature

`square(size: autolength, width: autorelative, height: autorelativefraction, fill: nonecolorgradienttiling, stroke: noneautolengthcolorgradientstroketilingdictionary, radius: relativedictionary, inset: relativedictionary, outset: relativedictionary, nonecontent) -> content`

## Parameters

- `size` (auto | length, optional): The square's side length. This is mutually exclusive with width and height.

- `width` (auto | relative, optional): The square's width. This is mutually exclusive with size and height.

- `height` (auto | relative | fraction, optional): The square's height. This is mutually exclusive with size and width.

- `fill` (none | color | gradient | tiling, optional): How to fill the square. See the rectangle's documentation for more details.

- `stroke` (none | auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the square. See the rectangle's documentation for more details.

- `radius` (relative | dictionary, optional): How much to round the square's corners. See the rectangle's documentation for more details.

- `inset` (relative | dictionary, optional): How much to pad the square's content. See the box's documentation for more details.

- `outset` (relative | dictionary, optional): How much to expand the square's size without affecting the layout. See the box's documentation for more details.

- `body` (none | content, optional): The content to place into the square. The square expands to fit this content, keeping the 1-1 aspect ratio.

## Examples

```typst
// Without content.
#square(size: 40pt)

// With content.
#square[
  Automatically \
  sized to fit.
]
```