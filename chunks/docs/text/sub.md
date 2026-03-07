---
url: https://typst.app/docs/reference/text/sub/
category: text
topic: sub
---


# sub (text)

Renders text in subscript.

## Signature

`sub(typographic: bool, baseline: autolength, size: autolength, content) -> content`

## Parameters

- `typographic` (bool, optional): Whether to use subscript glyphs from the font if available.

- `baseline` (auto | length, optional): The downward baseline shift for synthesized subscripts.

- `size` (auto | length, optional): The font size for synthesized subscripts.

- `body` (content, required): The text to display in subscript.

## Examples

```typst
Revenue#sub[yearly]
```

```typst
N#sub(typographic: true)[1]
N#sub(typographic: false)[1]
```