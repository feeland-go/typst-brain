---
url: https://typst.app/docs/reference/math/vec/
category: math
topic: vec
---


# vec (math)

A column vector.

## Signature

`math.vec(delim: nonestrarraysymbol, align: alignment, gap: relative, ..content) -> content`

## Parameters

- `delim` (none | str | array | symbol, optional): The delimiter to use.

- `align` (alignment, optional): The horizontal alignment that each element should have.

- `gap` (relative, optional): The gap between elements.

- `children` (content, required): The elements of the vector.

## Examples

```typst
$ vec(a, b, c) dot vec(1, 2, 3)
    = a + 2b + 3c $
```

```typst
#set math.vec(delim: "[")
$ vec(1, 2) $
```

```typst
#set math.vec(align: right)
$ vec(-1, 1, -1) $
```