---
url: https://typst.app/docs/reference/layout/stack/
category: layout
topic: stack
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Stack] 
  

# `stack`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Arranges content and spacing horizontally or vertically.
 

The stack places a list of items along an axis, with optional spacing between each item.
 

## Example 
```
#stack(
  dir: ttb,
  rect(width: 40pt),
  rect(width: 120pt),
  rect(width: 90pt),
)

```
 

## Accessibility 

Stacks do not carry any special semantics. The contents of the stack are read by Assistive Technology (AT) in the order in which they have been passed to this function.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    stack([dir: ][direction],[spacing: ][none][relative][fraction],[..][relative][fraction][content],) -> [content]  

### `dir`   [direction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The direction along which the items are stacked. Possible values are:
  `ltr`: Left to right.
 `rtl`: Right to left.
 `ttb`: Top to bottom.
 `btt`: Bottom to top.
  

You can use the `start` and `end` methods to obtain the initial and final points (respectively) of a direction, as `alignment`. You can also use the `axis` method to determine whether a direction is `"horizontal"` or `"vertical"`. The `inv` method returns a direction's inverse direction.
 

For example, `ttb.start()` is `top`, `ttb.end()` is `bottom`, `ttb.axis()` is `"vertical"` and `ttb.inv()` is equal to `btt`.
 

 Default: `ttb` 
 

### `spacing`   [none] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Spacing to insert between items where no explicit spacing was provided.
 

 Default: `none` 
 

### `children`   [relative] or [fraction] or [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The children to stack along the axis.
 [Spacing (V)Previous page] [VisualizeNext page]