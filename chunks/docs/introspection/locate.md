---
url: https://typst.app/docs/reference/introspection/locate/
category: introspection
topic: locate
---

[  ] 
   
  [Reference] 
   
  [Introspection] 
   
  [Locate] 
  

# `locate`Contextual  Question mark    Contextual functions can only be used when the context is known   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Determines the location of an element in the document.
 

Takes a selector that must match exactly one element and returns that element's [`location`]. This location can, in particular, be used to retrieve the physical [`page`] number and [`position`] (page, x, y) for that element.
 

## Examples 

Locating a specific element:
 
```
#context [
  Introduction is at: \
  #locate(<intro>).position()
]

= Introduction <intro>

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    locate([label][selector][location][function]) -> [location]  

### `selector`   [label] or [selector] or [location] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A selector that should match exactly one element. This element will be located.
 

Especially useful in combination with
  [`here`] to locate the current context,
 a [`location`] retrieved from some queried element via the [`location()`] method on content.
  [HerePrevious page] [LocationNext page]