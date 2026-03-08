---
url: https://typst.app/docs/reference/foundations/arguments/
category: foundations
topic: arguments
---


# arguments (foundations)

Captured arguments to a function.

## Signature

`arguments(..any) -> arguments arguments any Required Positional Variadic`

## Examples

```typst
#let format(title, ..authors) = {
  let by = authors
    .pos()
    .join(", ", last: " and ")

  [*#title* \ _Written by #by;_]
}

#format("ArtosFlow", "Jane", "Joe")
```

```typst
#let array = (2, 3, 5)
#calc.min(..array)
#let dict = (fill: blue)
#text(..dict)[Hello]
```

```typst
#let args = arguments(stroke: red, inset: 1em, [Body])
#box(..args)
```