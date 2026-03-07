---
url: https://typst.app/docs/reference/visualize/polygon/
category: visualize
topic: polygon
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Polygon] 
  

# `polygon`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A closed polygon.
 

The polygon is defined by its corner points and is closed automatically.
 

## Example 
```
#polygon(
  fill: blue.lighten(80%),
  stroke: blue,
  (20%, 0pt),
  (60%, 0pt),
  (80%, 2cm),
  (0%,  2cm),
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    polygon([fill: ][none][color][gradient][tiling],[fill-rule: ][str],[stroke: ][none][auto][length][color][gradient][stroke][tiling][dictionary],[..][array],) -> [content]  

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to fill the polygon.
 

When setting a fill, the default stroke disappears. To create a rectangle with both fill and stroke, you have to configure both.
 

 Default: `none` 
 

### `fill-rule`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The drawing rule used to fill the polygon.
 

See the [curve documentation] for an example.
 VariantDetails`"non-zero"`

Specifies that "inside" is computed by a non-zero sum of signed edge crossings.
`"even-odd"`

Specifies that "inside" is computed by an odd number of edge crossings.
 

 Default: `"non-zero"` 
 

### `stroke`   [none] or [auto] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to [stroke] the polygon.
 

Can be set to `none` to disable the stroke or to `auto` for a stroke of `1pt` black if and only if no fill is given.
 

 Default: `auto` 
 

### `vertices`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The vertices of the polygon. Each point is specified as an array of two [relative lengths].
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `regular`

A regular polygon, defined by its size and number of vertices.
   View example  
```
#polygon.regular(
  fill: blue.lighten(80%),
  stroke: blue,
  size: 30pt,
  vertices: 3,
)

```
   polygon.regular([fill: ][none][color][gradient][tiling],[stroke: ][none][auto][length][color][gradient][stroke][tiling][dictionary],[size: ][length],[vertices: ][int],) -> [content]  `fill`   [none] or [color] or [gradient] or [tiling]    

How to fill the polygon. See the general [polygon's documentation] for more details.
 `stroke`   [none] or [auto] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]    

How to stroke the polygon. See the general [polygon's documentation] for more details.
 `size`   [length]    

The diameter of the [circumcircle] of the regular polygon.
 

 Default: `1em` 
 `vertices`   [int]    

The number of vertices in the polygon.
 

 Default: `3` 
 [PathPrevious page] [RectangleNext page]