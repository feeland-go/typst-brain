---
url: https://typst.app/docs/reference/foundations/bytes/
category: foundations
topic: bytes
---


# bytes (foundations)

A sequence of bytes.

## Signature

`bytes(strbytesarray) -> bytes value str or bytes or array Required Positional`

## Examples

```typst
#bytes((123, 160, 22, 0)) \
#bytes("Hello 😃")

#let data = read(
  "rhino.png",
  encoding: none,
)

// Magic bytes.
#array(data.slice(0, 4)) \
#str(data.slice(1, 4))
```

```typst
#bytes("Hello 😃") \
#bytes((123, 160, 22, 0))
```