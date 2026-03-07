---
url: https://typst.app/docs/reference/math/underover/
category: math
topic: underover
---


# Under/Over (math)

Delimiters above or below parts of an equation.

## Signature

`math.underline(content) -> content body content Required Positional`

## Examples

```typst
$ underline(1 + 2 + ... + 5) $
```

```typst
$ overline(1 + 2 + ... + 5) $
```

```typst
$ underbrace(0 + 1 + dots.c + n, n + 1 "numbers") $
```