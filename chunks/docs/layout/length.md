---
url: https://typst.app/docs/reference/layout/length/
category: layout
topic: length
---


# length (layout)

A size or distance, possibly expressed with contextual units.

## Signature

`self.pt() -> float`

## Examples

```typst
#rect(width: 20pt)
#rect(width: 2em)
#rect(width: 1in)

#(3em + 5pt).em \
#(20pt).em \
#(40em + 2pt).abs \
#(5em).abs
```

```typst
#set text(size: 12pt)
#context [
  #(6pt).to-absolute() \
  #(6pt + 10em).to-absolute() \
  #(10em).to-absolute()
]

#set text(size: 6pt)
#context [
  #(6pt).to-absolute() \
  #(6pt + 10em).to-absolute() \
  #(10em).to-absolute()
]
```