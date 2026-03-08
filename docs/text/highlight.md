---
url: https://typst.app/docs/reference/text/highlight/
category: text
topic: highlight
---


# highlight (text)

Highlights text with a background color.

## Signature

`highlight(fill: nonecolorgradienttiling, stroke: nonelengthcolorgradientstroketilingdictionary, top-edge: lengthstr, bottom-edge: lengthstr, extent: length, radius: relativedictionary, content) -> content`

## Parameters

- `fill` (none | color | gradient | tiling, optional): The color to highlight the text with.

- `stroke` (none | length | color | gradient | stroke | tiling | dictionary, optional): The highlight's border color. See the rectangle's documentation for more details.

- `top-edge` (length | str, optional): The top end of the background rectangle.

- `bottom-edge` (length | str, optional): The bottom end of the background rectangle.

- `extent` (length, optional): The amount by which to extend the background to the sides beyond (or within if negative) the content.

- `radius` (relative | dictionary, optional): How much to round the highlight's corners. See the rectangle's documentation for more details.

- `body` (content, required): The content that should be highlighted.

## Examples

```typst
This is #highlight[important].
```

```typst
This is #highlight(
  fill: blue
)[highlighted with blue].
```

```typst
This is a #highlight(
  stroke: fuchsia
)[stroked highlighting].
```