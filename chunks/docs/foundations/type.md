---
url: https://typst.app/docs/reference/foundations/type/
category: foundations
topic: type
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Type] 
  

#  type  

Describes a kind of value.
 

To style your document, you need to work with values of different kinds: Lengths specifying the size of your elements, colors for your text and shapes, and more. Typst categorizes these into clearly defined types and tells you where it expects which type of value.
 

Apart from basic types for numeric values and [typical] [types] [known] [from] [programming] languages, Typst provides a special type for [content.] A value of this type can hold anything that you can enter into your document: Text, elements like headings and shapes, and style information.
 

## Example 
```
#let x = 10
#if type(x) == int [
  #x is an integer!
] else [
  #x is another value...
]

An image is of type
#type(image("glacier.jpg")).

```
 

The type of `10` is `int`. Now, what is the type of `int` or even `type`?
 
```
#type(int) \
#type(type)

```
 

Unlike other types like `int`, [none] and [auto] do not have a name representing them. To test if a value is one of these, compare your value to them directly, e.g:
 
```
#let val = none
#if val == none [
  Yep, it's none.
]

```
 

Note that `type` will return [`content`] for all document elements. To programmatically determine which kind of content you are dealing with, see [`content.func`].
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Determines a value's type.
   View example  
```
#type(12) \
#type(14.7) \
#type("hello") \
#type(<glacier>) \
#type([Hi]) \
#type(x => x + 1) \
#type(type)

```
   type(any) -> [type]  `value`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value whose type's to determine.
 [TargetPrevious page] [VersionNext page]