---
url: https://typst.app/docs/reference/layout/skew/
category: layout
topic: skew
---


# skew (layout)

Skews content.

## Signature

`skew(ax: angle, ay: angle, origin: alignment, reflow: bool, content) -> content`

## Parameters

- `ax` (angle, optional): The horizontal skewing angle.

- `ay` (angle, optional): The vertical skewing angle.

- `origin` (alignment, optional): The origin of the skew transformation.

- `reflow` (bool, optional): Whether the skew transformation impacts the layout.

- `body` (content, required): The content to skew.

## Examples

```typst
#skew(ax: -12deg)[
  This is some fake italic text.
]
```

```typst
#skew(ax: 30deg)[Skewed]
```

```typst
#skew(ay: 30deg)[Skewed]
```