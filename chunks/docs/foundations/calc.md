---
url: https://typst.app/docs/reference/foundations/calc/
category: foundations
topic: calc
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Calculation] 
  

# Calculation 

Module for calculations and processing of numeric values.
 

These definitions are part of the `calc` module and not imported by default. In addition to the functions listed below, the `calc` module also defines the constants `pi`, `tau`, `e`, and `inf`.
 

## Functions 

### `abs`

Calculates the absolute value of a numeric value.
   View example  
```
#calc.abs(-5) \
#calc.abs(5pt - 2cm) \
#calc.abs(2fr) \
#calc.abs(decimal("-342.440"))

```
   calc.abs([int][float][length][angle][ratio][fraction][decimal]) -> any  `value`   [int] or [float] or [length] or [angle] or [ratio] or [fraction] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);    

The value whose absolute value to calculate.
 

### `pow`

Raises a value to some exponent.
   View example  
```
#calc.pow(2, 3) \
#calc.pow(decimal("2.5"), 2)

```
   calc.pow([int][float][decimal],[int][float],) -> [int][float][decimal]  `base`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The base of the power.
 

If this is a [`decimal`], the exponent can only be an [integer].
 `exponent`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The exponent of the power.
 

### `exp`

Raises a value to some exponent of e.
   View example  
```
#calc.exp(1)

```
   calc.exp([int][float]) -> [float]  `exponent`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The exponent of the power.
 

### `sqrt`

Calculates the square root of a number.
   View example  
```
#calc.sqrt(16) \
#calc.sqrt(2.5)

```
   calc.sqrt([int][float]) -> [float]  `value`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number whose square root to calculate. Must be non-negative.
 

### `root`

Calculates the real nth root of a number.
 

If the number is negative, then n must be odd.
   View example  
```
#calc.root(16.0, 4) \
#calc.root(27.0, 3)

```
   calc.root([float],[int],) -> [float]  `radicand`   [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The expression to take the root of.
 `index`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Which root of the radicand to take.
 

### `sin`

Calculates the sine of an angle.
 

When called with an integer or a float, they will be interpreted as radians.
   View example  
```
#calc.sin(1.5) \
#calc.sin(90deg)

```
   calc.sin([int][float][angle]) -> [float]  `angle`   [int] or [float] or [angle]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The angle whose sine to calculate.
 

### `cos`

Calculates the cosine of an angle.
 

When called with an integer or a float, they will be interpreted as radians.
   View example  
```
#calc.cos(1.5) \
#calc.cos(90deg)

```
   calc.cos([int][float][angle]) -> [float]  `angle`   [int] or [float] or [angle]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The angle whose cosine to calculate.
 

### `tan`

Calculates the tangent of an angle.
 

When called with an integer or a float, they will be interpreted as radians.
   View example  
```
#calc.tan(1.5) \
#calc.tan(90deg)

```
   calc.tan([int][float][angle]) -> [float]  `angle`   [int] or [float] or [angle]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The angle whose tangent to calculate.
 

### `asin`

Calculates the arcsine of a number.
   View example  
```
#calc.asin(0) \
#calc.asin(1)

```
   calc.asin([int][float]) -> [angle]  `value`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number whose arcsine to calculate. Must be between -1 and 1.
 

### `acos`

Calculates the arccosine of a number.
   View example  
```
#calc.acos(0) \
#calc.acos(1)

```
   calc.acos([int][float]) -> [angle]  `value`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number whose arccosine to calculate. Must be between -1 and 1.
 

### `atan`

Calculates the arctangent of a number.
   View example  
```
#calc.atan(0) \
#calc.atan(1)

```
   calc.atan([int][float]) -> [angle]  `value`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number whose arctangent to calculate.
 

### `atan2`

Calculates the four-quadrant arctangent of a coordinate.
 

The arguments are `(x, y)`, not `(y, x)`.
   View example  
```
#calc.atan2(1, 1) \
#calc.atan2(-2, -3)

```
   calc.atan2([int][float],[int][float],) -> [angle]  `x`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The X coordinate.
 `y`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The Y coordinate.
 

### `sinh`

Calculates the hyperbolic sine of a hyperbolic angle.
   View example  
```
#calc.sinh(0) \
#calc.sinh(1.5)

```
   calc.sinh([float]) -> [float]  `value`   [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The hyperbolic angle whose hyperbolic sine to calculate.
 

### `cosh`

Calculates the hyperbolic cosine of a hyperbolic angle.
   View example  
```
#calc.cosh(0) \
#calc.cosh(1.5)

```
   calc.cosh([float]) -> [float]  `value`   [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The hyperbolic angle whose hyperbolic cosine to calculate.
 

### `tanh`

Calculates the hyperbolic tangent of a hyperbolic angle.
   View example  
```
#calc.tanh(0) \
#calc.tanh(1.5)

```
   calc.tanh([float]) -> [float]  `value`   [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The hyperbolic angle whose hyperbolic tangent to calculate.
 

### `log`

Calculates the logarithm of a number.
 

If the base is not specified, the logarithm is calculated in base 10.
   View example  
```
#calc.log(100)

```
   calc.log([int][float],[base: ][float],) -> [float]  `value`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number whose logarithm to calculate. Must be strictly positive.
 `base`   [float]    

The base of the logarithm. May not be zero.
 

 Default: `10.0` 
 

### `ln`

Calculates the natural logarithm of a number.
   View example  
```
#calc.ln(calc.e)

```
   calc.ln([int][float]) -> [float]  `value`   [int] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number whose logarithm to calculate. Must be strictly positive.
 

### `fact`

Calculates the factorial of a number.
   View example  
```
#calc.fact(5)

```
   calc.fact([int]) -> [int]  `number`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number whose factorial to calculate. Must be non-negative.
 

### `perm`

Calculates a permutation.
 

Returns the `k`-permutation of `n`, or the number of ways to choose `k` items from a set of `n` with regard to order.
   View example  
```
$ "perm"(n, k) &= n!/((n - k)!) \
  "perm"(5, 3) &= #calc.perm(5, 3) $

```
   calc.perm([int],[int],) -> [int]  `base`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The base number. Must be non-negative.
 `numbers`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number of permutations. Must be non-negative.
 

### `binom`

Calculates a binomial coefficient.
 

Returns the `k`-combination of `n`, or the number of ways to choose `k` items from a set of `n` without regard to order.
   View example  
```
#calc.binom(10, 5)

```
   calc.binom([int],[int],) -> [int]  `n`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The upper coefficient. Must be non-negative.
 `k`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The lower coefficient. Must be non-negative.
 

### `gcd`

Calculates the greatest common divisor of two integers.
 

This will error if the result of integer division would be larger than the maximum 64-bit signed integer.
   View example  
```
#calc.gcd(7, 42)

```
   calc.gcd([int],[int],) -> [int]  `a`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The first integer.
 `b`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The second integer.
 

### `lcm`

Calculates the least common multiple of two integers.
   View example  
```
#calc.lcm(96, 13)

```
   calc.lcm([int],[int],) -> [int]  `a`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The first integer.
 `b`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The second integer.
 

### `floor`

Rounds a number down to the nearest integer.
 

If the number is already an integer, it is returned unchanged.
 

Note that this function will always return an [integer], and will error if the resulting [`float`] or [`decimal`] is larger than the maximum 64-bit signed integer or smaller than the minimum for that type.
   View example  
```
#calc.floor(500.1)
#assert(calc.floor(3) == 3)
#assert(calc.floor(3.14) == 3)
#assert(calc.floor(decimal("-3.14")) == -4)

```
   calc.floor([int][float][decimal]) -> [int]  `value`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to round down.
 

### `ceil`

Rounds a number up to the nearest integer.
 

If the number is already an integer, it is returned unchanged.
 

Note that this function will always return an [integer], and will error if the resulting [`float`] or [`decimal`] is larger than the maximum 64-bit signed integer or smaller than the minimum for that type.
   View example  
```
#calc.ceil(500.1)
#assert(calc.ceil(3) == 3)
#assert(calc.ceil(3.14) == 4)
#assert(calc.ceil(decimal("-3.14")) == -3)

```
   calc.ceil([int][float][decimal]) -> [int]  `value`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to round up.
 

### `trunc`

Returns the integer part of a number.
 

If the number is already an integer, it is returned unchanged.
 

Note that this function will always return an [integer], and will error if the resulting [`float`] or [`decimal`] is larger than the maximum 64-bit signed integer or smaller than the minimum for that type.
   View example  
```
#calc.trunc(15.9)
#assert(calc.trunc(3) == 3)
#assert(calc.trunc(-3.7) == -3)
#assert(calc.trunc(decimal("8493.12949582390")) == 8493)

```
   calc.trunc([int][float][decimal]) -> [int]  `value`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to truncate.
 

### `fract`

Returns the fractional part of a number.
 

If the number is an integer, returns `0`.
   View example  
```
#calc.fract(-3.1)
#assert(calc.fract(3) == 0)
#assert(calc.fract(decimal("234.23949211")) == decimal("0.23949211"))

```
   calc.fract([int][float][decimal]) -> [int][float][decimal]  `value`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to truncate.
 

### `round`

Rounds a number to the nearest integer.
 

Half-integers are rounded away from zero.
 

Optionally, a number of decimal places can be specified. If negative, its absolute value will indicate the amount of significant integer digits to remove before the decimal point.
 

Note that this function will return the same type as the operand. That is, applying `round` to a [`float`] will return a `float`, and to a [`decimal`], another `decimal`. You may explicitly convert the output of this function to an integer with [`int`], but note that such a conversion will error if the `float` or `decimal` is larger than the maximum 64-bit signed integer or smaller than the minimum integer.
 

In addition, this function can error if there is an attempt to round beyond the maximum or minimum integer or `decimal`. If the number is a `float`, such an attempt will cause `float.inf` or `-float.inf` to be returned for maximum and minimum respectively.
   View example  
```
#calc.round(3.1415, digits: 2)
#assert(calc.round(3) == 3)
#assert(calc.round(3.14) == 3)
#assert(calc.round(3.5) == 4.0)
#assert(calc.round(3333.45, digits: -2) == 3300.0)
#assert(calc.round(-48953.45, digits: -3) == -49000.0)
#assert(calc.round(3333, digits: -2) == 3300)
#assert(calc.round(-48953, digits: -3) == -49000)
#assert(calc.round(decimal("-6.5")) == decimal("-7"))
#assert(calc.round(decimal("7.123456789"), digits: 6) == decimal("7.123457"))
#assert(calc.round(decimal("3333.45"), digits: -2) == decimal("3300"))
#assert(calc.round(decimal("-48953.45"), digits: -3) == decimal("-49000"))

```
   calc.round([int][float][decimal],[digits: ][int],) -> [int][float][decimal]  `value`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to round.
 `digits`   [int]    

If positive, the number of decimal places.
 

If negative, the number of significant integer digits that should be removed before the decimal point.
 

 Default: `0` 
 

### `clamp`

Clamps a number between a minimum and maximum value.
   View example  
```
#calc.clamp(5, 0, 4)
#assert(calc.clamp(5, 0, 10) == 5)
#assert(calc.clamp(5, 6, 10) == 6)
#assert(calc.clamp(decimal("5.45"), 2, decimal("45.9")) == decimal("5.45"))
#assert(calc.clamp(decimal("5.45"), decimal("6.75"), 12) == decimal("6.75"))

```
   calc.clamp([int][float][decimal],[int][float][decimal],[int][float][decimal],) -> [int][float][decimal]  `value`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to clamp.
 `min`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The inclusive minimum value.
 `max`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The inclusive maximum value.
 

### `min`

Determines the minimum of a sequence of values.
   View example  
```
#calc.min(1, -3, -5, 20, 3, 6) \
#calc.min("typst", "is", "cool")

```
   calc.min([..]any) -> any  `values`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The sequence of values from which to extract the minimum. Must not be empty.
 

### `max`

Determines the maximum of a sequence of values.
   View example  
```
#calc.max(1, -3, -5, 20, 3, 6) \
#calc.max("typst", "is", "cool")

```
   calc.max([..]any) -> any  `values`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The sequence of values from which to extract the maximum. Must not be empty.
 

### `even`

Determines whether an integer is even.
   View example  
```
#calc.even(4) \
#calc.even(5) \
#range(10).filter(calc.even)

```
   calc.even([int]) -> [bool]  `value`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to check for evenness.
 

### `odd`

Determines whether an integer is odd.
   View example  
```
#calc.odd(4) \
#calc.odd(5) \
#range(10).filter(calc.odd)

```
   calc.odd([int]) -> [bool]  `value`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The number to check for oddness.
 

### `rem`

Calculates the remainder of two numbers.
 

The value `calc.rem(x, y)` always has the same sign as `x`, and is smaller in magnitude than `y`.
 

This can error if given a [`decimal`] input and the dividend is too small in magnitude compared to the divisor.
   View example  
```
#calc.rem(7, 3) \
#calc.rem(7, -3) \
#calc.rem(-7, 3) \
#calc.rem(-7, -3) \
#calc.rem(1.75, 0.5)

```
   calc.rem([int][float][decimal],[int][float][decimal],) -> [int][float][decimal]  `dividend`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The dividend of the remainder.
 `divisor`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The divisor of the remainder.
 

### `div-euclid`

Performs euclidean division of two numbers.
 

The result of this computation is that of a division rounded to the integer `n` such that the dividend is greater than or equal to `n` times the divisor.
 

This can error if the resulting number is larger than the maximum value or smaller than the minimum value for its type.
   View example  
```
#calc.div-euclid(7, 3) \
#calc.div-euclid(7, -3) \
#calc.div-euclid(-7, 3) \
#calc.div-euclid(-7, -3) \
#calc.div-euclid(1.75, 0.5) \
#calc.div-euclid(decimal("1.75"), decimal("0.5"))

```
   calc.div-euclid([int][float][decimal],[int][float][decimal],) -> [int][float][decimal]  `dividend`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The dividend of the division.
 `divisor`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The divisor of the division.
 

### `rem-euclid`

This calculates the least nonnegative remainder of a division.
 

Warning: Due to a floating point round-off error, the remainder may equal the absolute value of the divisor if the dividend is much smaller in magnitude than the divisor and the dividend is negative. This only applies for floating point inputs.
 

In addition, this can error if given a [`decimal`] input and the dividend is too small in magnitude compared to the divisor.
   View example  
```
#calc.rem-euclid(7, 3) \
#calc.rem-euclid(7, -3) \
#calc.rem-euclid(-7, 3) \
#calc.rem-euclid(-7, -3) \
#calc.rem-euclid(1.75, 0.5) \
#calc.rem-euclid(decimal("1.75"), decimal("0.5"))

```
   calc.rem-euclid([int][float][decimal],[int][float][decimal],) -> [int][float][decimal]  `dividend`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The dividend of the remainder.
 `divisor`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The divisor of the remainder.
 

### `quo`

Calculates the quotient (floored division) of two numbers.
 

Note that this function will always return an [integer], and will error if the resulting number is larger than the maximum 64-bit signed integer or smaller than the minimum for that type.
   View example  
```
$ "quo"(a, b) &= floor(a/b) \
  "quo"(14, 5) &= #calc.quo(14, 5) \
  "quo"(3.46, 0.5) &= #calc.quo(3.46, 0.5) $

```
   calc.quo([int][float][decimal],[int][float][decimal],) -> [int]  `dividend`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The dividend of the quotient.
 `divisor`   [int] or [float] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The divisor of the quotient.
 

### `norm`

Calculates the p-norm of a sequence of values.
   View example  
```
#calc.norm(1, 2, -3, 0.5) \
#calc.norm(p: 3, 1, 2)

```
   calc.norm([p: ][float],[..][float],) -> [float]  `p`   [float]    

The p value to calculate the p-norm of.
 

 Default: `2.0` 
 `values`   [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The sequence of values from which to calculate the p-norm. Returns `0.0` if empty.
 [BytesPrevious page] [ContentNext page]