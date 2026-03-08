---
url: https://typst.app/docs/reference/foundations/int/
category: foundations
topic: int
---


# int (foundations)

A whole number.

## Signature

`int(boolintfloatstrdecimal) -> int value bool or int or float or str or decimal Required Positional`

## Examples

```typst
#(1 + 2) \
#(2 - 5) \
#(3 + 4 < 8)

#0xff \
#0o10 \
#0b1001
```

```typst
#int(false) \
#int(true) \
#int(2.7) \
#int(decimal("3.8")) \
#(int("27") + int("4"))
```

```typst
#(5).signum() \
#(-5).signum() \
#(0).signum()
```