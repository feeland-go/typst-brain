---
url: https://typst.app/docs/reference/foundations/float/
category: foundations
topic: float
---


# float (foundations)

A floating-point number.

## Signature

`float(boolintfloatratiostrdecimal) -> float value bool or int or float or ratio or str or decimal Required Positional`

## Examples

```typst
#3.14 \
#1e4 \
#(10 / 4)
```

```typst
#float(false) \
#float(true) \
#float(4) \
#float(40%) \
#float("2.7") \
#float("1e5")
```

```typst
#float.is-nan(0) \
#float.is-nan(1) \
#float.is-nan(float.nan)
```