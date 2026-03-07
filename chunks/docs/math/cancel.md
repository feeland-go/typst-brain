---
url: https://typst.app/docs/reference/math/cancel/
category: math
topic: cancel
---


# cancel (math)

Displays a diagonal line over a part of an equation.

## Signature

`math.cancel(content, length: relative, inverted: bool, cross: bool, angle: autoanglefunction, stroke: lengthcolorgradientstroketilingdictionary) -> content`

## Parameters

- `body` (content, required): The content over which the line should be placed.

- `length` (relative, optional): The length of the line, relative to the length of the diagonal spanning the whole element being "cancelled". A value of 100% would then have the line span precisely the element's diagonal.

- `inverted` (bool, optional): Whether the cancel line should be inverted (flipped along the y-axis). For the default angle setting, inverted means the cancel line points to the top left instead of top right.

- `cross` (bool, optional): Whether two opposing cancel lines should be drawn, forming a cross over the element. Overrides inverted.

- `angle` (auto | angle | function, optional): How much to rotate the cancel line.

- `stroke` (length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the cancel line.

## Examples

```typst
Here, we can simplify:
$ (a dot b dot cancel(x)) /
    cancel(x) $
```

```typst
$ a + cancel(x, length: #200%)
    - cancel(x, length: #200%) $
```

```typst
$ (a cancel((b + c), inverted: #true)) /
    cancel(b + c, inverted: #true) $
```