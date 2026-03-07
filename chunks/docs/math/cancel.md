---
url: https://typst.app/docs/reference/math/cancel/
category: math
topic: cancel
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Cancel] 
  

# `cancel`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Displays a diagonal line over a part of an equation.
 

This is commonly used to show the elimination of a term.
 

## Example 
```
Here, we can simplify:
$ (a dot b dot cancel(x)) /
    cancel(x) $

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.cancel([content],[length: ][relative],[inverted: ][bool],[cross: ][bool],[angle: ][auto][angle][function],[stroke: ][length][color][gradient][stroke][tiling][dictionary],) -> [content]  

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content over which the line should be placed.
 

### `length`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The length of the line, relative to the length of the diagonal spanning the whole element being "cancelled". A value of `100%` would then have the line span precisely the element's diagonal.
   View example   
```
$ a + cancel(x, length: #200%)
    - cancel(x, length: #200%) $

```
   

 Default: `100% + 3pt` 
 

### `inverted`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the cancel line should be inverted (flipped along the y-axis). For the default angle setting, inverted means the cancel line points to the top left instead of top right.
   View example   
```
$ (a cancel((b + c), inverted: #true)) /
    cancel(b + c, inverted: #true) $

```
   

 Default: `false` 
 

### `cross`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether two opposing cancel lines should be drawn, forming a cross over the element. Overrides `inverted`.
   View example   
```
$ cancel(Pi, cross: #true) $

```
   

 Default: `false` 
 

### `angle`   [auto] or [angle] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to rotate the cancel line.
  If given an angle, the line is rotated by that angle clockwise with respect to the y-axis.
 If `auto`, the line assumes the default angle; that is, along the rising diagonal of the content box.
 If given a function `angle => angle`, the line is rotated, with respect to the y-axis, by the angle returned by that function. The function receives the default angle as its input.
    View example   
```
$ cancel(Pi)
  cancel(Pi, angle: #0deg)
  cancel(Pi, angle: #45deg)
  cancel(Pi, angle: #90deg)
  cancel(1/(1+x), angle: #(a => a + 45deg))
  cancel(1/(1+x), angle: #(a => a + 90deg)) $

```
   

 Default: `auto` 
 

### `stroke`   [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to [stroke] the cancel line.
   View example   
```
$ cancel(
  sum x,
  stroke: #(
    paint: red,
    thickness: 1.5pt,
    dash: "dashed",
  ),
) $

```
   

 Default: `0.5pt` 
 [BinomialPrevious page] [CasesNext page]