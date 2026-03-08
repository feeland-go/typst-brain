---
url: https://typst.app/docs/reference/layout/repeat/
category: layout
topic: repeat
---


# repeat (layout)

Repeats content to the available space.

## Signature

`repeat(content, gap: length, justify: bool) -> content`

## Parameters

- `body` (content, required): The content to repeat.

- `gap` (length, optional): The gap between each instance of the body.

- `justify` (bool, optional): Whether to increase the gap between instances to completely fill the available space.

## Examples

```typst
Sign on the dotted line:
#box(width: 1fr, repeat[.])

#set text(10pt)
#v(8pt, weak: true)
#align(right)[
  Berlin, the 22nd of December, 2022
]
```