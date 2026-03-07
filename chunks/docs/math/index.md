---
url: https://typst.app/docs/reference/math/
category: math
topic: index
---


# Math (math)

Typst has special syntax and library functions to typeset mathematical formulas. Math formulas can be displayed inline with text or as separate blocks. They will be typeset into their own block if they start and end with at least one space (e.g. $ x^2 $).

## Examples

```typst
$ A = pi r^2 $
$ "area" = pi dot "radius"^2 $
$ cal(A) :=
    { x in RR | x "is natural" } $
#let x = 5
$ #x < 17 $
```

```typst
$ x < y => x gt.eq.not y $
```

```typst
$ sum_(k=0)^n k
    &= 1 + ... + n \
    &= (n(n+1)) / 2 $
```

## Overview

Reference Math Math Typst has special syntax and library functions to typeset mathematical formulas. Math formulas can be displayed inline with text or as separate blocks. They will be typeset into their own block if they start and end with at least one space (e.g. $ x^2 $). Variables In math, single letters are always displayed as is. Multiple letters, however, are interpreted as variables and functions. To display multiple letters verbatim, you can place them into quotes and to access single letter variables, you can use the hash syntax. $ A = pi r^2 $ $ "area" = pi dot "radius"^2 $ $ cal(A) := { x in RR | x "is natural" } $ #let x = 5 $ #x < 17 $ Symbols Math mode makes a wide selection of symbols like pi, dot, or RR available. Many mathematical symbols are available in different variants. You can select between different variants by applying modifiers to the symbol. Typst further recognizes a number of shorthand sequences like => that approximate a symbol. When such a shorthand exists, the symbol's documentation lists it. $ x < y => x gt.eq.not y $ Line Breaks Formulas can also contain line breaks. Each line can contain one or multiple alignment points (&) which are then aligned. $ sum_(k=0)^n k &= 1 + ... + n \ &= (n(n+1)) / 2 $ Function calls Math mode supports special function calls without the hash prefix. In these "math calls", the argument list works a little differently than in code: Within them, Typst is still in "math mode". Thus, you can write math directly into them, but need to use hash syntax to pass code expressions (except for strings, which are available in the math syntax). They support positional and named arguments, as well as argument spreading. They don't support trailing content blocks. They provide additional syntax for 2-dimensional argument lists. The semicolon (;) merges preceding arguments separated by commas into an array argument. $ frac(a^2, 2) $ $ vec(1, 2, delim: "[") $ $ mat(1, 2; 3, 4) $ $ mat(..#range(1, 5).chunks(2)) $ $ lim_x...