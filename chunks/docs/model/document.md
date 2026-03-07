---
url: https://typst.app/docs/reference/model/document/
category: model
topic: document
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Document] 
  

# `document`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

The root element of a document and its metadata.
 

All documents are automatically wrapped in a `document` element. You cannot create a document element yourself. This function is only used with [set rules] to specify document metadata. Such a set rule must not occur inside of any layout container.
 
```
#set document(title: [Hello])

This has no visible output, but
embeds metadata into the PDF!

```
 

Note that metadata set with this function is not rendered within the document. Instead, it is embedded in the compiled PDF file.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    document([title: ][none][content],[author: ][str][array],[description: ][none][content],[keywords: ][str][array],[date: ][none][auto][datetime],) -> [content]  

### `title`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The document's title. This is rendered as the title of the PDF viewer window or the browser tab of the page.
 

Adding a title is important for accessibility, as it makes it easier to navigate to your document and identify it among other open documents. When exporting to PDF/UA, a title is required.
 

While this can be arbitrary content, PDF viewers only support plain text titles, so the conversion might be lossy.
 

 Default: `none` 
 

### `author`   [str] or [array]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The document's authors.
 

 Default: `()` 
 

### `description`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The document's description.
 

 Default: `none` 
 

### `keywords`   [str] or [array]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The document's keywords.
 

 Default: `()` 
 

### `date`   [none] or [auto] or [datetime]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The document's creation date.
 

If this is `auto` (default), Typst uses the current date and time. Setting it to `none` prevents Typst from embedding any creation date into the PDF metadata.
 

The year component must be at least zero in order to be embedded into a PDF.
 

If you want to create byte-by-byte reproducible PDFs, set this to something other than `auto`.
 

 Default: `auto` 
 [CitePrevious page] [EmphasisNext page]