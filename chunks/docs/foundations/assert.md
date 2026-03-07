---
url: https://typst.app/docs/reference/foundations/assert/
category: foundations
topic: assert
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Assert] 
  

# `assert`

Ensures that a condition is fulfilled.
 

Fails with an error if the condition is not fulfilled. Does not produce any output in the document.
 

If you wish to test equality between two values, see [`assert.eq`] and [`assert.ne`].
 

## Example 
```
#assert(1 < 2, message: "math broke")

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  assert([bool],[message: ][str],)  

### `condition`   [bool]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The condition that must be true for the assertion to pass.
 

### `message`   [str]    

The error message when the assertion fails.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `eq`

Ensures that two values are equal.
 

Fails with an error if the first value is not equal to the second. Does not produce any output in the document.
   View example  
```
#assert.eq(10, 10)

```
   assert.eq(any,any,[message: ][str],)  `left`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The first value to compare.
 `right`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The second value to compare.
 `message`   [str]    

An optional message to display on error instead of the representations of the compared values.
 

### `ne`

Ensures that two values are not equal.
 

Fails with an error if the first value is equal to the second. Does not produce any output in the document.
   View example  
```
#assert.ne(3, 4)

```
   assert.ne(any,any,[message: ][str],)  `left`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The first value to compare.
 `right`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The second value to compare.
 `message`   [str]    

An optional message to display on error instead of the representations of the compared values.
 [ArrayPrevious page] [AutoNext page]