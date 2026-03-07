---
url: https://typst.app/docs/reference/math/lr/
category: math
topic: lr
---


# Left/Right (math)

Delimiter matching.

## Signature

`math.lr(size: relative, content) -> content size relative Settable`

## Examples

```typst
$ [a, b/2] $
$ lr(]sum_(x=1)^n], size: #50%) x $
$ abs((x + y) / 2) $
$ \{ (x / y) \} $
#set math.lr(size: 1em)
$ { (a / b), a, b in (0; 1/2] } $
```

```typst
$ { x mid(|) sum_(i=1)^n w_i|f_i (x)| < 1 } $
```

```typst
$ abs(x/2) $
```