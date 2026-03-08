---
url: https://typst.app/docs/reference/math/attach/
category: math
topic: attach
---


# Attach (math)

Subscript, superscripts, and limits.

## Signature

`math.attach(content, t: nonecontent, b: nonecontent, tl: nonecontent, bl: nonecontent, tr: nonecontent, br: nonecontent) -> content base content Required Positional`

## Examples

```typst
$ sum_(i=0)^n a_i = 2^(1+i) $
```

```typst
$ attach(
  Pi, t: alpha, b: beta,
  tl: 1, tr: 2+3, bl: 4+5, br: 6,
) $
```

```typst
$ scripts(sum)_1^2 != sum_1^2 $
```