---
url: https://typst.app/docs/reference/math/vec/
category: math
topic: vec
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Vector] 
  

# `vec`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A column vector.
 

Content in the vector's elements can be aligned with the [`align`] parameter, or the `&` symbol.
 

This function is for typesetting vector components. To typeset a symbol that represents a vector, [`arrow`] and [`bold`] are commonly used.
 

## Example 
```
$ vec(a, b, c) dot vec(1, 2, 3)
    = a + 2b + 3c $

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.vec([delim: ][none][str][array][symbol],[align: ][alignment],[gap: ][relative],[..][content],) -> [content]  

### `delim`   [none] or [str] or [array] or [symbol]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The delimiter to use.
 

Can be a single character specifying the left delimiter, in which case the right delimiter is inferred. Otherwise, can be an array containing a left and a right delimiter.
   View example   
```
#set math.vec(delim: "[")
$ vec(1, 2) $

```
   

 Default: `("(", ")")` 
 

### `align`   [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The horizontal alignment that each element should have.
   View example   
```
#set math.vec(align: right)
$ vec(-1, 1, -1) $

```
   

 Default: `center` 
 

### `gap`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The gap between elements.
   View example   
```
#set math.vec(gap: 1em)
$ vec(1, 2) $

```
   

 Default: `0% + 0.2em` 
 

### `children`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The elements of the vector.
 [VariantsPrevious page] [SymbolsNext page]