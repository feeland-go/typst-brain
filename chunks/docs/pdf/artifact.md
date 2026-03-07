---
url: https://typst.app/docs/reference/pdf/artifact/
category: pdf
topic: artifact
---

[  ] 
   
  [Reference] 
   
  [PDF] 
   
  [Artifact] 
  

# `artifact`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Marks content as a PDF artifact.
 

Artifacts are parts of the document that are not meant to be read by Assistive Technology (AT), such as screen readers. Typical examples include purely decorative images that do not contribute to the meaning of the document, watermarks, or repeated content such as page numbers.
 

Typst will automatically mark certain content, such as page headers, footers, backgrounds, and foregrounds, as artifacts. Likewise, paths and shapes are automatically marked as artifacts, but their content is not. Repetitions of table headers and footers are also marked as artifacts.
 

Once something is marked as an artifact, you cannot make any of its contents accessible again. If you need to mark only part of something as an artifact, you may need to use this function multiple times.
 

If you are unsure what constitutes an artifact, check the [Accessibility Guide].
 

In the future, this function may be moved out of the `pdf` module, making it possible to hide content in HTML export from AT.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    pdf.artifact([kind: ][str],[content],) -> [content]  

### `kind`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The artifact kind.
 

This will govern how the PDF reader treats the artifact during reflow and content extraction (e.g. copy and paste).
 VariantDetails`"header"`

Repeats on the top of each page.
`"footer"`

Repeats at the bottom of each page.
`"page"`

Not part of the document, but rather the page it is printed on. An example would be cut marks or color bars.
`"other"`

Other artifacts, including purely cosmetic content, backgrounds, watermarks, and repeated content.
 

 Default: `"other"` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content that is an artifact.
 [PDFPrevious page] [AttachNext page]