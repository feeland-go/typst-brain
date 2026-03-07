---
url: https://typst.app/docs/reference/layout/alignment/
category: layout
topic: alignment
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Alignment] 
  

#  alignment  

Where to align something along an axis.
 

Possible values are:
  `start`: Aligns at the [start] of the [text direction].
 `end`: Aligns at the [end] of the [text direction].
 `left`: Align at the left.
 `center`: Aligns in the middle, horizontally.
 `right`: Aligns at the right.
 `top`: Aligns at the top.
 `horizon`: Aligns in the middle, vertically.
 `bottom`: Align at the bottom.
  

These values are available globally and also in the alignment type's scope, so you can write either of the following two:
 
```
#align(center)[Hi]
#align(alignment.center)[Hi]

```
 

## 2D alignments 

To align along both axes at the same time, add the two alignments using the `+` operator. For example, `top + right` aligns the content to the top right corner.
 
```
#set page(height: 3cm)
#align(center + bottom)[Hi]

```
 

## Fields 

The `x` and `y` fields hold the alignment's horizontal and vertical components, respectively (as yet another `alignment`). They may be `none`.
 
```
#(top + right).x \
#left.x \
#left.y (none)

```
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  

### `axis`

The axis this alignment belongs to.
  `"horizontal"` for `start`, `left`, `center`, `right`, and `end`
 `"vertical"` for `top`, `horizon`, and `bottom`
 `none` for 2-dimensional alignments
    View example  
```
#left.axis() \
#bottom.axis()

```
   self.axis() -> [none][str]  

### `inv`

The inverse alignment.
   View example  
```
#top.inv() \
#left.inv() \
#center.inv() \
#(left + bottom).inv()

```
   self.inv() -> [alignment]  [AlignPrevious page] [AngleNext page]