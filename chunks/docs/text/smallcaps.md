---
url: https://typst.app/docs/reference/text/smallcaps/
category: text
topic: smallcaps
---

[  ] 
   
  [Reference] 
   
  [Text] 
   
  [Small Capitals] 
  

# `smallcaps`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Displays text in small capitals.
 

## Example 
```
Hello \
#smallcaps[Hello]

```
 

## Smallcaps fonts 

By default, this uses the `smcp` and `c2sc` OpenType features on the font. Not all fonts support these features. Sometimes, smallcaps are part of a dedicated font. This is, for example, the case for the Latin Modern family of fonts. In those cases, you can use a show-set rule to customize the appearance of the text in smallcaps:
 
```
#show smallcaps: set text(font: "Latin Modern Roman Caps")

```
 

In the future, this function will support synthesizing smallcaps from normal letters, but this is not yet implemented.
 

## Smallcaps headings 

You can use a [show rule] to apply smallcaps formatting to all your headings. In the example below, we also center-align our headings and disable the standard bold font.
 
```
#set par(justify: true)
#set heading(numbering: "I.")

#show heading: smallcaps
#show heading: set align(center)
#show heading: set text(
  weight: "regular"
)

= Introduction
#lorem(40)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    smallcaps([all: ][bool],[content],) -> [content]  

### `all`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to turn uppercase letters into small capitals as well.
 

Unless overridden by a show rule, this enables the `c2sc` OpenType feature.
   View example   
```
#smallcaps(all: true)[UNICEF] is an
agency of #smallcaps(all: true)[UN].

```
   

 Default: `false` 
 

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to display in small capitals.
 [Raw Text / CodePrevious page] [SmartquoteNext page]