---
url: https://typst.app/docs/reference/visualize/tiling/
category: visualize
topic: tiling
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Tiling] 
  

#  tiling  

A repeating tiling fill.
 

Typst supports the most common type of tilings, where a pattern is repeated in a grid-like fashion, covering the entire area of an element that is filled or stroked. The pattern is defined by a tile size and a body defining the content of each cell. You can also add horizontal or vertical spacing between the cells of the tiling.
 

## Examples 
```
#let pat = tiling(size: (30pt, 30pt))[
  #place(line(start: (0%, 0%), end: (100%, 100%)))
  #place(line(start: (0%, 100%), end: (100%, 0%)))
]

#rect(fill: pat, width: 100%, height: 60pt, stroke: 1pt)

```
 

Tilings are also supported on text, but only when setting the [relativeness] to either `auto` (the default value) or `"parent"`. To create word-by-word or glyph-by-glyph tilings, you can wrap the words or characters of your text in [boxes] manually or through a [show rule].
 
```
#let pat = tiling(
  size: (30pt, 30pt),
  relative: "parent",
  square(
    size: 30pt,
    fill: gradient
      .conic(..color.map.rainbow),
  )
)

#set text(fill: pat)
#lorem(10)

```
 

You can also space the elements further or closer apart using the [`spacing`] feature of the tiling. If the spacing is lower than the size of the tiling, the tiling will overlap. If it is higher, the tiling will have gaps of the same color as the background of the tiling.
 
```
#let pat = tiling(
  size: (30pt, 30pt),
  spacing: (10pt, 10pt),
  relative: "parent",
  square(
    size: 30pt,
    fill: gradient
     .conic(..color.map.rainbow),
  ),
)

#rect(
  width: 100%,
  height: 60pt,
  fill: pat,
)

```
 

## Relativeness 

The location of the starting point of the tiling is dependent on the dimensions of a container. This container can either be the shape that it is being painted on, or the closest surrounding container. This is controlled by the `relative` argument of a tiling constructor. By default, tilings are relative to the shape they are being painted on, unless the tiling is applied on text, in which case they are relative to the closest ancestor container.
 

Typst determines the ancestor container as follows:
  For shapes that are placed at the root/top level of the document, the closest ancestor is the page itself.
 For other shapes, the ancestor is the innermost [`block`] or [`box`] that contains the shape. This includes the boxes and blocks that are implicitly created by show rules and elements. For example, a [`rotate`] will not affect the parent of a gradient, but a [`grid`] will.
  

## Compatibility 

This type used to be called `pattern`. The name remains as an alias, but is deprecated since Typst 0.13.
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Construct a new tiling.
   View example  
```
#let pat = tiling(
  size: (20pt, 20pt),
  relative: "parent",
  place(
    dx: 5pt,
    dy: 5pt,
    rotate(45deg, square(
      size: 5pt,
      fill: black,
    )),
  ),
)

#rect(width: 100%, height: 60pt, fill: pat)

```
   tiling([size: ][auto][array],[spacing: ][array],[relative: ][auto][str],[content],) -> [tiling]  `size`   [auto] or [array]    

The bounding box of each cell of the tiling.
 

 Default: `auto` 
 `spacing`   [array]    

The spacing between cells of the tiling.
 

 Default: `(0pt, 0pt)` 
 `relative`   [auto] or [str]    

The [relative placement] of the tiling.
 

For an element placed at the root/top level of the document, the parent is the page itself. For other elements, the parent is the innermost block, box, column, grid, or stack that contains the element.
 VariantDetails`"self"`

Relative to itself (its own bounding box).
`"parent"`

Relative to its parent (the parent's bounding box).
 

 Default: `auto` 
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content of each cell of the tiling.
 [StrokePrevious page] [IntrospectionNext page]