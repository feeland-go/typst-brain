---
url: https://typst.app/docs/reference/text/underline/
category: text
topic: underline
---

[  ] 
   
  [Reference] 
   
  [Text] 
   
  [Underline] 
  

# `underline`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Underlines text.
 

## Example 
```
This is #underline[important].

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    underline([stroke: ][auto][length][color][gradient][stroke][tiling][dictionary],[offset: ][auto][length],[extent: ][length],[evade: ][bool],[background: ][bool],[content],) -> [content]  

### `stroke`   [auto] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to [stroke] the line.
 

If set to `auto`, takes on the text's color and a thickness defined in the current font.
   View example   
```
Take #underline(
  stroke: 1.5pt + red,
  offset: 2pt,
  [care],
)

```
   

 Default: `auto` 
 

### `offset`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The position of the line relative to the baseline, read from the font tables if `auto`.
   View example   
```
#underline(offset: 5pt)[
  The Tale Of A Faraway Line I
]

```
   

 Default: `auto` 
 

### `extent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The amount by which to extend the line beyond (or within if negative) the content.
   View example   
```
#align(center,
  underline(extent: 2pt)[Chapter 1]
)

```
   

 Default: `0pt` 
 

### `evade`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the line skips sections in which it would collide with the glyphs.
   View example   
```
This #underline(evade: true)[is great].
This #underline(evade: false)[is less great].

```
   

 Default: `true` 
 

### `background`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the line is placed behind the content it underlines.
   View example   
```
#set underline(stroke: (thickness: 1em, paint: maroon, cap: "round"))
#underline(background: true)[This is stylized.] \
#underline(background: false)[This is partially hidden.]

```
   

 Default: `false` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to underline.
 [TextPrevious page] [UppercaseNext page]