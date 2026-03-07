---
url: https://typst.app/docs/reference/layout/box/
category: layout
topic: box
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Box] 
  

# `box`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

An inline-level container that sizes content.
 

All elements except inline math, text, and boxes are block-level and cannot occur inside of a [paragraph]. The box function can be used to integrate such elements into a paragraph. Boxes take the size of their contents by default but can also be sized explicitly.
 

## Example 
```
Refer to the docs
#box(
  height: 9pt,
  image("docs.svg")
)
for more information.

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    box([width: ][auto][relative][fraction],[height: ][auto][relative],[baseline: ][relative],[fill: ][none][color][gradient][tiling],[stroke: ][none][length][color][gradient][stroke][tiling][dictionary],[radius: ][relative][dictionary],[inset: ][relative][dictionary],[outset: ][relative][dictionary],[clip: ][bool],[][none][content],) -> [content]  

### `width`   [auto] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The width of the box.
 

Boxes can have [fractional] widths, as the example below demonstrates.
 

Note: Currently, only boxes and only their widths might be fractionally sized within paragraphs. Support for fractionally sized images, shapes, and more might be added in the future.
   View example   
```
Line in #box(width: 1fr, line(length: 100%)) between.

```
   

 Default: `auto` 
 

### `height`   [auto] or [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The height of the box.
 

 Default: `auto` 
 

### `baseline`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

An amount to shift the box's baseline by.
   View example   
```
Image: #box(baseline: 40%, image("tiger.jpg", width: 2cm)).

```
   

 Default: `0% + 0pt` 
 

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The box's background color. See the [rectangle's documentation] for more details.
 

 Default: `none` 
 

### `stroke`   [none] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The box's border color. See the [rectangle's documentation] for more details.
 

 Default: `(:)` 
 

### `radius`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to round the box's corners. See the [rectangle's documentation] for more details.
 

 Default: `(:)` 
 

### `inset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to pad the box's content.
 

This can be a single length for all sides or a dictionary of lengths for individual sides. When passing a dictionary, it can contain the following keys in order of precedence: `top`, `right`, `bottom`, `left` (controlling the respective cell sides), `x`, `y` (controlling vertical and horizontal insets), and `rest` (covers all insets not styled by other dictionary entries). All keys are optional; omitted keys will use their previously set value, or the default value if never set.
 

[Relative lengths] for this parameter are relative to the box size excluding [outset]. Note that relative insets and outsets are different from relative [widths] and [heights], which are relative to the container.
 

Note: When the box contains text, its exact size depends on the current [text edges].
   View example   
```
#rect(inset: 0pt)[Tight]

```
   

 Default: `(:)` 
 

### `outset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to expand the box's size without affecting the layout.
 

This can be a single length for all sides or a dictionary of lengths for individual sides. [Relative lengths] for this parameter are relative to the box size excluding outset. See the documentation for [inset] above for further details.
 

This is useful to prevent padding from affecting line layout. For a generalized version of the example below, see the documentation for the [raw text's block parameter].
   View example   
```
An inline
#box(
  fill: luma(235),
  inset: (x: 3pt, y: 0pt),
  outset: (y: 3pt),
  radius: 2pt,
)[rectangle].

```
   

 Default: `(:)` 
 

### `clip`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to clip the content inside the box.
 

Clipping is useful when the box's content is larger than the box itself, as any content that exceeds the box's bounds will be hidden.
   View example   
```
#box(
  width: 50pt,
  height: 50pt,
  clip: true,
  image("tiger.jpg", width: 100pt, height: 100pt)
)

```
   

 Default: `false` 
 

### `body`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The contents of the box.
 

 Default: `none` 
 [BlockPrevious page] [Column BreakNext page]