---
url: https://typst.app/docs/reference/model/heading/
category: model
topic: heading
---


# heading (model)

A section heading.

## Signature

`heading(level: autoint, depth: int, offset: int, numbering: nonestrfunction, supplement: noneautocontentfunction, outlined: bool, bookmarked: autobool, hanging-indent: autolength, content) -> content`

## Parameters

- `level` (auto | int, optional): The absolute nesting depth of the heading, starting from one. If set to auto, it is computed from offset + depth.

- `depth` (int, optional): The relative nesting depth of the heading, starting from one. This is combined with offset to compute the actual level.

- `offset` (int, optional): The starting offset of each heading's level, used to turn its relative depth into its absolute level.

- `numbering` (none | str | function, optional): How to number the heading. Accepts a numbering pattern or function taking multiple numbers.

- `supplement` (none | auto | content | function, optional): A supplement for the heading.

- `outlined` (bool, optional): Whether the heading should appear in the outline.

- `bookmarked` (auto | bool, optional): Whether the heading should appear as a bookmark in the exported PDF's outline. Doesn't affect other export formats, such as PNG.

- `hanging-indent` (auto | length, optional): The indent all but the first line of a heading should have.

- `body` (content, required): The heading's title.

## Examples

```typst
#set heading(numbering: "1.a)")

= Introduction
In recent years, ...

== Preliminaries
To start, ...
```

```typst
#show heading.where(level: 2): set text(red)

= Level 1
== Level 2

#set heading(offset: 1)
= Also level 2
== Level 3
```

```typst
= Level 1

#set heading(offset: 1, numbering: "1.1")
= Level 2

#heading(offset: 2, depth: 2)[
  I'm level 4
]
```