---
url: https://typst.app/docs/reference/text/lower/
category: text
topic: lower
---


# lower (text)

Converts a string or content to lowercase.

## Signature

`lower(strcontent) -> strcontent`

## Parameters

- `text` (str | content, required): The text to convert to lowercase.

## Examples

```typst
#lower("ABC") \
#lower[*My Text*] \
#lower[already low]
```