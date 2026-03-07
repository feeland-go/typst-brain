---
url: https://typst.app/docs/reference/text/lorem/
category: text
topic: lorem
---


# lorem (text)

Creates blind text.

## Signature

`lorem(int) -> str`

## Parameters

- `words` (int, required): The length of the blind text in words.

## Examples

```typst
= Blind Text
#lorem(30)

= More Blind Text
#lorem(15)
```