---
url: https://typst.app/docs/reference/layout/rotate/
category: layout
topic: rotate
---


# rotate (layout)

Rotates content without affecting layout.

## Signature

`rotate(angle, origin: alignment, reflow: bool, content) -> content`

## Parameters

- `angle` (angle, optional): The amount of rotation.

- `origin` (alignment, optional): The origin of the rotation.

- `reflow` (bool, optional): Whether the rotation impacts the layout.

- `body` (content, required): The content to rotate.

## Examples

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  ..range(16)
    .map(i => rotate(24deg * i)[X]),
)
```

```typst
#rotate(-1.571rad)[Space!]
```

```typst
#set text(spacing: 8pt)
#let square = square.with(width: 8pt)

#box(square())
#box(rotate(30deg, origin: center, square()))
#box(rotate(30deg, origin: top + left, square()))
#box(rotate(30deg, origin: bottom + right, square()))
```