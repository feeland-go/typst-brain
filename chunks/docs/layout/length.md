---
url: https://typst.app/docs/reference/layout/length/
category: layout
topic: length
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Length] 
  

#  length  

A size or distance, possibly expressed with contextual units.
 

Typst supports the following length units:
  Points: `72pt`
 Millimeters: `254mm`
 Centimeters: `2.54cm`
 Inches: `1in`
 Relative to font size: `2.5em`
  

You can multiply lengths with and divide them by integers and floats.
 

## Example 
```
#rect(width: 20pt)
#rect(width: 2em)
#rect(width: 1in)

#(3em + 5pt).em \
#(20pt).em \
#(40em + 2pt).abs \
#(5em).abs

```
 

## Fields  `abs`: A length with just the absolute component of the current length (that is, excluding the `em` component).
 `em`: The amount of `em` units in this length, as a [float].
  

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  

### `pt`

Converts this length to points.
 

Fails with an error if this length has non-zero `em` units (such as `5em + 2pt` instead of just `2pt`). Use the `abs` field (such as in `(5em + 2pt).abs.pt()`) to ignore the `em` component of the length (thus converting only its absolute component).
 self.pt() -> [float]  

### `mm`

Converts this length to millimeters.
 

Fails with an error if this length has non-zero `em` units. See the [`pt`] method for more details.
 self.mm() -> [float]  

### `cm`

Converts this length to centimeters.
 

Fails with an error if this length has non-zero `em` units. See the [`pt`] method for more details.
 self.cm() -> [float]  

### `inches`

Converts this length to inches.
 

Fails with an error if this length has non-zero `em` units. See the [`pt`] method for more details.
 self.inches() -> [float]  

### `to-absolute`

Resolve this length to an absolute length.
   View example  
```
#set text(size: 12pt)
#context [
  #(6pt).to-absolute() \
  #(6pt + 10em).to-absolute() \
  #(10em).to-absolute()
]

#set text(size: 6pt)
#context [
  #(6pt).to-absolute() \
  #(6pt + 10em).to-absolute() \
  #(10em).to-absolute()
]

```
   self.to-absolute() -> [length]  [LayoutPrevious page] [MeasureNext page]