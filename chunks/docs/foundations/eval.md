---
url: https://typst.app/docs/reference/foundations/eval/
category: foundations
topic: eval
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Evaluate] 
  

# `eval`

Evaluates a string as Typst code.
 

This function should only be used as a last resort.
 

## Example 
```
#eval("1 + 1") \
#eval("(1, 2, 3, 4)").len() \
#eval("*Markup!*", mode: "markup") \

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  eval([str],[mode: ][str],[scope: ][dictionary],) -> any  

### `source`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A string of Typst code to evaluate.
 

### `mode`   [str]    

The [syntactical mode] in which the string is parsed.
   View example   
```
#eval("= Heading", mode: "markup")
#eval("1_2^3", mode: "math")

```
   VariantDetails`"markup"`

Evaluate as markup, as in a Typst file.
`"math"`

Evaluate as math, as in an equation.
`"code"`

Evaluate as code, as after a hash.
 

 Default: `"code"` 
 

### `scope`   [dictionary]    

A scope of definitions that are made available.
   View example   
```
#eval("x + 1", scope: (x: 2)) \
#eval(
  "abc/xyz",
  mode: "math",
  scope: (
    abc: $a + b + c$,
    xyz: $x + y + z$,
  ),
)

```
   

 Default: `(:)` 
 [DurationPrevious page] [FloatNext page]