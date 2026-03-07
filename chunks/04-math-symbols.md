---
typst_min_version: "0.11"
typst_max_version: null
updated_at: "2025-03-07"
token_count: 700
see_also:
  - 01-syntax-scripting.md
---

# Math & Symbols

## Math Mode
```typst
$inline math$              // inline
$ block equation $         // display
$ x = 5 $                  // simple
$ x^2 + y_2 $              // superscript/subscript
```

## Equations
```typst
$ sum_(i=1)^n i = (n(n+1))/2 $
$ integral_0^oo e^(-x) dif x = 1 $
$ A := B iff C arrow.r D $
```

## Fractions & Roots
```typst
$ a/b $              // inline fraction
$ frac(a, b) $       // explicit
$ sqrt(x) $          // square root
$ root(n, x) $       // nth root
```

## Matrices
```typst
$ mat(1, 2; 3, 4) $           // 2x2 matrix
$ mat(1, 2, 3; 4, 5, 6) $     // 2x3 matrix
$ mat delim: "[", 1; 2 $      // brackets
$ cases(1, "if x > 0"; -1, "if x < 0") $
```

## Common Symbols
```typst
Greek: alpha beta gamma delta epsilon theta lambda mu pi sigma phi omega
Operators: sum prod integral arrow.r arrow.l arrow.l.r
Relations: = != < <= > >= in subset eq.tilde approx
Logic: forall exists not and or implies iff
Sets: union intersect setminus emptyset
Arrows: arrow arrow.r arrow.l arrow.t arrow.b
```

## Math Functions
```typst
$ sin(x), cos(x), tan(x) $
$ ln(x), log_10(x), exp(x) $
$ lim_(x -> 0) $
```

## Text in Math
```typst
$ x "if" y $         // quoted text
$ x = 5 "meters" $
$ f(x) := cases(
  1, "if" x > 0,
  0, "otherwise"
) $
```

## Alignment
```typst
$ x &= 5 \
  y &= 10 $
```

---
See also: [01-syntax-scripting](01-syntax-scripting.md)
