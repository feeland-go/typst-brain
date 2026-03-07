---
url: https://typst.app/docs/reference/text/highlight/
category: text
topic: highlight
---

[  ] 
   
  [Reference] 
   
  [Text] 
   
  [Highlight] 
  

# `highlight`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Highlights text with a background color.
 

## Example 
```
This is #highlight[important].

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    highlight([fill: ][none][color][gradient][tiling],[stroke: ][none][length][color][gradient][stroke][tiling][dictionary],[top-edge: ][length][str],[bottom-edge: ][length][str],[extent: ][length],[radius: ][relative][dictionary],[content],) -> [content]  

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The color to highlight the text with.
   View example   
```
This is #highlight(
  fill: blue
)[highlighted with blue].

```
   

 Default: `rgb("#fffd11a1")` 
 

### `stroke`   [none] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The highlight's border color. See the [rectangle's documentation] for more details.
   View example   
```
This is a #highlight(
  stroke: fuchsia
)[stroked highlighting].

```
   

 Default: `(:)` 
 

### `top-edge`   [length] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The top end of the background rectangle.
   View example   
```
#set highlight(top-edge: "ascender")
#highlight[a] #highlight[aib]

#set highlight(top-edge: "x-height")
#highlight[a] #highlight[aib]

```
   VariantDetails`"ascender"`

The font's ascender, which typically exceeds the height of all glyphs.
`"cap-height"`

The approximate height of uppercase letters.
`"x-height"`

The approximate height of non-ascending lowercase letters.
`"baseline"`

The baseline on which the letters rest.
`"bounds"`

The top edge of the glyph's bounding box.
 

 Default: `"ascender"` 
 

### `bottom-edge`   [length] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The bottom end of the background rectangle.
   View example   
```
#set highlight(bottom-edge: "descender")
#highlight[a] #highlight[ap]

#set highlight(bottom-edge: "baseline")
#highlight[a] #highlight[ap]

```
   VariantDetails`"baseline"`

The baseline on which the letters rest.
`"descender"`

The font's descender, which typically exceeds the depth of all glyphs.
`"bounds"`

The bottom edge of the glyph's bounding box.
 

 Default: `"descender"` 
 

### `extent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The amount by which to extend the background to the sides beyond (or within if negative) the content.
   View example   
```
A long #highlight(extent: 4pt)[background].

```
   

 Default: `0pt` 
 

### `radius`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to round the highlight's corners. See the [rectangle's documentation] for more details.
   View example   
```
Listen #highlight(
  radius: 5pt, extent: 2pt
)[carefully], it will be on the test.

```
   

 Default: `(:)` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content that should be highlighted.
 [TextPrevious page] [Line BreakNext page]