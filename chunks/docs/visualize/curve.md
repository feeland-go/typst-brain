---
url: https://typst.app/docs/reference/visualize/curve/
category: visualize
topic: curve
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Curve] 
  

# `curve`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A curve consisting of movements, lines, and Bézier segments.
 

At any point in time, there is a conceptual pen or cursor.
  Move elements move the cursor without drawing.
 Line/Quadratic/Cubic elements draw a segment from the cursor to a new position, potentially with control point for a Bézier curve.
 Close elements draw a straight or smooth line back to the start of the curve or the latest preceding move segment.
  

For layout purposes, the bounding box of the curve is a tight rectangle containing all segments as well as the point `(0pt, 0pt)`.
 

Positions may be specified absolutely (i.e. relatively to `(0pt, 0pt)`), or relative to the current pen/cursor position, that is, the position where the previous segment ended.
 

Bézier curve control points can be skipped by passing `none` or automatically mirrored from the preceding segment by passing `auto`.
 

## Example 
```
#curve(
  fill: blue.lighten(80%),
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.cubic(none, (90pt, 0pt), (50pt, 0pt)),
  curve.close(),
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    curve([fill: ][none][color][gradient][tiling],[fill-rule: ][str],[stroke: ][none][auto][length][color][gradient][stroke][tiling][dictionary],[..][content],) -> [content]  

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to fill the curve.
 

When setting a fill, the default stroke disappears. To create a curve with both fill and stroke, you have to configure both.
 

 Default: `none` 
 

### `fill-rule`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The drawing rule used to fill the curve.
   View example   
```
// We use `.with` to get a new
// function that has the common
// arguments pre-applied.
#let star = curve.with(
  fill: red,
  curve.move((25pt, 0pt)),
  curve.line((10pt, 50pt)),
  curve.line((50pt, 20pt)),
  curve.line((0pt, 20pt)),
  curve.line((40pt, 50pt)),
  curve.close(),
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

How to [stroke] the curve.
 

Can be set to `none` to disable the stroke or to `auto` for a stroke of `1pt` black if and only if no fill is given.
   View example   
```
#let down = curve.line((40pt, 40pt), relative: true)
#let up = curve.line((40pt, -40pt), relative: true)

#curve(
  stroke: 4pt + gradient.linear(red, blue),
  down, up, down, up, down,
)

```
   

 Default: `auto` 
 

### `components`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The components of the curve, in the form of moves, line and Bézier segment, and closes.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `move`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Starts a new curve component.
 

If no `curve.move` element is passed, the curve will start at `(0pt, 0pt)`.
   View example  
```
#curve(
  fill: blue.lighten(80%),
  fill-rule: "even-odd",
  stroke: blue,
  curve.line((50pt, 0pt)),
  curve.line((50pt, 50pt)),
  curve.line((0pt, 50pt)),
  curve.close(),
  curve.move((10pt, 10pt)),
  curve.line((40pt, 10pt)),
  curve.line((40pt, 40pt)),
  curve.line((10pt, 40pt)),
  curve.close(),
)

```
   curve.move([array],[relative: ][bool],) -> [content]  `start`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The starting point for the new component.
 `relative`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the coordinates are relative to the previous point.
 

 Default: `false` 
 

### `line`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Adds a straight line from the current point to a following one.
   View example  
```
#curve(
  stroke: blue,
  curve.line((50pt, 0pt)),
  curve.line((50pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.line((100pt, 0pt)),
  curve.line((150pt, 0pt)),
)

```
   curve.line([array],[relative: ][bool],) -> [content]  `end`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The point at which the line shall end.
 `relative`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the coordinates are relative to the previous point.
   View example   
```
#curve(
  stroke: blue,
  curve.line((50pt, 0pt), relative: true),
  curve.line((0pt, 50pt), relative: true),
  curve.line((50pt, 0pt), relative: true),
  curve.line((0pt, -50pt), relative: true),
  curve.line((50pt, 0pt), relative: true),
)

```
   

 Default: `false` 
 

### `quad`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Adds a quadratic Bézier curve segment from the last point to `end`, using `control` as the control point.
   View example  
```
// Function to illustrate where the control point is.
#let mark((x, y)) = place(
  dx: x - 1pt, dy: y - 1pt,
  circle(fill: aqua, radius: 2pt),
)

#mark((20pt, 20pt))

#curve(
  stroke: blue,
  curve.move((0pt, 100pt)),
  curve.quad((20pt, 20pt), (100pt, 0pt)),
)

```
   curve.quad([none][auto][array],[array],[relative: ][bool],) -> [content]  `control`   [none] or [auto] or [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The control point of the quadratic Bézier curve.
  If `auto` and this segment follows another quadratic Bézier curve, the previous control point will be mirrored.
 If `none`, the control point defaults to `end`, and the curve will be a straight line.
    View example   
```
#curve(
  stroke: 2pt,
  curve.quad((20pt, 40pt), (40pt, 40pt), relative: true),
  curve.quad(auto, (40pt, -40pt), relative: true),
)

```
   `end`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The point at which the segment shall end.
 `relative`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the `control` and `end` coordinates are relative to the previous point.
 

 Default: `false` 
 

### `cubic`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Adds a cubic Bézier curve segment from the last point to `end`, using `control-start` and `control-end` as the control points.
   View example  
```
// Function to illustrate where the control points are.
#let handle(start, end) = place(
  line(stroke: red, start: start, end: end)
)

#handle((0pt, 80pt), (10pt, 20pt))
#handle((90pt, 60pt), (100pt, 0pt))

#curve(
  stroke: blue,
  curve.move((0pt, 80pt)),
  curve.cubic((10pt, 20pt), (90pt, 60pt), (100pt, 0pt)),
)

```
   curve.cubic([none][auto][array],[none][array],[array],[relative: ][bool],) -> [content]  `control-start`   [none] or [auto] or [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The control point going out from the start of the curve segment.
   

If `auto` and this element follows another `curve.cubic` element, the last control point will be mirrored. In SVG terms, this makes `curve.cubic` behave like the `S` operator instead of the `C` operator.
 
  

If `none`, the curve has no first control point, or equivalently, the control point defaults to the curve's starting point.
 
    View example   
```
#curve(
  stroke: blue,
  curve.move((0pt, 50pt)),
  // - No start control point
  // - End control point at `(20pt, 0pt)`
  // - End point at `(50pt, 0pt)`
  curve.cubic(none, (20pt, 0pt), (50pt, 0pt)),
  // - No start control point
  // - No end control point
  // - End point at `(50pt, 0pt)`
  curve.cubic(none, none, (100pt, 50pt)),
)

#curve(
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.cubic(none, (20pt, 0pt), (50pt, 0pt)),
  // Passing `auto` instead of `none` means the start control point
  // mirrors the end control point of the previous curve. Mirror of
  // `(20pt, 0pt)` w.r.t `(50pt, 0pt)` is `(80pt, 0pt)`.
  curve.cubic(auto, none, (100pt, 50pt)),
)

#curve(
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.cubic(none, (20pt, 0pt), (50pt, 0pt)),
  // `(80pt, 0pt)` is the same as `auto` in this case.
  curve.cubic((80pt, 0pt), none, (100pt, 50pt)),
)

```
   `control-end`   [none] or [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The control point going into the end point of the curve segment.
 

If set to `none`, the curve has no end control point, or equivalently, the control point defaults to the curve's end point.
 `end`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The point at which the curve segment shall end.
 `relative`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the `control-start`, `control-end`, and `end` coordinates are relative to the previous point.
 

 Default: `false` 
 

### `close`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Closes the curve by adding a segment from the last point to the start of the curve (or the last preceding `curve.move` point).
   View example  
```
// We define a function to show the same shape with
// both closing modes.
#let shape(mode: "smooth") = curve(
  fill: blue.lighten(80%),
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.cubic(auto, (90pt, 0pt), (50pt, 0pt)),
  curve.close(mode: mode),
)

#shape(mode: "smooth")
#shape(mode: "straight")

```
   curve.close([mode: ][str]) -> [content]  `mode`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to close the curve.
 VariantDetails`"smooth"`

Closes the curve with a smooth segment that takes into account the control point opposite the start point.
`"straight"`

Closes the curve with a straight line.
 

 Default: `"smooth"` 
 [ColorPrevious page] [EllipseNext page]