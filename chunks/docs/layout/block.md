---
url: https://typst.app/docs/reference/layout/block/
category: layout
topic: block
---


# block (layout)

A block-level container.

## Signature

`block(width: autorelative, height: autorelativefraction, breakable: bool, fill: nonecolorgradienttiling, stroke: nonelengthcolorgradientstroketilingdictionary, radius: relativedictionary, inset: relativedictionary, outset: relativedictionary, spacing: relativefraction, above: autorelativefraction, below: autorelativefraction, clip: bool, sticky: bool, nonecontent) -> content`

## Parameters

- `width` (auto | relative, optional): The block's width.

- `height` (auto | relative | fraction, optional): The block's height. When the height is larger than the remaining space on a page and breakable is true, the block will continue on the next page with the remaining height.

- `breakable` (bool, optional): Whether the block can be broken and continue on the next page.

- `fill` (none | color | gradient | tiling, optional): The block's background color. See the rectangle's documentation for more details.

- `stroke` (none | length | color | gradient | stroke | tiling | dictionary, optional): The block's border color. See the rectangle's documentation for more details.

- `radius` (relative | dictionary, optional): How much to round the block's corners. See the rectangle's documentation for more details.

- `inset` (relative | dictionary, optional): How much to pad the block's content. See the box's documentation for more details.

- `outset` (relative | dictionary, optional): How much to expand the block's size without affecting the layout. See the box's documentation for more details.

- `spacing` (relative | fraction, optional): The spacing around the block. When auto, inherits the paragraph spacing.

- `above` (auto | relative | fraction, optional): The spacing between this block and its predecessor.

- `below` (auto | relative | fraction, optional): The spacing between this block and its successor.

- `clip` (bool, optional): Whether to clip the content inside the block.

- `sticky` (bool, optional): Whether this block must stick to the following one, with no break in between.

- `body` (none | content, optional): The contents of the block.

## Examples

```typst
#set page(height: 100pt)
#block(
  fill: luma(230),
  inset: 8pt,
  radius: 4pt,
  lorem(30),
)
```

```typst
#show heading: it => it.body
= Blockless
More text.

#show heading: it => block(it.body)
= Blocky
More text.
```

```typst
#set align(center)
#block(
  width: 60%,
  inset: 8pt,
  fill: silver,
  lorem(10),
)
```