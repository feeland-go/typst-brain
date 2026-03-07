---
url: https://typst.app/docs/reference/layout/alignment/
category: layout
topic: alignment
---


# alignment (layout)

Where to align something along an axis.

## Signature

`self.axis() -> nonestr`

## Examples

```typst
#align(center)[Hi]
#align(alignment.center)[Hi]
```

```typst
#set page(height: 3cm)
#align(center + bottom)[Hi]
```

```typst
#(top + right).x \
#left.x \
#left.y (none)
```