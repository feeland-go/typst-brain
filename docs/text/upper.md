---
url: https://typst.app/docs/reference/text/upper/
category: text
topic: upper
---


# upper (text)

Converts a string or content to uppercase.

## Signature

`upper(strcontent) -> strcontent`

## Parameters

- `text` (str | content, required): The text to convert to uppercase.

## Examples

```typst
#upper("abc") \
#upper[*my text*] \
#upper[ALREADY HIGH]
```