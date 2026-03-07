---
url: https://typst.app/docs/reference/layout/layout/
category: layout
topic: layout
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Layout] 
  

# `layout`

Provides access to the current outer container's (or page's, if none) dimensions (width and height).
 

Accepts a function that receives a single parameter, which is a dictionary with keys `width` and `height`, both of type [`length`]. The function is provided [context], meaning you don't need to use it in combination with the `context` keyword. This is why [`measure`] can be called in the example below.
 
```
#let text = lorem(30)
#layout(size => [
  #let (height,) = measure(
    width: size.width,
    text,
  )
  This text is #height high with
  the current page width: \
  #text
])

```
 

Note that the `layout` function forces its contents into a [block]-level container, so placement relative to the page or pagebreaks are not possible within it.
 

If the `layout` call is placed inside a box with a width of `800pt` and a height of `400pt`, then the specified function will be given the argument `(width: 800pt, height: 400pt)`. If it is placed directly into the page, it receives the page's dimensions minus its margins. This is mostly useful in combination with [measurement].
 

To retrieve the remaining height of the page rather than its full size, you can wrap your `layout` call in a `block(height: 1fr)`. This works because the block automatically grows to fill the remaining space (see the [fraction] documentation for more details).
 
```
#set page(height: 150pt)

#lorem(20)

#block(height: 1fr, layout(size => [
  Remaining height: #size.height
]))

```
 

You can also use this function to resolve a [`ratio`] to a fixed length. This might come in handy if you're building your own layout abstractions.
 
```
#layout(size => {
  let half = 50% * size.width
  [Half a page is #half wide.]
})

```
 

Note that the width or height provided by `layout` will be infinite if the corresponding page dimension is set to `auto`.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  layout([function]) -> [content]  

### `func`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A function to call with the outer container's size. Its return value is displayed in the document.
 

The container's size is given as a [dictionary] with the keys `width` and `height`, both of type [`length`].
 

This function is called once for each time the content returned by `layout` appears in the document. This makes it possible to generate content that depends on the dimensions of its container.
 [HidePrevious page] [LengthNext page]