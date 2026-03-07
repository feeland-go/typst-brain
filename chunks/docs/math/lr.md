---
url: https://typst.app/docs/reference/math/lr/
category: math
topic: lr
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Left/Right] 
  

# Left/Right 

Delimiter matching.
 

The `lr` function allows you to match two delimiters and scale them with the content they contain. While this also happens automatically for delimiters that match syntactically, `lr` allows you to match two arbitrary delimiters and control their size exactly. Apart from the `lr` function, Typst provides a few more functions that create delimiter pairings for absolute, ceiled, and floored values as well as norms.
 

To prevent a delimiter from being matched by Typst, and thus auto-scaled, escape it with a backslash. To instead disable auto-scaling completely, use `set math.lr(size: 1em)`.
 

## Example 
```
$ [a, b/2] $
$ lr(]sum_(x=1)^n], size: #50%) x $
$ abs((x + y) / 2) $
$ \{ (x / y) \} $
#set math.lr(size: 1em)
$ { (a / b), a, b in (0; 1/2] } $

```
 

## Functions 

### `lr`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Scales delimiters.
 

While matched delimiters scale by default, this can be used to scale unmatched delimiters and to control the delimiter scaling more precisely.
 math.lr([size: ][relative],[content],) -> [content]  `size`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The size of the brackets, relative to the height of the wrapped content.
 

 Default: `100% + 0pt` 
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The delimited content, including the delimiters.
 

### `mid`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Scales delimiters vertically to the nearest surrounding `lr()` group.
   View example  
```
$ { x mid(|) sum_(i=1)^n w_i|f_i (x)| < 1 } $

```
   math.mid([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to be scaled.
 

### `abs`

Takes the absolute value of an expression.
   View example  
```
$ abs(x/2) $

```
   math.abs([size: ][relative],[content],) -> [content]  `size`   [relative]    

The size of the brackets, relative to the height of the wrapped content.
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The expression to take the absolute value of.
 

### `norm`

Takes the norm of an expression.
   View example  
```
$ norm(x/2) $

```
   math.norm([size: ][relative],[content],) -> [content]  `size`   [relative]    

The size of the brackets, relative to the height of the wrapped content.
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The expression to take the norm of.
 

### `floor`

Floors an expression.
   View example  
```
$ floor(x/2) $

```
   math.floor([size: ][relative],[content],) -> [content]  `size`   [relative]    

The size of the brackets, relative to the height of the wrapped content.
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The expression to floor.
 

### `ceil`

Ceils an expression.
   View example  
```
$ ceil(x/2) $

```
   math.ceil([size: ][relative],[content],) -> [content]  `size`   [relative]    

The size of the brackets, relative to the height of the wrapped content.
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The expression to ceil.
 

### `round`

Rounds an expression.
   View example  
```
$ round(x/2) $

```
   math.round([size: ][relative],[content],) -> [content]  `size`   [relative]    

The size of the brackets, relative to the height of the wrapped content.
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The expression to round.
 [FractionPrevious page] [MatrixNext page]