---
url: https://typst.app/docs/reference/math/accent/
category: math
topic: accent
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Accent] 
  

# `accent`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Attaches an accent to a base.
 

## Example 
```
$grave(a) = accent(a, `)$ \
$arrow(a) = accent(a, arrow)$ \
$tilde(a) = accent(a, \u{0303})$

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.accent([content],[str][content],[size: ][relative],[dotless: ][bool],) -> [content]  

### `base`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The base to which the accent is applied. May consist of multiple letters.
   View example   
```
$arrow(A B C)$

```
   

### `accent`   [str] or [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The accent to apply to the base.
 

Supported accents include:
 AccentNameCodepoint Grave`grave```` Acute`acute``´` Circumflex`hat``^` Tilde`tilde``~` Macron`macron``¯` Dash`dash``‾` Breve`breve``˘` Dot`dot``.` Double dot, Diaeresis`dot.double`, `diaer``¨` Triple dot`dot.triple``⃛` Quadruple dot`dot.quad``⃜` Circle`circle``∘` Double acute`acute.double``˝` Caron`caron``ˇ` Right arrow`arrow`, `->``→` Left arrow`arrow.l`, `<-``←` Left/Right arrow`arrow.l.r``↔` Right harpoon`harpoon``⇀` Left harpoon`harpoon.lt``↼`  

### `size`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The size of the accent, relative to the width of the base.
   View example   
```
$dash(A, size: #150%)$

```
   

 Default: `100% + 0pt` 
 

### `dotless`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to remove the dot on top of lowercase i and j when adding a top accent.
 

This enables the `dtls` OpenType feature.
   View example   
```
$hat(dotless: #false, i)$

```
   

 Default: `true` 
 [MathPrevious page] [AttachNext page]