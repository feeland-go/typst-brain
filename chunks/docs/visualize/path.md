---
url: https://typst.app/docs/reference/visualize/path/
category: visualize
topic: path
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Path] 
  

# `path`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  Warning  the `path` function is deprecated, use `curve` instead; it will be removed in Typst null

A path through a list of points, connected by Bézier curves.
 

## Example 
```
#path(
  fill: blue.lighten(80%),
  stroke: blue,
  closed: true,
  (0pt, 50pt),
  (100%, 50pt),
  ((50%, 0pt), (40pt, 0pt)),
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    path([fill: ][none][color][gradient][tiling],[fill-rule: ][str],[stroke: ][none][auto][length][color][gradient][stroke][tiling][dictionary],[closed: ][bool],[..][array],) -> [content]  

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to fill the path.
 

When setting a fill, the default stroke disappears. To create a rectangle with both fill and stroke, you have to configure both.
 

 Default: `none` 
 

### `fill-rule`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The drawing rule used to fill the path.
   View example   
```
// We use `.with` to get a new
// function that has the common
// arguments pre-applied.
#let star = path.with(
  fill: red,
  closed: true,
  (25pt, 0pt),
  (10pt, 50pt),
  (50pt, 20pt),
  (0pt, 20pt),
  (40pt, 50pt),
)

#star(fill-rule: "non-zero")
#star(fill-rule: "even-odd")

```
   VariantDetails`"non-zero"`

Specifies that "inside" is computed by a non-zero sum of signed edge crossings.
`"even-odd"`

Specifies that "inside" is computed by an odd number of edge crossings.
 

 Default: `"non-zero"` 
 

### `stroke`   [none] or [auto] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to [stroke] the path.
 

Can be set to `none` to disable the stroke or to `auto` for a stroke of `1pt` black if and only if no fill is given.
 

 Default: `auto` 
 

### `closed`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to close this path with one last Bézier curve. This curve will take into account the adjacent control points. If you want to close with a straight line, simply add one last point that's the same as the start point.
 

 Default: `false` 
 

### `vertices`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The vertices of the path.
 

Each vertex can be defined in 3 ways:
  A regular point, as given to the [`line`] or [`polygon`] function.
 An array of two points, the first being the vertex and the second being the control point. The control point is expressed relative to the vertex and is mirrored to get the second control point. The given control point is the one that affects the curve coming into this vertex (even for the first point). The mirrored control point affects the curve going out of this vertex.
 An array of three points, the first being the vertex and the next being the control points (control point for curves coming in and out, respectively).
  [LinePrevious page] [PolygonNext page]