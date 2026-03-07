---
url: https://typst.app/docs/reference/data-loading/toml/
category: data-loading
topic: toml
---

[  ] 
   
  [Reference] 
   
  [Data Loading] 
   
  [TOML] 
  

# `toml`

Reads structured data from a TOML file.
 

The file must contain a valid TOML table. The TOML values will be converted into corresponding Typst values as listed in the [table below].
 

The function returns a dictionary representing the TOML table.
 

The TOML file in the example consists of a table with the keys `title`, `version`, and `authors`.
 

## Example 
```
#let details = toml("details.toml")

Title: #details.title \
Version: #details.version \
Authors: #(details.authors
  .join(", ", last: " and "))

```
 

## Conversion details 

First of all, TOML documents are tables. Other values must be put in a table to be encoded or decoded.
 TOML valueConverted into Typst string[`str`] integer[`int`] float[`float`] boolean[`bool`] datetime[`datetime`] array[`array`] table[`dictionary`]  Typst valueConverted into TOML types that can be converted from TOMLcorresponding TOML value `none`ignored [`bytes`]string via [`repr`] [`symbol`]string [`content`]a table describing the content other types ([`length`], etc.)string via [`repr`]  

### Notes   

Be aware that TOML integers larger than 263-1 or smaller than -263 cannot be represented losslessly in Typst, and an error will be thrown according to the [specification].
 
  

Bytes are not encoded as TOML arrays for performance and readability reasons. Consider using [`cbor.encode`] for binary data.
 
  

The `repr` function is [for debugging purposes only], and its output is not guaranteed to be stable across Typst versions.
 
 

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  toml([str][bytes]) -> [dictionary]  

### `source`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A [path] to a TOML file or raw TOML bytes.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `decode` Warning  `toml.decode` is deprecated, directly pass bytes to `toml` instead; it will be removed in Typst 0.15.0

Reads structured data from a TOML string/bytes.
 toml.decode([str][bytes]) -> [dictionary]  `data`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

TOML data.
 

### `encode`

Encodes structured data into a TOML string.
 toml.encode([dictionary],[pretty: ][bool],) -> [str]  `value`   [dictionary]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Value to be encoded.
 

TOML documents are tables. Therefore, only dictionaries are suitable.
 `pretty`   [bool]    

Whether to pretty-print the resulting TOML.
 

 Default: `true` 
 [ReadPrevious page] [XMLNext page]