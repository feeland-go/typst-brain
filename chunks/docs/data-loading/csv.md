---
url: https://typst.app/docs/reference/data-loading/csv/
category: data-loading
topic: csv
---

[  ] 
   
  [Reference] 
   
  [Data Loading] 
   
  [CSV] 
  

# `csv`

Reads structured data from a CSV file.
 

The CSV file will be read and parsed into a 2-dimensional array of strings: Each row in the CSV file will be represented as an array of strings, and all rows will be collected into a single array. Header rows will not be stripped.
 

## Example 
```
#let results = csv("example.csv")

#table(
  columns: 2,
  [*Condition*], [*Result*],
  ..results.flatten(),
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  csv([str][bytes],[delimiter: ][str],[row-type: ][type],) -> [array]  

### `source`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A [path] to a CSV file or raw CSV bytes.
 

### `delimiter`   [str]    

The delimiter that separates columns in the CSV file. Must be a single ASCII character.
 

 Default: `","` 
 

### `row-type`   [type]    

How to represent the file's rows.
  If set to `array`, each row is represented as a plain array of strings.
 If set to `dictionary`, each row is represented as a dictionary mapping from header keys to strings. This option only makes sense when a header row is present in the CSV file.
  

 Default: `array` 
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `decode` Warning  `csv.decode` is deprecated, directly pass bytes to `csv` instead; it will be removed in Typst 0.15.0

Reads structured data from a CSV string/bytes.
 csv.decode([str][bytes],[delimiter: ][str],[row-type: ][type],) -> [array]  `data`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

CSV data.
 `delimiter`   [str]    

The delimiter that separates columns in the CSV file. Must be a single ASCII character.
 

 Default: `","` 
 `row-type`   [type]    

How to represent the file's rows.
  If set to `array`, each row is represented as a plain array of strings.
 If set to `dictionary`, each row is represented as a dictionary mapping from header keys to strings. This option only makes sense when a header row is present in the CSV file.
  

 Default: `array` 
 [CBORPrevious page] [JSONNext page]