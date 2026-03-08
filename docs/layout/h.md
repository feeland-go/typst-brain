---
url: https://typst.app/docs/reference/layout/h/
category: layout
topic: h
---


# h (layout)

Inserts horizontal spacing into a paragraph.

## Signature

`h(relativefraction, weak: bool) -> content`

## Parameters

- `amount` (relative | fraction, required): How much spacing to insert.

- `weak` (bool, optional): If true, the spacing collapses at the start or end of a paragraph. Moreover, from multiple adjacent weak spacings all but the largest one collapse.

## Examples

```typst
First #h(1cm) Second \
First #h(30%) Second
```

```typst
First #h(1fr) Second \
First #h(1fr) Second #h(1fr) Third \
First #h(2fr) Second #h(1fr) Third
```

```typst
#h(1cm, weak: true)
We identified a group of _weak_
specimens that fail to manifest
in most cases. However, when
#h(8pt, weak: true) supported
#h(8pt, weak: true) on both sides,
they do show up.

Further #h(0pt, weak: true) more,
even the smallest of them swallow
adjacent markup spaces.
```