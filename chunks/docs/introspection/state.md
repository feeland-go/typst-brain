---
url: https://typst.app/docs/reference/introspection/state/
category: introspection
topic: state
---


# state (introspection)

Manages stateful parts of your document.

## Signature

`state(str, any) -> state key str Required Positional`

## Examples

```typst
#set heading(numbering: "1.")
#let template(body) = [
  = Outline
  ...
  #body
]

#show: template

= Introduction
...
```

```typst
#let star = state("star", 0)
#let compute(expr) = {
  star.update(old =>
    eval(expr.replace("⭐", str(old)))
  )
  [New value is #context star.get().]
}

#compute("10") \
#compute("⭐ + 3") \
#compute("⭐ * 2") \
#compute("⭐ - 5")
```

```typst
...

#let more = [
  #compute("⭐ * 2") \
  #compute("⭐ - 5")
]

#compute("10") \
#compute("⭐ + 3") \
#more
```