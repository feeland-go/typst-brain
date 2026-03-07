---
url: https://typst.app/docs/reference/text/super/
category: text
topic: super
---


# super (text)

Renders text in superscript.

## Signature

`super(typographic: bool, baseline: autolength, size: autolength, content) -> content`

## Parameters

- `typographic` (bool, optional): Whether to use superscript glyphs from the font if available.

- `baseline` (auto | length, optional): The downward baseline shift for synthesized superscripts.

- `size` (auto | length, optional): The font size for synthesized superscripts.

- `body` (content, required): The text to display in superscript.

## Examples

```typst
1#super[st] try!
```

```typst
N#super(typographic: true)[1]
N#super(typographic: false)[1]
```