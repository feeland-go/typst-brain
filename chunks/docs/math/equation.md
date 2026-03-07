---
url: https://typst.app/docs/reference/math/equation/
category: math
topic: equation
---


# equation (math)

A mathematical equation.

## Signature

`math.equation(block: bool, numbering: nonestrfunction, number-align: alignment, supplement: noneautocontentfunction, alt: nonestr, content) -> content`

## Parameters

- `block` (bool, optional): Whether the equation is displayed as a separate block.

- `numbering` (none | str | function, optional): How to number block-level equations. Accepts a numbering pattern or function taking a single number.

- `number-align` (alignment, optional): The alignment of the equation numbering.

- `supplement` (none | auto | content | function, optional): A supplement for the equation.

- `alt` (none | str, optional): An alternative description of the mathematical equation.

- `body` (content, required): The contents of the equation.

## Examples

```typst
#set text(font: "New Computer Modern")

Let $a$, $b$, and $c$ be the side
lengths of right-angled triangle.
Then, we know that:
$ a^2 + b^2 = c^2 $

Prove by induction:
$ sum_(k=1)^n k = (n(n+1)) / 2 $
```

```typst
#set math.equation(numbering: "(1)")

We define:
$ phi.alt := (1 + sqrt(5)) / 2 $ <ratio>

With @ratio, we get:
$ F_n = floor(1 / sqrt(5) phi.alt^n) $
```

```typst
#set math.equation(numbering: "(1)", number-align: bottom)

We can calculate:
$ E &= sqrt(m_0^2 + p^2) \
    &approx 125 "GeV" $
```