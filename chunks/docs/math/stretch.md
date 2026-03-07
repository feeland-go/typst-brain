---
url: https://typst.app/docs/reference/math/stretch/
category: math
topic: stretch
---


# stretch (math)

Stretches a glyph.

## Signature

`math.stretch(content, size: relative) -> content`

## Parameters

- `body` (content, required): The glyph to stretch.

- `size` (relative, optional): The size to stretch to, relative to the maximum size of the glyph and its attachments.

## Examples

```typst
$ H stretch(=)^"define" U + p V $
$ f : X stretch(->>, size: #150%)_"surjective" Y $
$ x stretch(harpoons.ltrb, size: #3em) y
    stretch(\[, size: #150%) z $
```