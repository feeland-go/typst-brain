---
url: https://typst.app/docs/reference/model/emph/
category: model
topic: emph
---


# emph (model)

Emphasizes content by toggling italics.

## Signature

`emph(content) -> content`

## Parameters

- `body` (content, required): The content to emphasize.

## Examples

```typst
This is _emphasized._ \
This is #emph[too.]

#show emph: it => {
  text(blue, it.body)
}

This is _emphasized_ differently.
```