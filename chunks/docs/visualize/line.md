---
url: https://typst.app/docs/reference/visualize/line/
category: visualize
topic: line
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Line] 
  

# `line`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A line from one point to another.
 

## Example 
```
#set page(height: 100pt)

#line(length: 100%)
#line(end: (50%, 50%))
#line(
  length: 4cm,
  stroke: 2pt + maroon,
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    line([start: ][array],[end: ][none][array],[length: ][relative],[angle: ][angle],[stroke: ][length][color][gradient][stroke][tiling][dictionary],) -> [content]  

### `start`   [array]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The start point of the line.
 

Must be an array of exactly two relative lengths.
 

 Default: `(0% + 0pt, 0% + 0pt)` 
 

### `end`   [none] or [array]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The point where the line ends.
 

 Default: `none` 
 

### `length`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The line's length. This is only respected if `end` is `none`.
 

 Default: `0% + 30pt` 
 

### `angle`   [angle]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The angle at which the line points away from the origin. This is only respected if `end` is `none`.
 

 Default: `0deg` 
 

### `stroke`   [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to [stroke] the line.
   View example   
```
#set line(length: 100%)
#stack(
  spacing: 1em,
  line(stroke: 2pt + red),
  line(stroke: (paint: blue, thickness: 4pt, cap: "round")),
  line(stroke: (paint: blue, thickness: 1pt, dash: "dashed")),
  line(stroke: (paint: blue, thickness: 1pt, dash: ("dot", 2pt, 4pt, 2pt))),
)

```
   

 Default: `1pt + black` 
 [ImagePrevious page] [PathNext page]