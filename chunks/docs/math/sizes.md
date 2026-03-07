---
url: https://typst.app/docs/reference/math/sizes/
category: math
topic: sizes
---


# Sizes (math)

Forced size styles for expressions within formulas.

## Signature

`math.display(content, cramped: bool) -> content body content Required Positional`

## Examples

```typst
$sum_i x_i/2 = display(sum_i x_i/2)$
```

```typst
$ sum_i x_i/2
    = inline(sum_i x_i/2) $
```

```typst
$sum_i x_i/2 = script(sum_i x_i/2)$
```