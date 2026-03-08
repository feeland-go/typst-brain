---
url: https://typst.app/docs/reference/math/class/
category: math
topic: class
---


# class (math)

Forced use of a certain math class.

## Signature

`math.class(str, content) -> content`

## Parameters

- `class` (str, required): The class to apply to the content.

- `body` (content, required): The content to which the class is applied.

## Examples

```typst
#let loves = math.class(
  "relation",
  sym.suit.heart,
)

$x loves y and y loves 5$
```