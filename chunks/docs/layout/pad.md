---
url: https://typst.app/docs/reference/layout/pad/
category: layout
topic: pad
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Padding] 
  

# `pad`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Adds spacing around content.
 

The spacing can be specified for each side individually, or for all sides at once by specifying a positional argument.
 

## Example 
```
#set align(center)

#pad(x: 16pt, image("typing.jpg"))
_Typing speeds can be
 measured in words per minute._

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    pad([left: ][relative],[top: ][relative],[right: ][relative],[bottom: ][relative],[x: ][relative],[y: ][relative],[rest: ][relative],[content],) -> [content]  

### `left`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The padding at the left side.
 

 Default: `0% + 0pt` 
 

### `top`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The padding at the top side.
 

 Default: `0% + 0pt` 
 

### `right`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The padding at the right side.
 

 Default: `0% + 0pt` 
 

### `bottom`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The padding at the bottom side.
 

 Default: `0% + 0pt` 
 

### `x`   [relative]    

A shorthand to set `left` and `right` to the same value.
 

 Default: `0% + 0pt` 
 

### `y`   [relative]    

A shorthand to set `top` and `bottom` to the same value.
 

 Default: `0% + 0pt` 
 

### `rest`   [relative]    

A shorthand to set all four sides to the same value.
 

 Default: `0% + 0pt` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to pad at the sides.
 [MovePrevious page] [PageNext page]