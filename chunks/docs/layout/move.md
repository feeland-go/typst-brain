---
url: https://typst.app/docs/reference/layout/move/
category: layout
topic: move
---


# move (layout)

Moves content without affecting layout.

## Signature

`move(dx: relative, dy: relative, content) -> content`

## Parameters

- `dx` (relative, optional): The horizontal displacement of the content.

- `dy` (relative, optional): The vertical displacement of the content.

- `body` (content, required): The content to move.

## Examples

```typst
#rect(inset: 0pt, fill: gray, move(
  dx: 4pt, dy: 6pt,
  rect(
    inset: 8pt,
    fill: white,
    stroke: black,
    [Abra cadabra]
  )
))
```