---
url: https://typst.app/docs/reference/text/linebreak/
category: text
topic: linebreak
---


# linebreak (text)

Inserts a line break.

## Signature

`linebreak(justify: bool) -> content`

## Parameters

- `justify` (bool, optional): Whether to justify the line before the break.

## Examples

```typst
*Date:* 26.12.2022 \
*Topic:* Infrastructure Test \
*Severity:* High \
```

```typst
#set par(justify: true)
#let jb = linebreak(justify: true)

I have manually tuned the #jb
line breaks in this paragraph #jb
for an _interesting_ result. #jb
```