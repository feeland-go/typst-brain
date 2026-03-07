---
url: https://typst.app/docs/reference/foundations/arguments/
category: foundations
topic: arguments
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Arguments] 
  

#  arguments  

Captured arguments to a function.
 

## Argument Sinks 

Like built-in functions, custom functions can also take a variable number of arguments. You can specify an argument sink which collects all excess arguments as `..sink`. The resulting `sink` value is of the `arguments` type. It exposes methods to access the positional and named arguments.
 
```
#let format(title, ..authors) = {
  let by = authors
    .pos()
    .join(", ", last: " and ")

  [*#title* \ _Written by #by;_]
}

#format("ArtosFlow", "Jane", "Joe")

```
 

## Spreading 

Inversely to an argument sink, you can spread arguments, arrays and dictionaries into a function call with the `..spread` operator:
 
```
#let array = (2, 3, 5)
#calc.min(..array)
#let dict = (fill: blue)
#text(..dict)[Hello]

```
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Construct spreadable arguments in place.
 

This function behaves like `let args(..sink) = sink`.
   View example  
```
#let args = arguments(stroke: red, inset: 1em, [Body])
#box(..args)

```
   arguments([..]any) -> [arguments]  `arguments`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The arguments to construct.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `at`

Returns the positional argument at the specified index, or the named argument with the specified name.
 

If the key is an [integer], this is equivalent to first calling [`pos`] and then [`array.at`]. If it is a [string], this is equivalent to first calling [`named`] and then [`dictionary.at`].
 self.at([int][str],[default: ]any,) -> any  `key`   [int] or [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The index or name of the argument to get.
 `default`   any    

A default value to return if the key is invalid.
 

### `pos`

Returns the captured positional arguments as an array.
 self.pos() -> [array]  

### `named`

Returns the captured named arguments as a dictionary.
 self.named() -> [dictionary]  [FoundationsPrevious page] [ArrayNext page]