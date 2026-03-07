---
url: https://typst.app/docs/reference/layout/scale/
category: layout
topic: scale
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Scale] 
  

# `scale`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Scales content without affecting layout.
 

Lets you mirror content by specifying a negative scale on a single axis.
 

## Example 
```
#set align(center)
#scale(x: -100%)[This is mirrored.]
#scale(x: -100%, reflow: true)[This is mirrored.]

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    scale([factor: ][auto][length][ratio],[x: ][auto][length][ratio],[y: ][auto][length][ratio],[origin: ][alignment],[reflow: ][bool],[content],) -> [content]  

### `factor`   [auto] or [length] or [ratio]    

The scaling factor for both axes, as a positional argument. This is just an optional shorthand notation for setting `x` and `y` to the same value.
 

 Default: `100%` 
 

### `x`   [auto] or [length] or [ratio]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The horizontal scaling factor.
 

The body will be mirrored horizontally if the parameter is negative.
 

 Default: `100%` 
 

### `y`   [auto] or [length] or [ratio]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The vertical scaling factor.
 

The body will be mirrored vertically if the parameter is negative.
 

 Default: `100%` 
 

### `origin`   [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The origin of the transformation.
   View example   
```
A#box(scale(75%)[A])A \
B#box(scale(75%, origin: bottom + left)[B])B

```
   

 Default: `center + horizon` 
 

### `reflow`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the scaling impacts the layout.
 

If set to `false`, the scaled content will be allowed to overlap other content. If set to `true`, it will compute the new size of the scaled content and adjust the layout accordingly.
   View example   
```
Hello #scale(x: 20%, y: 40%, reflow: true)[World]!

```
   

 Default: `false` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to scale.
 [RotatePrevious page] [SkewNext page]