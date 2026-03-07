---
url: https://typst.app/docs/reference/layout/skew/
category: layout
topic: skew
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Skew] 
  

# `skew`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Skews content.
 

Skews an element in horizontal and/or vertical direction. The layout will act as if the element was not skewed unless you specify `reflow: true`.
 

## Example 
```
#skew(ax: -12deg)[
  This is some fake italic text.
]

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    skew([ax: ][angle],[ay: ][angle],[origin: ][alignment],[reflow: ][bool],[content],) -> [content]  

### `ax`   [angle]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The horizontal skewing angle.
   View example   
```
#skew(ax: 30deg)[Skewed]

```
   

 Default: `0deg` 
 

### `ay`   [angle]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The vertical skewing angle.
   View example   
```
#skew(ay: 30deg)[Skewed]

```
   

 Default: `0deg` 
 

### `origin`   [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The origin of the skew transformation.
 

The origin will stay fixed during the operation.
   View example   
```
X #box(skew(ax: -30deg, origin: center + horizon)[X]) X \
X #box(skew(ax: -30deg, origin: bottom + left)[X]) X \
X #box(skew(ax: -30deg, origin: top + right)[X]) X

```
   

 Default: `center + horizon` 
 

### `reflow`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the skew transformation impacts the layout.
 

If set to `false`, the skewed content will retain the bounding box of the original content. If set to `true`, the bounding box will take the transformation of the content into account and adjust the layout accordingly.
   View example   
```
Hello #skew(ay: 30deg, reflow: true, "World")!

```
   

 Default: `false` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to skew.
 [ScalePrevious page] [Spacing (H)Next page]