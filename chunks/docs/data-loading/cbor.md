---
url: https://typst.app/docs/reference/data-loading/cbor/
category: data-loading
topic: cbor
---

[  ] 
   
  [Reference] 
   
  [Data Loading] 
   
  [CBOR] 
  

# `cbor`

Reads structured data from a CBOR file.
 

The file must contain a valid CBOR serialization. The CBOR values will be converted into corresponding Typst values as listed in the [table below].
 

The function returns a dictionary, an array or, depending on the CBOR file, another CBOR data type.
 

## Conversion details CBOR valueConverted into Typst integer[`int`] (or [`float`]) bytes[`bytes`] float[`float`] text[`str`] bool[`bool`] null`none` array[`array`] map[`dictionary`]  Typst valueConverted into CBOR types that can be converted from CBORcorresponding CBOR value [`symbol`]text [`content`]a map describing the content other types ([`length`], etc.)text via [`repr`]  

### Notes   

Be aware that CBOR integers larger than 263-1 or smaller than -263 will be converted to floating point numbers, which may result in an approximative value.
 
  

CBOR tags are not supported, and an error will be thrown.
 
  

The `repr` function is [for debugging purposes only], and its output is not guaranteed to be stable across Typst versions.
 
 

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  cbor([str][bytes]) -> any  

### `source`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A [path] to a CBOR file or raw CBOR bytes.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `decode` Warning  `cbor.decode` is deprecated, directly pass bytes to `cbor` instead; it will be removed in Typst 0.15.0

Reads structured data from CBOR bytes.
 cbor.decode([bytes]) -> any  `data`   [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

CBOR data.
 

### `encode`

Encode structured data into CBOR bytes.
 cbor.encode(any) -> [bytes]  `value`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Value to be encoded.
 [Data LoadingPrevious page] [CSVNext page]