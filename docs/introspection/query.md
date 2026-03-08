---
url: https://typst.app/docs/reference/introspection/query/
category: introspection
topic: query
---


# queryContextual (introspection)

Finds elements in the document.

## Signature

`query(labelselectorlocationfunction) -> array`

## Parameters

- `target` (label | selector | location | function, required): Can be

## Examples

```typst
#set page(numbering: "1")

#heading(outlined: false)[
  Table of Contents
]
#context {
  let chapters = query(
    heading.where(
      level: 1,
      outlined: true,
    )
  )
  for chapter in chapters {
    let loc = chapter.location()
    let nr = numbering(
      loc.page-numbering(),
      ..counter(page).at(loc),
    )
    [#chapter.body #h(1fr) #nr \ ]
  }
}

= Introduction
#lorem(10)
#pagebreak()

== Sub-Heading
#lorem(8)

= Discussion
#lorem(18)
```

```typst
= Real
#context {
  let elems = query(heading)
  let count = elems.len()
  count * [= Fake]
}
```