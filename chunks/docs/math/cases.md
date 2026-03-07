---
url: https://typst.app/docs/reference/math/cases/
category: math
topic: cases
---


# cases (math)

A case distinction.

## Signature

`math.cases(delim: nonestrarraysymbol, reverse: bool, gap: relative, ..content) -> content`

## Parameters

- `delim` (none | str | array | symbol, optional): The delimiter to use.

- `reverse` (bool, optional): Whether the direction of cases should be reversed.

- `gap` (relative, optional): The gap between branches.

- `children` (content, required): The branches of the case distinction.

## Examples

```typst
$ f(x, y) := cases(
  1 "if" (x dot y)/2 <= 0,
  2 "if" x "is even",
  3 "if" x in NN,
  4 "else",
) $
```

```typst
#set math.cases(delim: "[")
$ x = cases(1, 2) $
```

```typst
#set math.cases(reverse: true)
$ cases(1, 2) = x $
```