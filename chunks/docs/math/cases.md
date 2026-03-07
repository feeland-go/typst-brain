---
url: https://typst.app/docs/reference/math/cases/
category: math
topic: cases
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Cases] 
  

# `cases`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A case distinction.
 

Content across different branches can be aligned with the `&` symbol.
 

## Example 
```
$ f(x, y) := cases(
  1 "if" (x dot y)/2 <= 0,
  2 "if" x "is even",
  3 "if" x in NN,
  4 "else",
) $

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.cases([delim: ][none][str][array][symbol],[reverse: ][bool],[gap: ][relative],[..][content],) -> [content]  

### `delim`   [none] or [str] or [array] or [symbol]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The delimiter to use.
 

Can be a single character specifying the left delimiter, in which case the right delimiter is inferred. Otherwise, can be an array containing a left and a right delimiter.
   View example   
```
#set math.cases(delim: "[")
$ x = cases(1, 2) $

```
   

 Default: `("{", "}")` 
 

### `reverse`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the direction of cases should be reversed.
   View example   
```
#set math.cases(reverse: true)
$ cases(1, 2) = x $

```
   

 Default: `false` 
 

### `gap`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The gap between branches.
   View example   
```
#set math.cases(gap: 1em)
$ x = cases(1, 2) $

```
   

 Default: `0% + 0.2em` 
 

### `children`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The branches of the case distinction.
 [CancelPrevious page] [ClassNext page]