---
url: https://typst.app/docs/reference/math/frac/
category: math
topic: frac
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Fraction] 
  

# `frac`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A mathematical fraction.
 

## Example 
```
$ 1/2 < (x+1)/2 $
$ ((x+1)) / 2 = frac(a, b) $

```
 

## Syntax 

This function also has dedicated syntax: Use a slash to turn neighbouring expressions into a fraction. Multiple atoms can be grouped into a single expression using round grouping parentheses. Such parentheses are removed from the output, but you can nest multiple to force them.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.frac([content],[content],[style: ][str],) -> [content]  

### `num`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The fraction's numerator.
 

### `denom`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The fraction's denominator.
 

### `style`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How the fraction should be laid out.
   View example: Styles   
```
$ frac(x, y, style: "vertical") $
$ frac(x, y, style: "skewed") $
$ frac(x, y, style: "horizontal") $

```
      View example: Setting the default   
```
#set math.frac(style: "skewed")
$ a / b $

```
      View example: Handling of grouping parentheses   
```
// Grouping parentheses are removed.
#set math.frac(style: "vertical")
$ (a + b) / b $

// Grouping parentheses are removed.
#set math.frac(style: "skewed")
$ (a + b) / b $

// Grouping parentheses are retained.
#set math.frac(style: "horizontal")
$ (a + b) / b $

```
      View example: Different styles in inline vs block equations   
```
// This changes the style for inline equations only.
#show math.equation.where(block: false): set math.frac(style: "horizontal")

This $(x-y)/z = 3$ is inline math, and this is block math:
$ (x-y)/z = 3 $

```
   VariantDetails`"vertical"`

Stacked numerator and denominator with a bar.
`"skewed"`

Numerator and denominator separated by a slash.
`"horizontal"`

Numerator and denominator placed inline and parentheses are not absorbed.
 

 Default: `"vertical"` 
 [EquationPrevious page] [Left/RightNext page]