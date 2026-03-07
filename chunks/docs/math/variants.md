---
url: https://typst.app/docs/reference/math/variants/
category: math
topic: variants
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Variants] 
  

# Variants 

Alternate typefaces within formulas.
 

These functions are distinct from the [`text`] function because math fonts contain multiple variants of each letter.
 

## Functions 

### `serif`

Serif (roman) font style in math.
 

This is already the default.
 math.serif([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);    

The content to style.
 

### `sans`

Sans-serif font style in math.
   View example  
```
$ sans(A B C) $

```
   math.sans([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to style.
 

### `frak`

Fraktur font style in math.
   View example  
```
$ frak(P) $

```
   math.frak([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to style.
 

### `mono`

Monospace font style in math.
   View example  
```
$ mono(x + y = z) $

```
   math.mono([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to style.
 

### `bb`

Blackboard bold (double-struck) font style in math.
 

For uppercase latin letters, blackboard bold is additionally available through [symbols] of the form `NN` and `RR`.
   View example  
```
$ bb(b) $
$ bb(N) = NN $
$ f: NN -> RR $

```
   math.bb([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to style.
 

### `cal`

Calligraphic (chancery) font style in math.
   View example  
```
Let $cal(P)$ be the set of ...

```
  

This is the default calligraphic/script style for most math fonts. See [`scr`] for more on how to get the other style (roundhand).
 math.cal([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to style.
 

### `scr`

Script (roundhand) font style in math.
   View example  
```
$scr(L)$ is not the set of linear
maps $cal(L)$.

```
  

There are two ways that fonts can support differentiating `cal` and `scr`. The first is using Unicode variation sequences. This works out of the box in Typst, however only a few math fonts currently support this.
 

The other way is using [font features]. For example, the roundhand style might be available in a font through the [stylistic set] 1 (`ss01`) feature. To use it in Typst, you could then define your own version of `scr` like in the example below.
   View example: Recreation using stylistic set 1  
```
#let scr(it) = text(
  stylistic-set: 1,
  $cal(it)$,
)

We establish $cal(P) != scr(P)$.

```
   math.scr([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to style.
 [Under/OverPrevious page] [VectorNext page]