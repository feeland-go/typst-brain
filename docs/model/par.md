---
url: https://typst.app/docs/reference/model/par/
category: model
topic: par
---


# par (model)

A logical subdivison of textual content.

## Signature

`par(leading: length, spacing: length, justify: bool, justification-limits: dictionary, linebreaks: autostr, first-line-indent: lengthdictionary, hanging-indent: length, content) -> content`

## Parameters

- `leading` (length, optional): The spacing between lines.

- `spacing` (length, optional): The spacing between paragraphs.

- `justify` (bool, optional): Whether to justify text in its line.

- `justification-limits` (dictionary, optional): How much the spacing between words and characters may be adjusted during justification.

- `linebreaks` (auto | str, optional): How to determine line breaks.

- `first-line-indent` (length | dictionary, optional): The indent the first line of a paragraph should have.

- `hanging-indent` (length, optional): The indent that all but the first line of a paragraph should have.

- `body` (content, required): The contents of the paragraph.

## Examples

```typst
#set par(
  first-line-indent: 1em,
  spacing: 0.65em,
  justify: true,
)

We proceed by contradiction.
Suppose that there exists a set
of positive integers $a$, $b$, and
$c$ that satisfies the equation
$a^n + b^n = c^n$ for some
integer value of $n > 2$.

Without loss of generality,
let $a$ be the smallest of the
three integers. Then, we ...
```

```typst
#let example(name) = columns(2, gutter: 10pt)[
  #place(top, float: true, scope: "parent", strong(name))
  /* Text from https://en.wikipedia.org/wiki/Anne_Bayley */
]

#set page(width: 440pt, height: 21em, margin: 15pt)
#set par(justify: true)
#set text(size: 0.8em)

#grid(
  columns: (1fr, 1fr),
  gutter: 20pt,
  {
    // These are Typst's default limits.
    set par(justification-limits: (
      spacing: (min: 100% * 2 / 3, max: 150%),
      tracking: (min: 0em, max: 0em),
    ))
    example[Word-level justification]
  },
  {
    // These are our custom character-level limits.
    set par(justification-limits: (
      tracking: (min: -0.01em, max: 0.02em),
    ))
    example[Character-level justification]
  },
)
```

```typst
#set page(width: 207pt)
#set par(linebreaks: "simple")
Some texts feature many longer
words. Those are often exceedingly
challenging to break in a visually
pleasing way.

#set par(linebreaks: "optimized")
Some texts feature many longer
words. Those are often exceedingly
challenging to break in a visually
pleasing way.
```