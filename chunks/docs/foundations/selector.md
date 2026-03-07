---
url: https://typst.app/docs/reference/foundations/selector/
category: foundations
topic: selector
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Selector] 
  

#  selector  

A filter for selecting elements within the document.
 

To construct a selector you can:
  use an [element function]
 filter for an element function with [specific fields]
 use a [string] or [regular expression]
 use a [`<label>`]
 use a [`location`]
 call the [`selector`] constructor to convert any of the above types into a selector value and use the methods below to refine it
  

Selectors are used to [apply styling rules] to elements. You can also use selectors to [query] the document for certain types of elements.
 

Furthermore, you can pass a selector to several of Typst's built-in functions to configure their behaviour. One such example is the [outline] where it can be used to change which elements are listed within the outline.
 

Multiple selectors can be combined using the methods shown below. However, not all kinds of selectors are supported in all places, at the moment.
 

## Example 
```
#context query(
  heading.where(level: 1)
    .or(heading.where(level: 2))
)

= This will be found
== So will this
=== But this will not.

```
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Turns a value into a selector. The following values are accepted:
  An element function like a `heading` or `figure`.
 A [string] or [regular expression].
 A `<label>`.
 A [`location`].
 A more complex selector like `heading.where(level: 1)`.
  selector([str][regex][label][selector][location][function]) -> [selector]  `target`   [str] or [regex] or [label] or [selector] or [location] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Can be an element function like a `heading` or `figure`, a `<label>` or a more complex selector like `heading.where(level: 1)`.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `or`

Selects all elements that match this or any of the other selectors.
 self.or([..][str][regex][label][selector][location][function]) -> [selector]  `others`   [str] or [regex] or [label] or [selector] or [location] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The other selectors to match on.
 

### `and`

Selects all elements that match this and all of the other selectors.
 self.and([..][str][regex][label][selector][location][function]) -> [selector]  `others`   [str] or [regex] or [label] or [selector] or [location] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The other selectors to match on.
 

### `before`

Returns a modified selector that will only match elements that occur before the first match of `end`.
 self.before([label][selector][location][function],[inclusive: ][bool],) -> [selector]  `end`   [label] or [selector] or [location] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The original selection will end at the first match of `end`.
 `inclusive`   [bool]    

Whether `end` itself should match or not. This is only relevant if both selectors match the same type of element. Defaults to `true`.
 

 Default: `true` 
 

### `after`

Returns a modified selector that will only match elements that occur after the first match of `start`.
 self.after([label][selector][location][function],[inclusive: ][bool],) -> [selector]  `start`   [label] or [selector] or [location] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The original selection will start at the first match of `start`.
 `inclusive`   [bool]    

Whether `start` itself should match or not. This is only relevant if both selectors match the same type of element. Defaults to `true`.
 

 Default: `true` 
 [RepresentationPrevious page] [Standard LibraryNext page]