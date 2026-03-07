---
url: https://typst.app/docs/reference/math/sizes/
category: math
topic: sizes
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Sizes] 
  

# Sizes 

Forced size styles for expressions within formulas.
 

These functions allow manual configuration of the size of equation elements to make them look as in a display/inline equation or as if used in a root or sub/superscripts.
 

## Functions 

### `display`

Forced display style in math.
 

This is the normal size for block equations.
   View example  
```
$sum_i x_i/2 = display(sum_i x_i/2)$

```
   math.display([content],[cramped: ][bool],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);    

The content to size.
 `cramped`   [bool]    

Whether to impose a height restriction for exponents, like regular sub- and superscripts do.
 

 Default: `false` 
 

### `inline`

Forced inline (text) style in math.
 

This is the normal size for inline equations.
   View example  
```
$ sum_i x_i/2
    = inline(sum_i x_i/2) $

```
   math.inline([content],[cramped: ][bool],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to size.
 `cramped`   [bool]    

Whether to impose a height restriction for exponents, like regular sub- and superscripts do.
 

 Default: `false` 
 

### `script`

Forced script style in math.
 

This is the smaller size used in powers or sub- or superscripts.
   View example  
```
$sum_i x_i/2 = script(sum_i x_i/2)$

```
   math.script([content],[cramped: ][bool],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to size.
 `cramped`   [bool]    

Whether to impose a height restriction for exponents, like regular sub- and superscripts do.
 

 Default: `true` 
 

### `sscript`

Forced second script style in math.
 

This is the smallest size, used in second-level sub- and superscripts (script of the script).
   View example  
```
$sum_i x_i/2 = sscript(sum_i x_i/2)$

```
   math.sscript([content],[cramped: ][bool],) -> [content]  `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to size.
 `cramped`   [bool]    

Whether to impose a height restriction for exponents, like regular sub- and superscripts do.
 

 Default: `true` 
 [RootsPrevious page] [StretchNext page]