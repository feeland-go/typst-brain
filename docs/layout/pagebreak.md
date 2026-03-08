---
url: https://typst.app/docs/reference/layout/pagebreak/
category: layout
topic: pagebreak
---


# pagebreak (layout)

A manual page break.

## Signature

`pagebreak(weak: bool, to: nonestr) -> content`

## Parameters

- `weak` (bool, optional): If true, the page break is skipped if the current page is already empty.

- `to` (none | str, optional): If given, ensures that the next page will be an even/odd page, with an empty page in between if necessary.

## Examples

```typst
The next page contains
more details on compound theory.
#pagebreak()

== Compound Theory
In 1984, the first ...
```

```typst
#set page(height: 30pt)

First.
#pagebreak(to: "odd")
Third.
```