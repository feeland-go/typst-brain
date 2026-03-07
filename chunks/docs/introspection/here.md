---
url: https://typst.app/docs/reference/introspection/here/
category: introspection
topic: here
---

[  ] 
   
  [Reference] 
   
  [Introspection] 
   
  [Here] 
  

# `here`Contextual  Question mark    Contextual functions can only be used when the context is known   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Provides the current location in the document.
 

You can think of `here` as a low-level building block that directly extracts the current location from the active [context]. Some other functions use it internally: For instance, `counter.get()` is equivalent to `counter.at(here())`.
 

Within show rules on [locatable] elements, `here()` will match the location of the shown element.
 

If you want to display the current page number, refer to the documentation of the [`counter`] type. While `here` can be used to determine the physical page number, typically you want the logical page number that may, for instance, have been reset after a preface.
 

## Examples 

Determining the current position in the document in combination with the [`position`] method:
 
```
#context [
  I am located at
  #here().position()
]

```
 

Running a [query] for elements before the current position:
 
```
= Introduction
= Background

There are
#context query(
  selector(heading).before(here())
).len()
headings before me.

= Conclusion

```
 

Refer to the [`selector`] type for more details on before/after selectors.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    here() -> [location]  [CounterPrevious page] [LocateNext page]