---
url: https://typst.app/docs/reference/foundations/bytes/
category: foundations
topic: bytes
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Bytes] 
  

#  bytes  

A sequence of bytes.
 

This is conceptually similar to an array of [integers] between `0` and `255`, but represented much more efficiently. You can iterate over it using a [for loop].
 

You can convert
  a [string] or an [array] of integers to bytes with the [`bytes`] constructor
 bytes to a string with the [`str`] constructor, with UTF-8 encoding
 bytes to an array of integers with the [`array`] constructor
  

When [reading] data from a file, you can decide whether to load it as a string or as raw bytes.
 
```
#bytes((123, 160, 22, 0)) \
#bytes("Hello 😃")

#let data = read(
  "rhino.png",
  encoding: none,
)

// Magic bytes.
#array(data.slice(0, 4)) \
#str(data.slice(1, 4))

```
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value to bytes.
  Strings are encoded in UTF-8.
 Arrays of integers between `0` and `255` are converted directly. The dedicated byte representation is much more efficient than the array representation and thus typically used for large byte buffers (e.g. image data).
    View example  
```
#bytes("Hello 😃") \
#bytes((123, 160, 22, 0))

```
   bytes([str][bytes][array]) -> [bytes]  `value`   [str] or [bytes] or [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that should be converted to bytes.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `len`

The length in bytes.
 self.len() -> [int]  

### `at`

Returns the byte at the specified index. Returns the default value if the index is out of bounds or fails with an error if no default value was specified.
 self.at([int],[default: ]any,) -> any  `index`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The index at which to retrieve the byte.
 `default`   any    

A default value to return if the index is out of bounds.
 

### `slice`

Extracts a subslice of the bytes. Fails with an error if the start or end index is out of bounds.
 self.slice([int],[none][int],[count: ][int],) -> [bytes]  `start`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The start index (inclusive).
 `end`   [none] or [int]   Positional  Question mark    Positional parameters are specified in order, without names.      

The end index (exclusive). If omitted, the whole slice until the end is extracted.
 

 Default: `none` 
 `count`   [int]    

The number of items to extract. This is equivalent to passing `start + count` as the `end` position. Mutually exclusive with `end`.
 [BooleanPrevious page] [CalculationNext page]