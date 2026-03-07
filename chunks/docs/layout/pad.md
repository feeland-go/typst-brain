---
url: https://typst.app/docs/reference/layout/pad/
category: layout
topic: pad
---


# pad (layout)

Adds spacing around content.

## Signature

`pad(left: relative, top: relative, right: relative, bottom: relative, x: relative, y: relative, rest: relative, content) -> content`

## Parameters

- `left` (relative, optional): The padding at the left side.

- `top` (relative, optional): The padding at the top side.

- `right` (relative, optional): The padding at the right side.

- `bottom` (relative, optional): The padding at the bottom side.

- `x` (relative, optional): A shorthand to set left and right to the same value.

- `y` (relative, optional): A shorthand to set top and bottom to the same value.

- `rest` (relative, optional): A shorthand to set all four sides to the same value.

- `body` (content, required): The content to pad at the sides.

## Examples

```typst
#set align(center)

#pad(x: 16pt, image("typing.jpg"))
_Typing speeds can be
 measured in words per minute._
```