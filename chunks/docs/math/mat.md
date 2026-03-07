---
url: https://typst.app/docs/reference/math/mat/
category: math
topic: mat
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Matrix] 
  

# `mat`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A matrix.
 

The elements of a row should be separated by commas, while the rows themselves should be separated by semicolons. The semicolon syntax merges preceding arguments separated by commas into an array. You can also use this special syntax of math function calls to define custom functions that take 2D data.
 

Content in cells can be aligned with the [`align`] parameter, or content in cells that are in the same row can be aligned with the `&` symbol.
 

## Example 
```
$ mat(
  1, 2, ..., 10;
  2, 2, ..., 10;
  dots.v, dots.v, dots.down, dots.v;
  10, 10, ..., 10;
) $

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.mat([delim: ][none][str][array][symbol],[align: ][alignment],[augment: ][none][int][dictionary],[gap: ][relative],[row-gap: ][relative],[column-gap: ][relative],[..][array],) -> [content]  

### `delim`   [none] or [str] or [array] or [symbol]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The delimiter to use.
 

Can be a single character specifying the left delimiter, in which case the right delimiter is inferred. Otherwise, can be an array containing a left and a right delimiter.
   View example   
```
#set math.mat(delim: "[")
$ mat(1, 2; 3, 4) $

```
   

 Default: `("(", ")")` 
 

### `align`   [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The horizontal alignment that each cell should have.
   View example   
```
#set math.mat(align: right)
$ mat(-1, 1, 1; 1, -1, 1; 1, 1, -1) $

```
   

 Default: `center` 
 

### `augment`   [none] or [int] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Draws augmentation lines in a matrix.
  `none`: No lines are drawn.
 A single number: A vertical augmentation line is drawn after the specified column number. Negative numbers start from the end.
 A dictionary: With a dictionary, multiple augmentation lines can be drawn both horizontally and vertically. Additionally, the style of the lines can be set. The dictionary can contain the following keys:  `hline`: The offsets at which horizontal lines should be drawn. For example, an offset of `2` would result in a horizontal line being drawn after the second row of the matrix. Accepts either an integer for a single line, or an array of integers for multiple lines. Like for a single number, negative numbers start from the end.
 `vline`: The offsets at which vertical lines should be drawn. For example, an offset of `2` would result in a vertical line being drawn after the second column of the matrix. Accepts either an integer for a single line, or an array of integers for multiple lines. Like for a single number, negative numbers start from the end.
 `stroke`: How to [stroke] the line. If set to `auto`, takes on a thickness of 0.05 em and square line caps.
  
    View example: Basic usage   
```
$ mat(1, 0, 1; 0, 1, 2; augment: #2) $
// Equivalent to:
$ mat(1, 0, 1; 0, 1, 2; augment: #(-1)) $

```
      View example: Customizing the augmentation line   
```
$ mat(0, 0, 0; 1, 1, 1; augment: #(hline: 1, stroke: 2pt + green)) $

```
   

 Default: `none` 
 

### `gap`   [relative]    

The gap between rows and columns.
 

This is a shorthand to set `row-gap` and `column-gap` to the same value.
   View example   
```
#set math.mat(gap: 1em)
$ mat(1, 2; 3, 4) $

```
   

 Default: `0% + 0pt` 
 

### `row-gap`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The gap between rows.
   View example   
```
#set math.mat(row-gap: 1em)
$ mat(1, 2; 3, 4) $

```
   

 Default: `0% + 0.2em` 
 

### `column-gap`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The gap between columns.
   View example   
```
#set math.mat(column-gap: 1em)
$ mat(1, 2; 3, 4) $

```
   

 Default: `0% + 0.5em` 
 

### `rows`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

An array of arrays with the rows of the matrix.
   View example   
```
#let data = ((1, 2, 3), (4, 5, 6))
#let matrix = math.mat(..data)
$ v := matrix $

```
   [Left/RightPrevious page] [PrimesNext page]