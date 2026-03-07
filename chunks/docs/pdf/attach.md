---
url: https://typst.app/docs/reference/pdf/attach/
category: pdf
topic: attach
---

[  ] 
   
  [Reference] 
   
  [PDF] 
   
  [Attach] 
  

# `attach`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A file that will be attached to the output PDF.
 

This can be used to distribute additional files associated with the PDF within it. PDF readers will display the files in a file listing.
 

Some international standards use this mechanism to attach machine-readable data (e.g., ZUGFeRD/Factur-X for invoices) that mirrors the visual content of the PDF.
 

## Example 
```
#pdf.attach(
  "experiment.csv",
  relationship: "supplement",
  mime-type: "text/csv",
  description: "Raw Oxygen readings from the Arctic experiment",
)

```
 

## Notes  This element is ignored if exporting to a format other than PDF.
 File attachments are not currently supported for PDF/A-2, even if the attached file conforms to PDF/A-1 or PDF/A-2.
 

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    pdf.attach([str],[bytes],[relationship: ][none][str],[mime-type: ][none][str],[description: ][none][str],) -> [content]  

### `path`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The [path] of the file to be attached.
 

Must always be specified, but is only read from if no data is provided in the following argument.
 

### `data`   [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Raw file data, optionally.
 

If omitted, the data is read from the specified path.
 

### `relationship`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The relationship of the attached file to the document.
 

Ignored if export doesn't target PDF/A-3.
 VariantDetails`"source"`

The PDF document was created from the source file.
`"data"`

The file was used to derive a visual presentation in the PDF.
`"alternative"`

An alternative representation of the document.
`"supplement"`

Additional resources for the document.
 

 Default: `none` 
 

### `mime-type`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The MIME type of the attached file.
 

 Default: `none` 
 

### `description`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

A description for the attached file.
 

 Default: `none` 
 [ArtifactPrevious page] [Data CellNext page]