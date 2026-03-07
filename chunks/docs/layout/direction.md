---
url: https://typst.app/docs/reference/layout/direction/
category: layout
topic: direction
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Direction] 
  

#  direction  

The four directions into which content can be laid out.
 

Possible values are:
  `ltr`: Left to right.
 `rtl`: Right to left.
 `ttb`: Top to bottom.
 `btt`: Bottom to top.
  

These values are available globally and also in the direction type's scope, so you can write either of the following two:
 
```
#stack(dir: rtl)[A][B][C]
#stack(dir: direction.rtl)[A][B][C]

```
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  

### `from`

Returns a direction from a starting point.
   View example  
```
#direction.from(left) \
#direction.from(right) \
#direction.from(top) \
#direction.from(bottom)

```
   direction.from([alignment]) -> [direction]  `side`   [alignment]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

### `to`

Returns a direction from an end point.
   View example  
```
#direction.to(left) \
#direction.to(right) \
#direction.to(top) \
#direction.to(bottom)

```
   direction.to([alignment]) -> [direction]  `side`   [alignment]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

### `axis`

The axis this direction belongs to, either `"horizontal"` or `"vertical"`.
   View example  
```
#ltr.axis() \
#ttb.axis()

```
   self.axis() -> [str]  

### `sign`

The corresponding sign, for use in calculations.
   View example  
```
#ltr.sign() \
#rtl.sign() \
#ttb.sign() \
#btt.sign()

```
   self.sign() -> [int]  

### `start`

The start point of this direction, as an alignment.
   View example  
```
#ltr.start() \
#rtl.start() \
#ttb.start() \
#btt.start()

```
   self.start() -> [alignment]  

### `end`

The end point of this direction, as an alignment.
   View example  
```
#ltr.end() \
#rtl.end() \
#ttb.end() \
#btt.end()

```
   self.end() -> [alignment]  

### `inv`

The inverse direction.
   View example  
```
#ltr.inv() \
#rtl.inv() \
#ttb.inv() \
#btt.inv()

```
   self.inv() -> [direction]  [ColumnsPrevious page] [FractionNext page]