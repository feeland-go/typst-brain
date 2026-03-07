---
url: https://typst.app/docs/reference/introspection/location/
category: introspection
topic: location
---


# location (introspection)

Identifies an element in the document.

## Signature

`self.page() -> int`

## Examples

```typst
#context [
  I am located on
  page #here().page()
]
```