---
url: https://typst.app/docs/reference/math/accent/
category: math
topic: accent
---


# accent (math)

Attaches an accent to a base.

## Signature

`math.accent(content, strcontent, size: relative, dotless: bool) -> content`

## Parameters

- `base` (content, required): The base to which the accent is applied. May consist of multiple letters.

- `accent` (str | content, required): The accent to apply to the base.

- `size` (relative, optional): The size of the accent, relative to the width of the base.

- `dotless` (bool, optional): Whether to remove the dot on top of lowercase i and j when adding a top accent.

## Examples

```typst
$grave(a) = accent(a, `)$ \
$arrow(a) = accent(a, arrow)$ \
$tilde(a) = accent(a, \u{0303})$
```

```typst
$arrow(A B C)$
```

```typst
$dash(A, size: #150%)$
```