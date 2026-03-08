---
url: https://typst.app/docs/reference/foundations/symbol/
category: foundations
topic: symbol
---


# symbol (foundations)

A Unicode symbol.

## Signature

`symbol(..strarray) -> symbol variants str or array Required Positional Variadic`

## Examples

```typst
#sym.arrow.r \
#sym.gt.eq.not \
$gt.eq.not$ \
#emoji.face.halo
```

```typst
$arrow.l$ \
$arrow.r$ \
$arrow.t.quad$
```

```typst
#let envelope = symbol(
  "🖂",
  ("stamped", "🖃"),
  ("stamped.pen", "🖆"),
  ("lightning", "🖄"),
  ("fly", "🖅"),
)

#envelope
#envelope.stamped
#envelope.stamped.pen
#envelope.lightning
#envelope.fly
```