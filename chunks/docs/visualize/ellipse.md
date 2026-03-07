---
url: https://typst.app/docs/reference/visualize/ellipse/
category: visualize
topic: ellipse
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Ellipse] 
  

# `ellipse`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

An ellipse with optional content.
 

## Example 
```
// Without content.
#ellipse(width: 35%, height: 30pt)

// With content.
#ellipse[
  #set align(center)
  Automatically sized \
  to fit the content.
]

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    ellipse([width: ][auto][relative],[height: ][auto][relative][fraction],[fill: ][none][color][gradient][tiling],[stroke: ][none][auto][length][color][gradient][stroke][tiling][dictionary],[inset: ][relative][dictionary],[outset: ][relative][dictionary],[][none][content],) -> [content]  

### `width`   [auto] or [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The ellipse's width, relative to its parent container.
 

 Default: `auto` 
 

### `height`   [auto] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The ellipse's height, relative to its parent container.
 

 Default: `auto` 
 

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to fill the ellipse. See the [rectangle's documentation] for more details.
 

 Default: `none` 
 

### `stroke`   [none] or [auto] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to stroke the ellipse. See the [rectangle's documentation] for more details.
 

 Default: `auto` 
 

### `inset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to pad the ellipse's content. See the [box's documentation] for more details.
 

 Default: `0% + 5pt` 
 

### `outset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to expand the ellipse's size without affecting the layout. See the [box's documentation] for more details.
 

 Default: `(:)` 
 

### `body`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The content to place into the ellipse.
 

When this is omitted, the ellipse takes on a default size of at most `45pt` by `30pt`.
 

 Default: `none` 
 [CurvePrevious page] [GradientNext page]