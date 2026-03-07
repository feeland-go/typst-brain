---
url: https://typst.app/docs/reference/math/attach/
category: math
topic: attach
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Attach] 
  

# Attach 

Subscript, superscripts, and limits.
 

Attachments can be displayed either as sub/superscripts, or limits. Typst automatically decides which is more suitable depending on the base, but you can also control this manually with the `scripts` and `limits` functions.
 

If you want the base to stretch to fit long top and bottom attachments (for example, an arrow with text above it), use the [`stretch`] function.
 

## Example 
```
$ sum_(i=0)^n a_i = 2^(1+i) $

```
 

## Syntax 

This function also has dedicated syntax for attachments after the base: Use the underscore (`_`) to indicate a subscript i.e. bottom attachment and the hat (`^`) to indicate a superscript i.e. top attachment.
 

## Functions 

### `attach`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A base with optional attachments.
   View example  
```
$ attach(
  Pi, t: alpha, b: beta,
  tl: 1, tr: 2+3, bl: 4+5, br: 6,
) $

```
   math.attach([content],[t: ][none][content],[b: ][none][content],[tl: ][none][content],[bl: ][none][content],[tr: ][none][content],[br: ][none][content],) -> [content]  `base`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The base to which things are attached.
 `t`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The top attachment, smartly positioned at top-right or above the base.
 

You can wrap the base in `limits()` or `scripts()` to override the smart positioning.
 

 Default: `none` 
 `b`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The bottom attachment, smartly positioned at the bottom-right or below the base.
 

You can wrap the base in `limits()` or `scripts()` to override the smart positioning.
 

 Default: `none` 
 `tl`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The top-left attachment (before the base).
 

 Default: `none` 
 `bl`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The bottom-left attachment (before base).
 

 Default: `none` 
 `tr`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The top-right attachment (after the base).
 

 Default: `none` 
 `br`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The bottom-right attachment (after the base).
 

 Default: `none` 
 

### `scripts`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Forces a base to display attachments as scripts.
   View example  
```
$ scripts(sum)_1^2 != sum_1^2 $

```
   math.scripts([content]) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The base to attach the scripts to.
 

### `limits`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

Forces a base to display attachments as limits.
   View example  
```
$ limits(A)_1^2 != A_1^2 $

```
   math.limits([content],[inline: ][bool],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The base to attach the limits to.
 `inline`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to also force limits in inline equations.
 

When applying limits globally (e.g., through a show rule), it is typically a good idea to disable this.
 

 Default: `true` 
 [AccentPrevious page] [BinomialNext page]