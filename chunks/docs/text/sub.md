---
url: https://typst.app/docs/reference/text/sub/
category: text
topic: sub
---

[  ] 
   
  [Reference] 
   
  [Text] 
   
  [Subscript] 
  

# `sub`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Renders text in subscript.
 

The text is rendered smaller and its baseline is lowered.
 

## Example 
```
Revenue#sub[yearly]

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    sub([typographic: ][bool],[baseline: ][auto][length],[size: ][auto][length],[content],) -> [content]  

### `typographic`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to use subscript glyphs from the font if available.
 

Ideally, subscripts glyphs are provided by the font (using the `subs` OpenType feature). Otherwise, Typst is able to synthesize subscripts by lowering and scaling down regular glyphs.
 

When this is set to `false`, synthesized glyphs will be used regardless of whether the font provides dedicated subscript glyphs. When `true`, synthesized glyphs may still be used in case the font does not provide the necessary subscript glyphs.
   View example   
```
N#sub(typographic: true)[1]
N#sub(typographic: false)[1]

```
   

 Default: `true` 
 

### `baseline`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The downward baseline shift for synthesized subscripts.
 

This only applies to synthesized subscripts. In other words, this has no effect if `typographic` is `true` and the font provides the necessary subscript glyphs.
 

If set to `auto`, the baseline is shifted according to the metrics provided by the font, with a fallback to `0.2em` in case the font does not define the necessary metrics.
 

 Default: `auto` 
 

### `size`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The font size for synthesized subscripts.
 

This only applies to synthesized subscripts. In other words, this has no effect if `typographic` is `true` and the font provides the necessary subscript glyphs.
 

If set to `auto`, the size is scaled according to the metrics provided by the font, with a fallback to `0.6em` in case the font does not define the necessary metrics.
 

 Default: `auto` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The text to display in subscript.
 [StrikethroughPrevious page] [SuperscriptNext page]