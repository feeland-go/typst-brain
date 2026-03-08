---
url: https://typst.app/docs/reference/layout/v/
category: layout
topic: v
---


# v (layout)

Inserts vertical spacing into a flow of blocks.

## Signature

`v(relativefraction, weak: bool) -> content`

## Parameters

- `amount` (relative | fraction, required): How much spacing to insert.

- `weak` (bool, optional): If true, the spacing collapses at the start or end of a flow. Moreover, from multiple adjacent weak spacings all but the largest one collapse. Weak spacings will always collapse adjacent paragraph spacing, even if the paragraph spacing is larger.

## Examples

```typst
#grid(
  rows: 3cm,
  columns: 6,
  gutter: 1fr,
  [A #parbreak() B],
  [A #v(0pt) B],
  [A #v(10pt) B],
  [A #v(0pt, weak: true) B],
  [A #v(40%, weak: true) B],
  [A #v(1fr) B],
)
```

```typst
The following theorem is
foundational to the field:
#v(4pt, weak: true)
$ x^2 + y^2 = r^2 $
#v(4pt, weak: true)
The proof is simple:
```