---
url: https://typst.app/docs/reference/math/frac/
category: math
topic: frac
---


# frac (math)

A mathematical fraction.

## Signature

`math.frac(content, content, style: str) -> content`

## Parameters

- `num` (content, required): The fraction's numerator.

- `denom` (content, required): The fraction's denominator.

- `style` (str, optional): How the fraction should be laid out.

## Examples

```typst
$ 1/2 < (x+1)/2 $
$ ((x+1)) / 2 = frac(a, b) $
```

```typst
$ frac(x, y, style: "vertical") $
$ frac(x, y, style: "skewed") $
$ frac(x, y, style: "horizontal") $
```

```typst
#set math.frac(style: "skewed")
$ a / b $
```