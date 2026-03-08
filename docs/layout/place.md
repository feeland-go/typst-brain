---
url: https://typst.app/docs/reference/layout/place/
category: layout
topic: place
---


# place (layout)

Places content relatively to its parent container.

## Signature

`place(autoalignment, scope: str, float: bool, clearance: length, dx: relative, dy: relative, content) -> content`

## Parameters

- `alignment` (auto | alignment, optional): Relative to which position in the parent container to place the content.

- `scope` (str, optional): Relative to which containing scope something is placed.

- `float` (bool, optional): Whether the placed element has floating layout.

- `clearance` (length, optional): The spacing between the placed element and other elements in a floating layout.

- `dx` (relative, optional): The horizontal displacement of the placed content.

- `dy` (relative, optional): The vertical displacement of the placed content.

- `body` (content, required): The content to place.

## Examples

```typst
#set page(height: 120pt)
Hello, world!

#rect(
  width: 100%,
  height: 2cm,
  place(horizon + right, square()),
)

#place(
  top + left,
  dx: -5pt,
  square(size: 5pt, fill: red),
)
```

```typst
#let annotate(..args) = {
  box(place(..args))
  sym.wj
  h(0pt, weak: true)
}

A placed #annotate(square(), dy: 2pt)
square in my text.
```

```typst
#set page(height: 150pt, columns: 2)
#place(
  top + center,
  scope: "parent",
  float: true,
  rect(width: 80%, fill: aqua),
)

#lorem(25)
```