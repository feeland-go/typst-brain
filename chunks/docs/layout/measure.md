---
url: https://typst.app/docs/reference/layout/measure/
category: layout
topic: measure
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Measure] 
  

# `measure`Contextual  Question mark    Contextual functions can only be used when the context is known   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Measures the layouted size of content.
 

The `measure` function lets you determine the layouted size of content. By default an infinite space is assumed, so the measured dimensions may not necessarily match the final dimensions of the content. If you want to measure in the current layout dimensions, you can combine `measure` and [`layout`].
 

## Example 

The same content can have a different size depending on the [context] that it is placed into. In the example below, the `#content` is of course bigger when we increase the font size.
 
```
#let content = [Hello!]
#content
#set text(14pt)
#content

```
 

For this reason, you can only measure when context is available.
 
```
#let thing(body) = context {
  let size = measure(body)
  [Width of "#body" is #size.width]
}

#thing[Hey] \
#thing[Welcome]

```
 

The measure function returns a dictionary with the entries `width` and `height`, both of type [`length`].

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    measure([width: ][auto][length],[height: ][auto][length],[content],) -> [dictionary]  

### `width`   [auto] or [length]    

The width available to layout the content.
 

Setting this to `auto` indicates infinite available width.
 

Note that using the `width` and `height` parameters of this function is different from measuring a sized [`block`] containing the content. In the following example, the former will get the dimensions of the inner content instead of the dimensions of the block.
   View example   
```
#context measure(lorem(100), width: 400pt)

#context measure(block(lorem(100), width: 400pt))

```
   

 Default: `auto` 
 

### `height`   [auto] or [length]    

The height available to layout the content.
 

Setting this to `auto` indicates infinite available height.
 

 Default: `auto` 
 

### `content`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content whose size to measure.
 [LengthPrevious page] [MoveNext page]