---
url: https://typst.app/docs/reference/foundations/array/
category: foundations
topic: array
---


# array (foundations)

A sequence of values.

## Signature

`array(bytesarrayversion) -> array value bytes or array or version Required Positional`

## Examples

```typst
#let values = (1, 7, 4, -3, 2)

#values.at(0) \
#(values.at(0) = 3)
#values.at(-1) \
#values.find(calc.even) \
#values.filter(calc.odd) \
#values.map(calc.abs) \
#values.rev() \
#(1, (2, 3)).flatten() \
#(("A", "B", "C")
    .join(", ", last: " and "))
```

```typst
#let hi = "Hello 😃"
#array(bytes(hi))
```

```typst
#range(5) \
#range(2, 5) \
#range(20, step: 4) \
#range(21, step: 4) \
#range(5, 2, step: -1)
```