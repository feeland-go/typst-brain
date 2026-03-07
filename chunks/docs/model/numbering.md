---
url: https://typst.app/docs/reference/model/numbering/
category: model
topic: numbering
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Numbering] 
  

# `numbering`

Applies a numbering to a sequence of numbers.
 

A numbering defines how a sequence of numbers should be displayed as content. It is defined either through a pattern string or an arbitrary function.
 

A numbering pattern consists of counting symbols, for which the actual number is substituted, their prefixes, and one suffix. The prefixes and the suffix are displayed as-is.
 

## Example 
```
#numbering("1.1)", 1, 2, 3) \
#numbering("1.a.i", 1, 2) \
#numbering("I – 1", 12, 2) \
#numbering(
  (..nums) => nums
    .pos()
    .map(str)
    .join(".") + ")",
  1, 2, 3,
)

```
 

## Numbering patterns and numbering functions 

There are multiple instances where you can provide a numbering pattern or function in Typst. For example, when defining how to number [headings] or [figures]. Every time, the expected format is the same as the one described below for the [`numbering`] parameter.
 

The following example illustrates that a numbering function is just a regular [function] that accepts numbers and returns [`content`].
 
```
#let unary(.., last) = "|" * last
#set heading(numbering: unary)
= First heading
= Second heading
= Third heading

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  numbering([str][function],[..][int],) -> any  

### `numbering`   [str] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Defines how the numbering works.
 

Counting symbols are `1`, `a`, `A`, `i`, `I`, `α`, `Α`, `一`, `壹`, `あ`, `い`, `ア`, `イ`, `א`, `가`, `ㄱ`, `*`, `١`, `۱`, `१`, `১`, `ক`, `①`, and `⓵`. They are replaced by the number in the sequence, preserving the original case.
 

The `*` character means that symbols should be used to count, in the order of `*`, `†`, `‡`, `§`, `¶`, `‖`. If there are more than six items, the number is represented using repeated symbols.
 

Suffixes are all characters after the last counting symbol. They are displayed as-is at the end of any rendered number.
 

Prefixes are all characters that are neither counting symbols nor suffixes. They are displayed as-is at in front of their rendered equivalent of their counting symbol.
 

This parameter can also be an arbitrary function that gets each number as an individual argument. When given a function, the `numbering` function just forwards the arguments to that function. While this is not particularly useful in itself, it means that you can just give arbitrary numberings to the `numbering` function without caring whether they are defined as a pattern or function.
 

### `numbers`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The numbers to apply the numbering to. Must be non-negative.
 

In general, numbers are counted from one. A number of zero indicates that the first element has not yet appeared.
 

If `numbering` is a pattern and more numbers than counting symbols are given, the last counting symbol with its prefix is repeated.
 [Numbered ListPrevious page] [OutlineNext page]