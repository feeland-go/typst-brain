---
url: https://typst.app/docs/reference/foundations/content/
category: foundations
topic: content
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Content] 
  

#  content  

A piece of document content.
 

This type is at the heart of Typst. All markup you write and most [functions] you call produce content values. You can create a content value by enclosing markup in square brackets. This is also how you pass content to functions.
 

## Example 
```
Type of *Hello!* is
#type([*Hello!*])

```
 

Content can be added with the `+` operator, [joined together] and multiplied with integers. Wherever content is expected, you can also pass a [string] or `none`.
 

## Representation 

Content consists of elements with fields. When constructing an element with its element function, you provide these fields as arguments and when you have a content value, you can access its fields with [field access syntax].
 

Some fields are required: These must be provided when constructing an element and as a consequence, they are always available through field access on content of that type. Required fields are marked as such in the documentation.
 

Most fields are optional: Like required fields, they can be passed to the element function to configure them for a single element. However, these can also be configured with [set rules] to apply them to all elements within a scope. Optional fields are only available with field access syntax when they were explicitly passed to the element function, not when they result from a set rule.
 

Each element has a default appearance. However, you can also completely customize its appearance with a [show rule]. The show rule is passed the element. It can access the element's field and produce arbitrary content from it.
 

In the web app, you can hover over a content variable to see exactly which elements the content is composed of and what fields they have. Alternatively, you can inspect the output of the [`repr`] function.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  

### `func`

The content's element function. This function can be used to create the element contained in this content. It can be used in set and show rules for the element. Can be compared with global functions to check whether you have a specific kind of element.
 self.func() -> [function]  

### `has`

Whether the content has the specified field.
 self.has([str]) -> [bool]  `field`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The field to look for.
 

### `at`

Access the specified field on the content. Returns the default value if the field does not exist or fails with an error if no default value was specified.
 self.at([str],[default: ]any,) -> any  `field`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The field to access.
 `default`   any    

A default value to return if the field does not exist.
 

### `fields`

Returns the fields of this content.
   View example  
```
#rect(
  width: 10cm,
  height: 10cm,
).fields()

```
   self.fields() -> [dictionary]  

### `location`

The location of the content. This is only available on content returned by [query] or provided by a [show rule], for other content it will be `none`. The resulting location can be used with [counters], [state] and [queries].
 self.location() -> [none][location]  [CalculationPrevious page] [DatetimeNext page]