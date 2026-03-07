---
url: https://typst.app/docs/reference/visualize/stroke/
category: visualize
topic: stroke
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Stroke] 
  

#  stroke  

Defines how to draw a line.
 

A stroke has a paint (a solid color or gradient), a thickness, a line cap, a line join, a miter limit, and a dash pattern. All of these values are optional and have sensible defaults.
 

## Example 
```
#set line(length: 100%)
#stack(
  spacing: 1em,
  line(stroke: 2pt + red),
  line(stroke: (paint: blue, thickness: 4pt, cap: "round")),
  line(stroke: (paint: blue, thickness: 1pt, dash: "dashed")),
  line(stroke: 2pt + gradient.linear(..color.map.rainbow)),
)

```
 

## Simple strokes 

You can create a simple solid stroke from a color, a thickness, or a combination of the two. Specifically, wherever a stroke is expected you can pass any of the following values:
  A length specifying the stroke's thickness. The color is inherited, defaulting to black.
 A color to use for the stroke. The thickness is inherited, defaulting to `1pt`.
 A stroke combined from color and thickness using the `+` operator as in `2pt + red`.
  

For full control, you can also provide a [dictionary] or a `stroke` object to any function that expects a stroke. The dictionary's keys may include any of the parameters for the constructor function, shown below.
 

## Fields 

On a stroke object, you can access any of the fields listed in the constructor function. For example, `(2pt + blue).thickness` is `2pt`. Meanwhile, `stroke(red).cap` is `auto` because it's unspecified. Fields set to `auto` are inherited.
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value to a stroke or constructs a stroke with the given parameters.
 

Note that in most cases you do not need to convert values to strokes in order to use them, as they will be converted automatically. However, this constructor can be useful to ensure a value has all the fields of a stroke.
   View example  
```
#let my-func(x) = {
    x = stroke(x) // Convert to a stroke
    [Stroke has thickness #x.thickness.]
}
#my-func(3pt) \
#my-func(red) \
#my-func(stroke(cap: "round", thickness: 1pt))

```
   stroke([auto][color][gradient][tiling],[auto][length],[auto][str],[auto][str],[none][auto][str][array][dictionary],[auto][float],) -> [stroke]  `paint`   [auto] or [color] or [gradient] or [tiling]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The color or gradient to use for the stroke.
 

If set to `auto`, the value is inherited, defaulting to `black`.
 `thickness`   [auto] or [length]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The stroke's thickness.
 

If set to `auto`, the value is inherited, defaulting to `1pt`.
 `cap`   [auto] or [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

How the ends of the stroke are rendered.
 

If set to `auto`, the value is inherited, defaulting to `"butt"`.
 VariantDetails`"butt"`

Square stroke cap with the edge at the stroke's end point.
`"round"`

Circular stroke cap centered at the stroke's end point.
`"square"`

Square stroke cap centered at the stroke's end point.
 `join`   [auto] or [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

How sharp turns are rendered.
 

If set to `auto`, the value is inherited, defaulting to `"miter"`.
 VariantDetails`"miter"`

Segments are joined with sharp edges. Sharp bends exceeding the miter limit are bevelled instead.
`"round"`

Segments are joined with circular corners.
`"bevel"`

Segments are joined with a bevel (a straight edge connecting the butts of the joined segments).
 `dash`   [none] or [auto] or [str] or [array] or [dictionary]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The dash pattern to use. This can be:
  One of the predefined patterns:  `"solid"` or `none`
 `"dotted"`
 `"densely-dotted"`
 `"loosely-dotted"`
 `"dashed"`
 `"densely-dashed"`
 `"loosely-dashed"`
 `"dash-dotted"`
 `"densely-dash-dotted"`
 `"loosely-dash-dotted"`
  
 An [array] with alternating lengths for dashes and gaps. You can also use the string `"dot"` for a length equal to the line thickness.
 A [dictionary] with the keys `array` (same as the array above), and `phase` (of type [length]), which defines where in the pattern to start drawing.
  

If set to `auto`, the value is inherited, defaulting to `none`.
   View example   
```
#set line(length: 100%, stroke: 2pt)
#stack(
  spacing: 1em,
  line(stroke: (dash: "dashed")),
  line(stroke: (dash: (10pt, 5pt, "dot", 5pt))),
  line(stroke: (dash: (array: (10pt, 5pt, "dot", 5pt), phase: 10pt))),
)

```
      View options   VariantDetails`"solid"``"dotted"``"densely-dotted"``"loosely-dotted"``"dashed"``"densely-dashed"``"loosely-dashed"``"dash-dotted"``"densely-dash-dotted"``"loosely-dash-dotted"`   `miter-limit`   [auto] or [float]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Number at which protruding sharp bends are rendered with a bevel instead or a miter join. The higher the number, the sharper an angle can be before it is bevelled. Only applicable if `join` is `"miter"`.
 

Specifically, the miter limit is the maximum ratio between the corner's protrusion length and the stroke's thickness.
 

If set to `auto`, the value is inherited, defaulting to `4.0`.
   View example   
```
#let items = (
  curve.move((15pt, 0pt)),
  curve.line((0pt, 30pt)),
  curve.line((30pt, 30pt)),
  curve.line((10pt, 20pt)),
)

#set curve(stroke: 6pt + blue)
#stack(
  dir: ltr,
  spacing: 1cm,
  curve(stroke: (miter-limit: 1), ..items),
  curve(stroke: (miter-limit: 4), ..items),
  curve(stroke: (miter-limit: 5), ..items),
)

```
   [SquarePrevious page] [TilingNext page]