---
url: https://typst.app/docs/reference/math/equation/
category: math
topic: equation
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Equation] 
  

# `equation`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A mathematical equation.
 

Can be displayed inline with text or as a separate block. An equation becomes block-level through the presence of whitespace after the opening dollar sign and whitespace before the closing dollar sign.
 

## Example 
```
#set text(font: "New Computer Modern")

Let $a$, $b$, and $c$ be the side
lengths of right-angled triangle.
Then, we know that:
$ a^2 + b^2 = c^2 $

Prove by induction:
$ sum_(k=1)^n k = (n(n+1)) / 2 $

```
 

By default, block-level equations will not break across pages. This can be changed through `show math.equation: set block(breakable: true)`.
 

## Syntax 

This function also has dedicated syntax: Write mathematical markup within dollar signs to create an equation. Starting and ending the equation with whitespace lifts it into a separate block that is centered horizontally. For more details about math syntax, see the [main math page].

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.equation([block: ][bool],[numbering: ][none][str][function],[number-align: ][alignment],[supplement: ][none][auto][content][function],[alt: ][none][str],[content],) -> [content]  

### `block`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the equation is displayed as a separate block.
 

 Default: `false` 
 

### `numbering`   [none] or [str] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to number block-level equations. Accepts a [numbering pattern or function] taking a single number.
   View example   
```
#set math.equation(numbering: "(1)")

We define:
$ phi.alt := (1 + sqrt(5)) / 2 $ <ratio>

With @ratio, we get:
$ F_n = floor(1 / sqrt(5) phi.alt^n) $

```
   

 Default: `none` 
 

### `number-align`   [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The alignment of the equation numbering.
 

By default, the alignment is `end + horizon`. For the horizontal component, you can use `right`, `left`, or `start` and `end` of the text direction; for the vertical component, you can use `top`, `horizon`, or `bottom`.
   View example   
```
#set math.equation(numbering: "(1)", number-align: bottom)

We can calculate:
$ E &= sqrt(m_0^2 + p^2) \
    &approx 125 "GeV" $

```
   

 Default: `end + horizon` 
 

### `supplement`   [none] or [auto] or [content] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

A supplement for the equation.
 

For references to equations, this is added before the referenced number.
 

If a function is specified, it is passed the referenced equation and should return content.
   View example   
```
#set math.equation(numbering: "(1)", supplement: [Eq.])

We define:
$ phi.alt := (1 + sqrt(5)) / 2 $ <ratio>

With @ratio, we get:
$ F_n = floor(1 / sqrt(5) phi.alt^n) $

```
   

 Default: `auto` 
 

### `alt`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

An alternative description of the mathematical equation.
 

This should describe the full equation in natural language and will be made available to Assistive Technology. You can learn more in the [Textual Representations section of the Accessibility Guide].
   View example   
```
#math.equation(
  alt: "integral from 1 to infinity of a x squared plus b with respect to x",
  block: true,
  $ integral_1^oo a x^2 + b dif x $,
)

```
   

 Default: `none` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The contents of the equation.
 [ClassPrevious page] [FractionNext page]