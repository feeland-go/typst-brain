---
url: https://typst.app/docs/reference/model/terms/
category: model
topic: terms
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Term List] 
  

# `terms`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A list of terms and their descriptions.
 

Displays a sequence of terms and their descriptions vertically. When the descriptions span over multiple lines, they use hanging indent to communicate the visual hierarchy.
 

## Example 
```
/ Ligature: A merged glyph.
/ Kerning: A spacing adjustment
  between two adjacent letters.

```
 

## Syntax 

This function also has dedicated syntax: Starting a line with a slash, followed by a term, a colon and a description creates a term list item.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    terms([tight: ][bool],[separator: ][content],[indent: ][length],[hanging-indent: ][length],[spacing: ][auto][length],[..][content][array],) -> [content]  

### `tight`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Defines the default [spacing] of the term list. If it is `false`, the items are spaced apart with [paragraph spacing]. If it is `true`, they use [paragraph leading] instead. This makes the list more compact, which can look better if the items are short.
 

In markup mode, the value of this parameter is determined based on whether items are separated with a blank line. If items directly follow each other, this is set to `true`; if items are separated by a blank line, this is set to `false`. The markup-defined tightness cannot be overridden with set rules.
   View example   
```
/ Fact: If a term list has a lot
  of text, and maybe other inline
  content, it should not be tight
  anymore.

/ Tip: To make it wide, simply
  insert a blank line between the
  items.

```
   

 Default: `true` 
 

### `separator`   [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The separator between the item and the description.
 

If you want to just separate them with a certain amount of space, use `h(2cm, weak: true)` as the separator and replace `2cm` with your desired amount of space.
   View example   
```
#set terms(separator: [: ])

/ Colon: A nice separator symbol.

```
   

 Default: `h(amount: 0.6em, weak: true)` 
 

### `indent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The indentation of each item.
 

 Default: `0pt` 
 

### `hanging-indent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The hanging indent of the description.
 

This is in addition to the whole item's `indent`.
   View example   
```
#set terms(hanging-indent: 0pt)
/ Term: This term list does not
  make use of hanging indents.

```
   

 Default: `2em` 
 

### `spacing`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The spacing between the items of the term list.
 

If set to `auto`, uses paragraph [`leading`] for tight term lists and paragraph [`spacing`] for wide (non-tight) term lists.
 

 Default: `auto` 
 

### `children`   [content] or [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The term list's children.
 

When using the term list syntax, adjacent items are automatically collected into term lists, even through constructs like for loops.
   View example   
```
#for (year, product) in (
  "1978": "TeX",
  "1984": "LaTeX",
  "2019": "Typst",
) [/ #product: Born in #year.]

```
   

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `item`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

A term list item.
 terms.item([content],[content],) -> [content]  `term`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The term described by the list item.
 `description`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The description of the term.
 [TablePrevious page] [TitleNext page]