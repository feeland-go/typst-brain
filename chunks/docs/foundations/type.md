---
url: https://typst.app/docs/reference/foundations/type/
category: foundations
topic: type
---


# type (foundations)

Describes a kind of value.

## Signature

`type(any) -> type value any Required Positional`

## Examples

```typst
#let x = 10
#if type(x) == int [
  #x is an integer!
] else [
  #x is another value...
]

An image is of type
#type(image("glacier.jpg")).
```

```typst
#type(int) \
#type(type)
```

```typst
#let val = none
#if val == none [
  Yep, it's none.
]
```