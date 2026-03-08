---
url: https://typst.app/docs/reference/text/overline/
category: text
topic: overline
---


# overline (text)

Adds a line over text.

## Signature

`overline(stroke: autolengthcolorgradientstroketilingdictionary, offset: autolength, extent: length, evade: bool, background: bool, content) -> content`

## Parameters

- `stroke` (auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the line.

- `offset` (auto | length, optional): The position of the line relative to the baseline. Read from the font tables if auto.

- `extent` (length, optional): The amount by which to extend the line beyond (or within if negative) the content.

- `evade` (bool, optional): Whether the line skips sections in which it would collide with the glyphs.

- `background` (bool, optional): Whether the line is placed behind the content it overlines.

- `body` (content, required): The content to add a line over.

## Examples

```typst
#overline[A line over text.]
```

```typst
#set text(fill: olive)
#overline(
  stroke: green.darken(20%),
  offset: -12pt,
  [The Forest Theme],
)
```

```typst
#overline(offset: -1.2em)[
  The Tale Of A Faraway Line II
]
```