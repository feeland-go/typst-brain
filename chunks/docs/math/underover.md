---
url: https://typst.app/docs/reference/math/underover/
category: math
topic: underover
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Under/Over] 
  

# Under/Over 

Delimiters above or below parts of an equation.
 

The braces and brackets further allow you to add an optional annotation below or above themselves.
 

## Functions 

### `underline`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A horizontal line under content.
   View example  
```
$ underline(1 + 2 + ... + 5) $

```
   math.underline([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content above the line.
 

### `overline`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal line over content.
   View example  
```
$ overline(1 + 2 + ... + 5) $

```
   math.overline([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content below the line.
 

### `underbrace`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal brace under content, with an optional annotation below.
   View example  
```
$ underbrace(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.underbrace([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content above the brace.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content below the brace.
 

 Default: `none` 
 

### `overbrace`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal brace over content, with an optional annotation above.
   View example  
```
$ overbrace(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.overbrace([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content below the brace.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content above the brace.
 

 Default: `none` 
 

### `underbracket`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal bracket under content, with an optional annotation below.
   View example  
```
$ underbracket(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.underbracket([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content above the bracket.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content below the bracket.
 

 Default: `none` 
 

### `overbracket`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal bracket over content, with an optional annotation above.
   View example  
```
$ overbracket(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.overbracket([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content below the bracket.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content above the bracket.
 

 Default: `none` 
 

### `underparen`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal parenthesis under content, with an optional annotation below.
   View example  
```
$ underparen(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.underparen([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content above the parenthesis.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content below the parenthesis.
 

 Default: `none` 
 

### `overparen`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal parenthesis over content, with an optional annotation above.
   View example  
```
$ overparen(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.overparen([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content below the parenthesis.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content above the parenthesis.
 

 Default: `none` 
 

### `undershell`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal tortoise shell bracket under content, with an optional annotation below.
   View example  
```
$ undershell(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.undershell([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content above the tortoise shell bracket.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content below the tortoise shell bracket.
 

 Default: `none` 
 

### `overshell`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A horizontal tortoise shell bracket over content, with an optional annotation above.
   View example  
```
$ overshell(0 + 1 + dots.c + n, n + 1 "numbers") $

```
   math.overshell([content],[][none][content],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content below the tortoise shell bracket.
 `annotation`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The optional content above the tortoise shell bracket.
 

 Default: `none` 
 [Text OperatorPrevious page] [VariantsNext page]