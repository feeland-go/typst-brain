---
url: https://typst.app/docs/reference/foundations/float/
category: foundations
topic: float
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Float] 
  

#  float  

A floating-point number.
 

A limited-precision representation of a real number. Typst uses 64 bits to store floats. Wherever a float is expected, you can also pass an [integer].
 

You can convert a value to a float with this type's constructor.
 

NaN and positive infinity are available as `float.nan` and `float.inf` respectively.
 

## Example 
```
#3.14 \
#1e4 \
#(10 / 4)

```
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value to a float.
  Booleans are converted to `0.0` or `1.0`.
 Integers are converted to the closest 64-bit float. For integers with absolute value less than `calc.pow(2, 53)`, this conversion is exact.
 Ratios are divided by 100%.
 Strings are parsed in base 10 to the closest 64-bit float. Exponential notation is supported.
    View example  
```
#float(false) \
#float(true) \
#float(4) \
#float(40%) \
#float("2.7") \
#float("1e5")

```
   float([bool][int][float][ratio][str][decimal]) -> [float]  `value`   [bool] or [int] or [float] or [ratio] or [str] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that should be converted to a float.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `is-nan`

Checks if a float is not a number.
 

In IEEE 754, more than one bit pattern represents a NaN. This function returns `true` if the float is any of those bit patterns.
   View example  
```
#float.is-nan(0) \
#float.is-nan(1) \
#float.is-nan(float.nan)

```
   self.is-nan() -> [bool]  

### `is-infinite`

Checks if a float is infinite.
 

Floats can represent positive infinity and negative infinity. This function returns `true` if the float is an infinity.
   View example  
```
#float.is-infinite(0) \
#float.is-infinite(1) \
#float.is-infinite(float.inf)

```
   self.is-infinite() -> [bool]  

### `signum`

Calculates the sign of a floating point number.
  If the number is positive (including `+0.0`), returns `1.0`.
 If the number is negative (including `-0.0`), returns `-1.0`.
 If the number is NaN, returns `float.nan`.
    View example  
```
#(5.0).signum() \
#(-5.0).signum() \
#(0.0).signum() \
#float.nan.signum()

```
   self.signum() -> [float]  

### `from-bytes`

Interprets bytes as a float.
   View example  
```
#float.from-bytes(bytes((0, 0, 0, 0, 0, 0, 240, 63))) \
#float.from-bytes(bytes((63, 240, 0, 0, 0, 0, 0, 0)), endian: "big")

```
   float.from-bytes([bytes],[endian: ][str],) -> [float]  `bytes`   [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The bytes that should be converted to a float.
 

Must have a length of either 4 or 8. The bytes are then interpreted in [IEEE 754]'s binary32 (single-precision) or binary64 (double-precision) format depending on the length of the bytes.
 `endian`   [str]    

The endianness of the conversion.
 VariantDetails`"big"`

Big-endian byte order: The highest-value byte is at the beginning of the bytes.
`"little"`

Little-endian byte order: The lowest-value byte is at the beginning of the bytes.
 

 Default: `"little"` 
 

### `to-bytes`

Converts a float to bytes.
   View example  
```
#array(1.0.to-bytes(endian: "big")) \
#array(1.0.to-bytes())

```
   self.to-bytes([endian: ][str],[size: ][int],) -> [bytes]  `endian`   [str]    

The endianness of the conversion.
 VariantDetails`"big"`

Big-endian byte order: The highest-value byte is at the beginning of the bytes.
`"little"`

Little-endian byte order: The lowest-value byte is at the beginning of the bytes.
 

 Default: `"little"` 
 `size`   [int]    

The size of the resulting bytes.
 

This must be either 4 or 8. The call will return the representation of this float in either [IEEE 754]'s binary32 (single-precision) or binary64 (double-precision) format depending on the provided size.
 

 Default: `8` 
 [EvaluatePrevious page] [FunctionNext page]