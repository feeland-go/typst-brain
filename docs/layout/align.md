---
url: https://typst.app/docs/reference/layout/align/
category: layout
topic: align
---


# align (layout)

Aligns content horizontally and vertically.

## Signature

`align(alignment, content) -> content`

## Parameters

- `alignment` (alignment, optional): The alignment along both axes.

- `body` (content, required): The content to align.

## Examples

```typst
#set page(height: 120pt)
#set align(center)

Centered text, a sight to see \
In perfect balance, visually \
Not left nor right, it stands alone \
A work of art, a visual throne
```

```typst
#set page(height: 120pt)
#set align(horizon)

Vertically centered, \
the stage had entered, \
a new paragraph.
```

```typst
#set page(height: 120pt)
Though left in the beginning ...

#align(right + bottom)[
  ... they were right in the end, \
  and with addition had gotten, \
  the paragraph to the bottom!
]
```