---
url: https://typst.app/docs/reference/foundations/function/
category: foundations
topic: function
---


# function (foundations)

A mapping from argument values to a return value.

## Signature

`self.with(..any) -> function arguments any Required Positional Variadic`

## Examples

```typst
// Call a function.
#list([A], [B])

// Named arguments and trailing
// content blocks.
#enum(start: 2)[A][B]

// Version without parentheses.
#list[A][B]
```

```typst
#let alert(body, fill: red) = {
  set text(white)
  set align(center)
  rect(
    fill: fill,
    inset: 8pt,
    radius: 4pt,
    [*Warning:\ #body*],
  )
}

#alert[
  Danger is imminent!
]

#alert(fill: blue)[
  KEEP OFF TRACKS
]
```

```typst
#show "once?": it => [#it #it]
once?
```