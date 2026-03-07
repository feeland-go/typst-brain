---
url: https://typst.app/docs/reference/foundations/decimal/
category: foundations
topic: decimal
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Decimal] 
  

#  decimal  

A fixed-point decimal number type.
 

This type should be used for precise arithmetic operations on numbers represented in base 10. A typical use case is representing currency.
 

## Example 
```
Decimal: #(decimal("0.1") + decimal("0.2")) \
Float: #(0.1 + 0.2)

```
 

## Construction and casts 

To create a decimal number, use the `decimal(string)` constructor, such as in `decimal("3.141592653")` (note the double quotes!). This constructor preserves all given fractional digits, provided they are representable as per the limits specified below (otherwise, an error is raised).
 

You can also convert any [integer] to a decimal with the `decimal(int)` constructor, e.g. `decimal(59)`. However, note that constructing a decimal from a [floating-point number], while supported, is an imprecise conversion and therefore discouraged. A warning will be raised if Typst detects that there was an accidental `float` to `decimal` cast through its constructor, e.g. if writing `decimal(3.14)` (note the lack of double quotes, indicating this is an accidental `float` cast and therefore imprecise). It is recommended to use strings for constant decimal values instead (e.g. `decimal("3.14")`).
 

The precision of a `float` to `decimal` cast can be slightly improved by rounding the result to 15 digits with [`calc.round`], but there are still no precision guarantees for that kind of conversion.
 

## Operations 

Basic arithmetic operations are supported on two decimals and on pairs of decimals and integers.
 

Built-in operations between `float` and `decimal` are not supported in order to guard against accidental loss of precision. They will raise an error instead.
 

Certain `calc` functions, such as trigonometric functions and power between two real numbers, are also only supported for `float` (although raising `decimal` to integer exponents is supported). You can opt into potentially imprecise operations with the `float(decimal)` constructor, which casts the `decimal` number into a `float`, allowing for operations without precision guarantees.
 

## Displaying decimals 

To display a decimal, simply insert the value into the document. To only display a certain number of digits, [round] the decimal first. Localized formatting of decimals and other numbers is not yet supported, but planned for the future.
 

You can convert decimals to strings using the [`str`] constructor. This way, you can post-process the displayed representation, e.g. to replace the period with a comma (as a stand-in for proper built-in localization to languages that use the comma).
 

## Precision and limits 

A `decimal` number has a limit of 28 to 29 significant base-10 digits. This includes the sum of digits before and after the decimal point. As such, numbers with more fractional digits have a smaller range. The maximum and minimum `decimal` numbers have a value of `79228162514264337593543950335` and `-79228162514264337593543950335` respectively. In contrast with [`float`], this type does not support infinity or NaN, so overflowing or underflowing operations will raise an error.
 

Typical operations between `decimal` numbers, such as addition, multiplication, and [power] to an integer, will be highly precise due to their fixed-point representation. Note, however, that multiplication and division may not preserve all digits in some edge cases: while they are considered precise, digits past the limits specified above are rounded off and lost, so some loss of precision beyond the maximum representable digits is possible. Note that this behavior can be observed not only when dividing, but also when multiplying by numbers between 0 and 1, as both operations can push a number's fractional digits beyond the limits described above, leading to rounding. When those two operations do not surpass the digit limits, they are fully precise.
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value to a `decimal`.
 

It is recommended to use a string to construct the decimal number, or an [integer] (if desired). The string must contain a number in the format `"3.14159"` (or `"-3.141519"` for negative numbers). The fractional digits are fully preserved; if that's not possible due to the limit of significant digits (around 28 to 29) having been reached, an error is raised as the given decimal number wouldn't be representable.
 

While this constructor can be used with [floating-point numbers] to cast them to `decimal`, doing so is discouraged as this cast is inherently imprecise. It is easy to accidentally perform this cast by writing `decimal(1.234)` (note the lack of double quotes), which is why Typst will emit a warning in that case. Please write `decimal("1.234")` instead for that particular case (initialization of a constant decimal). Also note that floats that are NaN or infinite cannot be cast to decimals and will raise an error.
   View example  
```
#decimal("1.222222222222222")

```
   decimal([bool][int][float][str][decimal]) -> [decimal]  `value`   [bool] or [int] or [float] or [str] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that should be converted to a decimal.
 [DatetimePrevious page] [DictionaryNext page]