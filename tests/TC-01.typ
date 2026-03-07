// TC-01.typ — Basic Typst Syntax Test Case
// This file tests core Typst functionality

// == Test 1: Basic Text and Headings
= Test Document

This is a test document for typst-brain validation.

== Section 1: Text Formatting

*Bold text*, _italic text_, and `code inline`.

== Section 2: Lists

- Item 1
- Item 2
  - Nested item
- Item 3

Numbered list:
+ First
+ Second
+ Third

// == Test 3: Math
== Section 3: Mathematics

Inline math: $E = m c^2$

Block math:
$ integral_0^infinity e^(-x^2) dif x = sqrt(pi)/2 $

// == Test 4: Code Block
== Section 4: Code

```typst
#let greeting(name) = {
  "Hello, " + name + "!"
}

#greeting("World")
```

// == Test 5: Table
== Section 5: Tables

| Name | Value |
|------|-------|
| A    | 1     |
| B    | 2     |
| C    | 3     |

// == Test 6: Variables and Functions
#let x = 5
#let double(n) = n * 2

Result: #double(x)

// == Test 7: Conditionals
#if x > 3 [
  X is greater than 3
] else [
  X is not greater than 3
]

// == Test 8: Loops
#for i in range(3) [
  Item #i
]

// == Test 9: Figure
#figure(
  rect(width: 3cm, height: 2cm, fill: blue.lighten(50%)),
  caption: [A simple rectangle],
)

// == Test 10: References
@fig-demo shows a demo figure.

#figure(
  circle(radius: 1cm, fill: red.lighten(50%)),
  caption: [A demo circle],
) <fig-demo>

// End of test file
