---
url: https://typst.app/docs/reference/model/ref/
category: model
topic: ref
---


# ref (model)

A reference to a label or bibliography.

## Signature

`ref(label, supplement: noneautocontentfunction, form: str) -> content`

## Parameters

- `target` (label, required): The target label that should be referenced.

- `supplement` (none | auto | content | function, optional): A supplement for the reference.

- `form` (str, optional): The kind of reference to produce.

## Examples

```typst
#set page(numbering: "1")
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

= Introduction <intro>
Recent developments in
typesetting software have
rekindled hope in previously
frustrated researchers. @distress
As shown in @results (see
#ref(<results>, form: "page")),
we ...

= Results <results>
We discuss our approach in
comparison with others.

== Performance <perf>
@slow demonstrates what slow
software looks like.
$ T(n) = O(2^n) $ <slow>

#bibliography("works.bib")
```

```typst
#set page(
  numbering: "1",
  supplement: "p.",
)
#set ref(form: "page")

#figure(
  stack(
    dir: ltr,
    spacing: 1em,
    circle(),
    square(),
  ),
  caption: [Shapes],
) <shapes>

#pagebreak()

See @shapes for examples
of different shapes.
```

```typst
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

#show ref: it => {
  let eq = math.equation
  let el = it.element
  // Skip all other references.
  if el == none or el.func() != eq { return it }
  // Override equation references.
  link(el.location(), numbering(
    el.numbering,
    ..counter(eq).at(el.location())
  ))
}

= Beginnings <beginning>
In @beginning we prove @pythagoras.
$ a^2 + b^2 = c^2 $ <pythagoras>
```