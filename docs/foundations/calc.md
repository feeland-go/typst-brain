---
url: https://typst.app/docs/reference/foundations/calc/
category: foundations
topic: calc
---


# Calculation (foundations)

Module for calculations and processing of numeric values.

## Signature

`calc.abs(intfloatlengthangleratiofractiondecimal) -> any value int or float or length or angle or ratio or fraction or decimal Required Positional`

## Examples

```typst
#calc.abs(-5) \
#calc.abs(5pt - 2cm) \
#calc.abs(2fr) \
#calc.abs(decimal("-342.440"))
```

```typst
#calc.pow(2, 3) \
#calc.pow(decimal("2.5"), 2)
```

```typst
#calc.exp(1)
```