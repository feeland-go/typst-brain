---
url: https://typst.app/docs/reference/visualize/rect/
category: visualize
topic: rect
---


# rect (visualize)

A rectangle with optional content.

## Signature

`rect(width: autorelative, height: autorelativefraction, fill: nonecolorgradienttiling, stroke: noneautolengthcolorgradientstroketilingdictionary, radius: relativedictionary, inset: relativedictionary, outset: relativedictionary, nonecontent) -> content`

## Parameters

- `width` (auto | relative, optional): The rectangle's width, relative to its parent container.

- `height` (auto | relative | fraction, optional): The rectangle's height, relative to its parent container.

- `fill` (none | color | gradient | tiling, optional): How to fill the rectangle.

- `stroke` (none | auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the rectangle. This can be:

- `radius` (relative | dictionary, optional): How much to round the rectangle's corners, relative to the minimum of the width and height divided by two. This can be:

- `inset` (relative | dictionary, optional): How much to pad the rectangle's content. See the box's documentation for more details.

- `outset` (relative | dictionary, optional): How much to expand the rectangle's size without affecting the layout. See the box's documentation for more details.

- `body` (none | content, optional): The content to place into the rectangle.

## Examples

```typst
// Without content.
#rect(width: 35%, height: 30pt)

// With content.
#rect[
  Automatically sized \
  to fit the content.
]
```

```typst
#rect(fill: blue)
```

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  rect(stroke: red),
  rect(stroke: 2pt),
  rect(stroke: 2pt + red),
)
```