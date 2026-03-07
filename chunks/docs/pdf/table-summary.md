---
url: https://typst.app/docs/reference/pdf/table-summary/
category: pdf
topic: table-summary
---

[  ] 
   
  [Reference] 
   
  [PDF] 
   
  [Table Summary] 
  

# `table-summary`

A summary of the purpose and structure of a complex table.
 

This will be available for Assistive Technology (AT), such as screen readers, when exporting to PDF, but not for sighted readers of your file.
 

This field is intended for instructions that help the user navigate the table using AT. It is not an alternative description, so do not duplicate the contents of the table within. Likewise, do not use this for the core takeaway of the table. Instead, include that in the text around the table or, even better, in a [figure caption].
 

If in doubt whether your table is complex enough to warrant a summary, err on the side of not including one. If you are certain that your table is complex enough, consider whether a sighted user might find it challenging. They might benefit from the instructions you put here, so consider printing them visibly in the document instead.
 

The API of this feature is temporary. Hence, calling this function requires enabling the `a11y-extras` feature flag at the moment. Even if this functionality should be available without a feature flag in the future, the summary will remain exclusive to PDF export.
 
```
#figure(
  pdf.table-summary(
    // The summary just provides orientation and structural
    // information for AT users.
    summary: "The first two columns list the names of each participant. The last column contains cells spanning multiple rows for their assigned group.",
    table(
      columns: 3,
      table.header[First Name][Given Name][Group],
      [Mike], [Davis], table.cell(rowspan: 3)[Sales],
      [Anna], [Smith],
      [John], [Johnson],
      [Sara], [Wilkins], table.cell(rowspan: 2)[Operations],
      [Tom], [Brown],
    ),
  ),
  // This is the key takeaway of the table, so we put it in the caption.
  caption: [The Sales org now has a new member],
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  pdf.table-summary([summary: ][str],[content],) -> [content]  

### `summary`   [str]    

### `table`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The table.
 [Header CellPrevious page] [HTMLNext page]