---
url: https://typst.app/docs/reference/layout/columns/
category: layout
topic: columns
---


# columns (layout)

Separates a region into multiple equally sized columns.

## Signature

`columns(int, gutter: relative, content) -> content`

## Parameters

- `count` (int, optional): The number of columns.

- `gutter` (relative, optional): The size of the gutter space between each column.

- `body` (content, required): The content that should be layouted into the columns.

## Examples

```typst
#columns(2, gutter: 8pt)[
  This text is in the
  first column.

  #colbreak()

  This text is in the
  second column.
]
```

```typst
#set page(columns: 2, height: 150pt)

#place(
  top + center,
  scope: "parent",
  float: true,
  text(1.4em, weight: "bold")[
    My document
  ],
)

#lorem(40)
```