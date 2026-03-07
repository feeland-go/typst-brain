---
url: https://typst.app/docs/reference/foundations/decimal/
category: foundations
topic: decimal
---


# decimal (foundations)

A fixed-point decimal number type.

## Signature

`decimal(boolintfloatstrdecimal) -> decimal value bool or int or float or str or decimal Required Positional`

## Examples

```typst
Decimal: #(decimal("0.1") + decimal("0.2")) \
Float: #(0.1 + 0.2)
```

```typst
#decimal("1.222222222222222")
```