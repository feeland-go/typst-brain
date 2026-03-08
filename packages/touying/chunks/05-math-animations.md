# Math Equation Animation

Touying supports animating parts of a math equation using `pause`.

```typst
== Math Equation Animation
Equation with `pause`:
$
  f(x) &= pause x^2 + 2x + 1 \\
       &= pause (x + 1)^2 \\
$

#meanwhile
Here, #pause we have the expression of $f(x)$.
#pause By factorizing, we can obtain this result.
```
