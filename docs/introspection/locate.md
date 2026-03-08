---
url: https://typst.app/docs/reference/introspection/locate/
category: introspection
topic: locate
---


# locateContextual (introspection)

Determines the location of an element in the document.

## Signature

`locate(labelselectorlocationfunction) -> location`

## Parameters

- `selector` (label | selector | location | function, required): A selector that should match exactly one element. This element will be located.

## Examples

```typst
#context [
  Introduction is at: \
  #locate(<intro>).position()
]

= Introduction <intro>
```