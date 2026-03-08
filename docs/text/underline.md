---
url: https://typst.app/docs/reference/text/underline/
category: text
topic: underline
---


# underline (text)

Underlines text.

## Signature

`underline(stroke: autolengthcolorgradientstroketilingdictionary, offset: autolength, extent: length, evade: bool, background: bool, content) -> content`

## Parameters

- `stroke` (auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the line.

- `offset` (auto | length, optional): The position of the line relative to the baseline, read from the font tables if auto.

- `extent` (length, optional): The amount by which to extend the line beyond (or within if negative) the content.

- `evade` (bool, optional): Whether the line skips sections in which it would collide with the glyphs.

- `background` (bool, optional): Whether the line is placed behind the content it underlines.

- `body` (content, required): The content to underline.

## Examples

```typst
This is #underline[important].
```

```typst
Take #underline(
  stroke: 1.5pt + red,
  offset: 2pt,
  [care],
)
```

```typst
#underline(offset: 5pt)[
  The Tale Of A Faraway Line I
]
```