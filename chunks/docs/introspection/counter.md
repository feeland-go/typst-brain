---
url: https://typst.app/docs/reference/introspection/counter/
category: introspection
topic: counter
---


# counter (introspection)

Counts through pages, elements, and more.

## Signature

`counter(strlabelselectorlocationfunction) -> counter key str or label or selector or location or function Required Positional`

## Examples

```typst
#set heading(numbering: "1.")

= Introduction
Raw value of heading counter is
#context counter(heading).get()
```

```typst
#set heading(numbering: "1.")

= Introduction
Some text here.

= Background
The current value is: #context {
  counter(heading).display()
}

Or in roman numerals: #context {
  counter(heading).display("I")
}
```

```typst
#set heading(numbering: "1.")

= Introduction
#counter(heading).step()

= Background
#counter(heading).update(3)
#counter(heading).update(n => n * 2)

= Analysis
Let's skip 7.1.
#counter(heading).step(level: 2)

== Analysis
Still at #context {
  counter(heading).display()
}
```