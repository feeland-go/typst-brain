---
url: https://typst.app/docs/reference/layout/align/
category: layout
topic: align
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Align] 
  

# `align`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Aligns content horizontally and vertically.
 

## Example 

Let's start with centering our content horizontally:
 
```
#set page(height: 120pt)
#set align(center)

Centered text, a sight to see \
In perfect balance, visually \
Not left nor right, it stands alone \
A work of art, a visual throne

```
 

To center something vertically, use horizon alignment:
 
```
#set page(height: 120pt)
#set align(horizon)

Vertically centered, \
the stage had entered, \
a new paragraph.

```
 

## Combining alignments 

You can combine two alignments with the `+` operator. Let's also only apply this to one piece of content by using the function form instead of a set rule:
 
```
#set page(height: 120pt)
Though left in the beginning ...

#align(right + bottom)[
  ... they were right in the end, \
  and with addition had gotten, \
  the paragraph to the bottom!
]

```
 

## Nested alignment 

You can use varying alignments for layout containers and the elements within them. This way, you can create intricate layouts:
 
```
#align(center, block[
  #set align(left)
  Though centered together \
  alone \
  we \
  are \
  left.
])

```
 

## Alignment within the same line 

The `align` function performs block-level alignment and thus always interrupts the current paragraph. To have different alignment for parts of the same line, you should use [fractional spacing] instead:
 
```
Start #h(1fr) End

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    align([][alignment],[content],) -> [content]  

### `alignment`   [alignment]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The [alignment] along both axes.
   View example   
```
#set page(height: 6cm)
#set text(lang: "ar")

مثال
#align(
  end + horizon,
  rect(inset: 12pt)[ركن]
)

```
   

 Default: `start + top` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to align.
 [LayoutPrevious page] [AlignmentNext page]