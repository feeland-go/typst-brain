---
url: https://typst.app/docs/reference/layout/pagebreak/
category: layout
topic: pagebreak
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Page Break] 
  

# `pagebreak`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A manual page break.
 

Must not be used inside any containers.
 

## Example 
```
The next page contains
more details on compound theory.
#pagebreak()

== Compound Theory
In 1984, the first ...

```
  

Even without manual page breaks, content will be automatically paginated based on the configured page size. You can set [the page height] to `auto` to let the page grow dynamically until a manual page break occurs.
 

Pagination tries to avoid single lines of text at the top or bottom of a page (these are called widows and orphans). You can adjust the [`text.costs`] parameter to disable this behavior.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    pagebreak([weak: ][bool],[to: ][none][str],) -> [content]  

### `weak`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

If `true`, the page break is skipped if the current page is already empty.
 

 Default: `false` 
 

### `to`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

If given, ensures that the next page will be an even/odd page, with an empty page in between if necessary.
   View example   
```
#set page(height: 30pt)

First.
#pagebreak(to: "odd")
Third.

```
     VariantDetails`"even"`

Next page will be an even page.
`"odd"`

Next page will be an odd page.
 

 Default: `none` 
 [PagePrevious page] [PlaceNext page]