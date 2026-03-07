---
url: https://typst.app/docs/reference/layout/hide/
category: layout
topic: hide
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Hide] 
  

# `hide`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Hides content without affecting layout.
 

The `hide` function allows you to hide content while the layout still "sees" it. This is useful for creating blank space that is exactly as large as some content.
 

## Example 
```
Hello Jane \
#hide[Hello] Joe

```
 

## Redaction 

This function may also be useful for redacting content as its arguments are neither present visually nor accessible to Assistive Technology. That said, there can be some traces of the hidden content (such as a bookmarked heading in the PDF's Document Outline).
 

Note that, depending on the circumstances, it may be possible for content to be reverse engineered based on its size in the layout. We thus do not recommend using this function to hide highly sensitive information.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    hide([content]) -> [content]  

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to hide.
 [GridPrevious page] [LayoutNext page]