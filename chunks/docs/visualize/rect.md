---
url: https://typst.app/docs/reference/visualize/rect/
category: visualize
topic: rect
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Rectangle] 
  

# `rect`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A rectangle with optional content.
 

## Example 
```
// Without content.
#rect(width: 35%, height: 30pt)

// With content.
#rect[
  Automatically sized \
  to fit the content.
]

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    rect([width: ][auto][relative],[height: ][auto][relative][fraction],[fill: ][none][color][gradient][tiling],[stroke: ][none][auto][length][color][gradient][stroke][tiling][dictionary],[radius: ][relative][dictionary],[inset: ][relative][dictionary],[outset: ][relative][dictionary],[][none][content],) -> [content]  

### `width`   [auto] or [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The rectangle's width, relative to its parent container.
 

 Default: `auto` 
 

### `height`   [auto] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The rectangle's height, relative to its parent container.
 

 Default: `auto` 
 

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to fill the rectangle.
 

When setting a fill, the default stroke disappears. To create a rectangle with both fill and stroke, you have to configure both.
   View example   
```
#rect(fill: blue)

```
   

 Default: `none` 
 

### `stroke`   [none] or [auto] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to stroke the rectangle. This can be:
   

`none` to disable stroking
 
  

`auto` for a stroke of `1pt + black` if and only if no fill is given.
 
  

Any kind of [stroke]
 
  

A dictionary describing the stroke for each side individually. The dictionary can contain the following keys in order of precedence:
  `top`: The top stroke.
 `right`: The right stroke.
 `bottom`: The bottom stroke.
 `left`: The left stroke.
 `x`: The horizontal stroke.
 `y`: The vertical stroke.
 `rest`: The stroke on all sides except those for which the dictionary explicitly sets a size.
  

All keys are optional; omitted keys will use their previously set value, or the default stroke if never set.
 
    View example   
```
#stack(
  dir: ltr,
  spacing: 1fr,
  rect(stroke: red),
  rect(stroke: 2pt),
  rect(stroke: 2pt + red),
)

```
   

 Default: `auto` 
 

### `radius`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to round the rectangle's corners, relative to the minimum of the width and height divided by two. This can be:
   

A relative length for a uniform corner radius.
 
  

A dictionary: With a dictionary, the stroke for each side can be set individually. The dictionary can contain the following keys in order of precedence:
  `top-left`: The top-left corner radius.
 `top-right`: The top-right corner radius.
 `bottom-right`: The bottom-right corner radius.
 `bottom-left`: The bottom-left corner radius.
 `left`: The top-left and bottom-left corner radii.
 `top`: The top-left and top-right corner radii.
 `right`: The top-right and bottom-right corner radii.
 `bottom`: The bottom-left and bottom-right corner radii.
 `rest`: The radii for all corners except those for which the dictionary explicitly sets a size.
  
    View example   
```
#set rect(stroke: 4pt)
#rect(
  radius: (
    left: 5pt,
    top-right: 20pt,
    bottom-right: 10pt,
  ),
  stroke: (
    left: red,
    top: yellow,
    right: green,
    bottom: blue,
  ),
)

```
   

 Default: `(:)` 
 

### `inset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to pad the rectangle's content. See the [box's documentation] for more details.
 

 Default: `0% + 5pt` 
 

### `outset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to expand the rectangle's size without affecting the layout. See the [box's documentation] for more details.
 

 Default: `(:)` 
 

### `body`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The content to place into the rectangle.
 

When this is omitted, the rectangle takes on a default size of at most `45pt` by `30pt`.
 

 Default: `none` 
 [PolygonPrevious page] [SquareNext page]