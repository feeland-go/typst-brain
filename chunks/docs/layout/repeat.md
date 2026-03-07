---
url: https://typst.app/docs/reference/layout/repeat/
category: layout
topic: repeat
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Repeat] 
  

# `repeat`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Repeats content to the available space.
 

This can be useful when implementing a custom index, reference, or outline.
 

Space may be inserted between the instances of the body parameter, so be sure to adjust the [`justify`] parameter accordingly.
 

Errors if there are no bounds on the available space, as it would create infinite content.
 

## Example 
```
Sign on the dotted line:
#box(width: 1fr, repeat[.])

#set text(10pt)
#v(8pt, weak: true)
#align(right)[
  Berlin, the 22nd of December, 2022
]

```
 

## Accessibility 

Repeated content is automatically marked as an [artifact] and hidden from Assistive Technology (AT). Do not use this function to create content that contributes to the meaning of your document.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    repeat([content],[gap: ][length],[justify: ][bool],) -> [content]  

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to repeat.
 

### `gap`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The gap between each instance of the body.
 

 Default: `0pt` 
 

### `justify`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to increase the gap between instances to completely fill the available space.
 

 Default: `true` 
 [Relative LengthPrevious page] [RotateNext page]