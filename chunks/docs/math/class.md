---
url: https://typst.app/docs/reference/math/class/
category: math
topic: class
---

[  ] 
   
  [Reference] 
   
  [Math] 
   
  [Class] 
  

# `class`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Forced use of a certain math class.
 

This is useful to treat certain symbols as if they were of a different class, e.g. to make a symbol behave like a relation. The class of a symbol defines the way it is laid out, including spacing around it, and how its scripts are attached by default. Note that the latter can always be overridden using [`limits`] and [`scripts`].
 

## Example 
```
#let loves = math.class(
  "relation",
  sym.suit.heart,
)

$x loves y and y loves 5$

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    math.class([str],[content],) -> [content]  

### `class`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The class to apply to the content.
    View options   VariantDetails`"normal"`

The default class for non-special things.
`"punctuation"`

Punctuation, e.g. a comma.
`"opening"`

An opening delimiter, e.g. `(`.
`"closing"`

A closing delimiter, e.g. `)`.
`"fence"`

A delimiter that is the same on both sides, e.g. `|`.
`"large"`

A large operator like `sum`.
`"relation"`

A relation like `=` or `prec`.
`"unary"`

A unary operator like `not`.
`"binary"`

A binary operator like `times`.
`"vary"`

An operator that can be both unary or binary like `+`.
   

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to which the class is applied.
 [CasesPrevious page] [EquationNext page]