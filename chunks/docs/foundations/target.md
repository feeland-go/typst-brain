---
url: https://typst.app/docs/reference/foundations/target/
category: foundations
topic: target
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Target] 
  

# `target`Contextual  Question mark    Contextual functions can only be used when the context is known   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Returns the current export target.
 

This function returns either
  `"paged"` (for PDF, PNG, and SVG export), or
 `"html"` (for HTML export).
  

The design of this function is not yet finalized and for this reason it is guarded behind the `html` feature. Visit the [HTML documentation page] for more details.
 

## When to use it 

This function allows you to format your document properly across both HTML and paged export targets. It should primarily be used in templates and show rules, rather than directly in content. This way, the document's contents can be fully agnostic to the export target and content can be shared between PDF and HTML export.
 

## Varying targets 

This function is [contextual] as the target can vary within a single compilation: When exporting to HTML, the target will be `"paged"` while within an [`html.frame`].
 

## Example 
```
#let kbd(it) = context {
  if target() == "html" {
    html.elem("kbd", it)
  } else {
    set text(fill: rgb("#1f2328"))
    let r = 3pt
    box(
      fill: rgb("#f6f8fa"),
      stroke: rgb("#d1d9e0b3"),
      outset: (y: r),
      inset: (x: r),
      radius: r,
      raw(it)
    )
  }
}

Press #kbd("F1") for help.

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    target() -> [str]  [SystemPrevious page] [TypeNext page]