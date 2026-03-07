---
url: https://typst.app/docs/reference/foundations/label/
category: foundations
topic: label
---


# label (foundations)

A label for an element.

## Signature

`label(str) -> label name str Required Positional`

## Examples

```typst
#show <a>: set text(blue)
#show label("b"): set text(red)

= Heading <a>
*Strong* #label("b")
```