---
url: https://typst.app/docs/reference/data-loading/json/
category: data-loading
topic: json
---

[  ] 
   
  [Reference] 
   
  [Data Loading] 
   
  [JSON] 
  

# `json`

Reads structured data from a JSON file.
 

The file must contain a valid JSON value, such as object or array. The JSON values will be converted into corresponding Typst values as listed in the [table below].
 

The function returns a dictionary, an array or, depending on the JSON file, another JSON data type.
 

The JSON files in the example contain objects with the keys `temperature`, `unit`, and `weather`.
 

## Example 
```
#let forecast(day) = block[
  #box(square(
    width: 2cm,
    inset: 8pt,
    fill: if day.weather == "sunny" {
      yellow
    } else {
      aqua
    },
    align(
      bottom + right,
      strong(day.weather),
    ),
  ))
  #h(6pt)
  #set text(22pt, baseline: -8pt)
  #day.temperature °#day.unit
]

#forecast(json("monday.json"))
#forecast(json("tuesday.json"))

```
 

## Conversion details JSON valueConverted into Typst `null``none` bool[`bool`] number[`float`] or [`int`] string[`str`] array[`array`] object[`dictionary`]  Typst valueConverted into JSON types that can be converted from JSONcorresponding JSON value [`bytes`]string via [`repr`] [`symbol`]string [`content`]an object describing the content other types ([`length`], etc.)string via [`repr`]  

### Notes   

In most cases, JSON numbers will be converted to floats or integers depending on whether they are whole numbers. However, be aware that integers larger than 263-1 or smaller than -263 will be converted to floating-point numbers, which may result in an approximative value.
 
  

Bytes are not encoded as JSON arrays for performance and readability reasons. Consider using [`cbor.encode`] for binary data.
 
  

The `repr` function is [for debugging purposes only], and its output is not guaranteed to be stable across Typst versions.
 
 

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  json([str][bytes]) -> any  

### `source`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A [path] to a JSON file or raw JSON bytes.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `decode` Warning  `json.decode` is deprecated, directly pass bytes to `json` instead; it will be removed in Typst 0.15.0

Reads structured data from a JSON string/bytes.
 json.decode([str][bytes]) -> any  `data`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

JSON data.
 

### `encode`

Encodes structured data into a JSON string.
 json.encode(any,[pretty: ][bool],) -> [str]  `value`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Value to be encoded.
 `pretty`   [bool]    

Whether to pretty print the JSON with newlines and indentation.
 

 Default: `true` 
 [CSVPrevious page] [ReadNext page]