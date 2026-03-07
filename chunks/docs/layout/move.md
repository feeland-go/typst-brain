---
url: https://typst.app/docs/reference/layout/move/
category: layout
topic: move
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Move] 
  

# `move`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Moves content without affecting layout.
 

The `move` function allows you to move content while the layout still 'sees' it at the original positions. Containers will still be sized as if the content was not moved.
 

## Example 
```
#rect(inset: 0pt, fill: gray, move(
  dx: 4pt, dy: 6pt,
  rect(
    inset: 8pt,
    fill: white,
    stroke: black,
    [Abra cadabra]
  )
))

```
 

## Accessibility 

Moving is transparent to Assistive Technology (AT). Your content will be read in the order it appears in the source, regardless of any visual movement. If you need to hide content from AT altogether in PDF export, consider using [`pdf.artifact`].

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    move([dx: ][relative],[dy: ][relative],[content],) -> [content]  

### `dx`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The horizontal displacement of the content.
 

 Default: `0% + 0pt` 
 

### `dy`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The vertical displacement of the content.
 

 Default: `0% + 0pt` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to move.
 [MeasurePrevious page] [PaddingNext page]