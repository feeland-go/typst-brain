---
url: https://typst.app/docs/reference/model/outline/
category: model
topic: outline
---


# outline (model)

A table of contents, figures, or other elements.

## Signature

`outline(title: noneautocontent, target: labelselectorlocationfunction, depth: noneint, indent: autorelativefunction) -> content`

## Parameters

- `title` (none | auto | content, optional): The title of the outline.

- `target` (label | selector | location | function, optional): The type of element to include in the outline.

- `depth` (none | int, optional): The maximum level up to which elements are included in the outline. When this argument is none, all elements are included.

- `indent` (auto | relative | function, optional): How to indent the outline's entries.

## Examples

```typst
#set heading(numbering: "1.")
#outline()

= Introduction
#lorem(5)

= Methods
== Setup
#lorem(10)
```

```typst
#outline(
  title: [List of Figures],
  target: figure.where(kind: image),
)

#figure(
  image("tiger.jpg"),
  caption: [A nice figure!],
)
```

```typst
#show outline.entry.where(
  level: 1
): set block(above: 1.2em)

#outline()

= About ACME Corp.
== History
=== Origins
= Products
== ACME Tools
```