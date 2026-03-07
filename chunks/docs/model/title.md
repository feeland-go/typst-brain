---
url: https://typst.app/docs/reference/model/title/
category: model
topic: title
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Title] 
  

# `title`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A document title.
 

This should be used to display the main title of the whole document and should occur only once per document. In contrast, level 1 [headings] are intended to be used for the top-level sections of the document.
 

Note that additional frontmatter (like an author list) that should appear together with the title does not belong in its body.
 

In HTML export, this shows as a `h1` element while level 1 headings show as `h2` elements.
 

## Example 
```
#set document(
  title: [Interstellar Mail Delivery]
)

#title()

= Introduction
In recent years, ...

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    title([][auto][content]) -> [content]  

### `body`   [auto] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The content of the title.
 

When omitted (or `auto`), this will default to [`document.title`]. In this case, a document title must have been previously set with `set document(title: [..])`.
   View example   
```
#set document(title: "Course ABC, Homework 1")
#title[Homework 1]

...

```
   

 Default: `auto` 
 [Term ListPrevious page] [TextNext page]