---
url: https://typst.app/docs/reference/layout/direction/
category: layout
topic: direction
---


# direction (layout)

The four directions into which content can be laid out.

## Signature

`direction.from(alignment) -> direction side alignment Required Positional`

## Examples

```typst
#stack(dir: rtl)[A][B][C]
#stack(dir: direction.rtl)[A][B][C]
```

```typst
#direction.from(left) \
#direction.from(right) \
#direction.from(top) \
#direction.from(bottom)
```

```typst
#direction.to(left) \
#direction.to(right) \
#direction.to(top) \
#direction.to(bottom)
```