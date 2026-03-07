---
url: https://typst.app/docs/reference/model/list/
category: model
topic: list
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Bullet List] 
  

# `list`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A bullet list.
 

Displays a sequence of items vertically, with each item introduced by a marker.
 

## Example 
```
Normal list.
- Text
- Math
- Layout
- ...

Multiple lines.
- This list item spans multiple
  lines because it is indented.

Function call.
#list(
  [Foundations],
  [Calculate],
  [Construct],
  [Data Loading],
)

```
 

## Syntax 

This functions also has dedicated syntax: Start a line with a hyphen, followed by a space to create a list item. A list item can contain multiple paragraphs and other block-level content. All content that is indented more than an item's marker becomes part of that item.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    list([tight: ][bool],[marker: ][content][array][function],[indent: ][length],[body-indent: ][length],[spacing: ][auto][length],[..][content],) -> [content]  

### `tight`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Defines the default [spacing] of the list. If it is `false`, the items are spaced apart with [paragraph spacing]. If it is `true`, they use [paragraph leading] instead. This makes the list more compact, which can look better if the items are short.
 

In markup mode, the value of this parameter is determined based on whether items are separated with a blank line. If items directly follow each other, this is set to `true`; if items are separated by a blank line, this is set to `false`. The markup-defined tightness cannot be overridden with set rules.
   View example   
```
- If a list has a lot of text, and
  maybe other inline content, it
  should not be tight anymore.

- To make a list wide, simply insert
  a blank line between the items.

```
   

 Default: `true` 
 

### `marker`   [content] or [array] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The marker which introduces each item.
 

Instead of plain content, you can also pass an array with multiple markers that should be used for nested lists. If the list nesting depth exceeds the number of markers, the markers are cycled. For total control, you may pass a function that maps the list's nesting depth (starting from `0`) to a desired marker.
   View example   
```
#set list(marker: [--])
- A more classic list
- With en-dashes

#set list(marker: ([•], [--]))
- Top-level
  - Nested
  - Items
- Items

```
   

 Default: `([•], [‣], [–])` 
 

### `indent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The indent of each item.
 

 Default: `0pt` 
 

### `body-indent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The spacing between the marker and the body of each item.
 

 Default: `0.5em` 
 

### `spacing`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The spacing between the items of the list.
 

If set to `auto`, uses paragraph [`leading`] for tight lists and paragraph [`spacing`] for wide (non-tight) lists.
 

 Default: `auto` 
 

### `children`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The bullet list's children.
 

When using the list syntax, adjacent items are automatically collected into lists, even through constructs like for loops.
   View example   
```
#for letter in "ABC" [
  - Letter #letter
]

```
   

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `item`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A bullet list item.
 list.item([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The item's body.
 [BibliographyPrevious page] [CiteNext page]