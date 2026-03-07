---
url: https://typst.app/docs/reference/layout/colbreak/
category: layout
topic: colbreak
---


# colbreak (layout)

Forces a column break.

## Signature

`colbreak(weak: bool) -> content`

## Parameters

- `weak` (bool, optional): If true, the column break is skipped if the current column is already empty.

## Examples

```typst
#set page(columns: 2)
Preliminary findings from our
ongoing research project have
revealed a hitherto unknown
phenomenon of extraordinary
significance.

#colbreak()
Through rigorous experimentation
and analysis, we have discovered
a hitherto uncharacterized process
that defies our current
understanding of the fundamental
laws of nature.
```