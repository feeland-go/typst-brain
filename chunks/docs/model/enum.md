---
url: https://typst.app/docs/reference/model/enum/
category: model
topic: enum
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Numbered List] 
  

# `enum`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A numbered list.
 

Displays a sequence of items vertically and numbers them consecutively.
 

## Example 
```
Automatically numbered:
+ Preparations
+ Analysis
+ Conclusions

Manually numbered:
2. What is the first step?
5. I am confused.
+  Moving on ...

Multiple lines:
+ This enum item has multiple
  lines because the next line
  is indented.

Function call.
#enum[First][Second]

```
 

You can easily switch all your enumerations to a different numbering style with a set rule.
 
```
#set enum(numbering: "a)")

+ Starting off ...
+ Don't forget step two

```
 

You can also use [`enum.item`] to programmatically customize the number of each item in the enumeration:
 
```
#enum(
  enum.item(1)[First step],
  enum.item(5)[Fifth step],
  enum.item(10)[Tenth step]
)

```
 

## Syntax 

This functions also has dedicated syntax:
  Starting a line with a plus sign creates an automatically numbered enumeration item.
 Starting a line with a number followed by a dot creates an explicitly numbered enumeration item.
  

Enumeration items can contain multiple paragraphs and other block-level content. All content that is indented more than an item's marker becomes part of that item.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    enum([tight: ][bool],[numbering: ][str][function],[start: ][auto][int],[full: ][bool],[reversed: ][bool],[indent: ][length],[body-indent: ][length],[spacing: ][auto][length],[number-align: ][alignment],[..][content][array],) -> [content]  

### `tight`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Defines the default [spacing] of the enumeration. If it is `false`, the items are spaced apart with [paragraph spacing]. If it is `true`, they use [paragraph leading] instead. This makes the list more compact, which can look better if the items are short.
 

In markup mode, the value of this parameter is determined based on whether items are separated with a blank line. If items directly follow each other, this is set to `true`; if items are separated by a blank line, this is set to `false`. The markup-defined tightness cannot be overridden with set rules.
   View example   
```
+ If an enum has a lot of text, and
  maybe other inline content, it
  should not be tight anymore.

+ To make an enum wide, simply
  insert a blank line between the
  items.

```
   

 Default: `true` 
 

### `numbering`   [str] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to number the enumeration. Accepts a [numbering pattern or function].
 

If the numbering pattern contains multiple counting symbols, they apply to nested enums. If given a function, the function receives one argument if `full` is `false` and multiple arguments if `full` is `true`.
   View example   
```
#set enum(numbering: "1.a)")
+ Different
+ Numbering
  + Nested
  + Items
+ Style

#set enum(numbering: n => super[#n])
+ Superscript
+ Numbering!

```
   

 Default: `"1."` 
 

### `start`   [auto] or [int]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Which number to start the enumeration with.
   View example   
```
#enum(
  start: 3,
  [Skipping],
  [Ahead],
)

```
   

 Default: `auto` 
 

### `full`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to display the full numbering, including the numbers of all parent enumerations.
   View example   
```
#set enum(numbering: "1.a)", full: true)
+ Cook
  + Heat water
  + Add ingredients
+ Eat

```
   

 Default: `false` 
 

### `reversed`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to reverse the numbering for this enumeration.
   View example   
```
#set enum(reversed: true)
+ Coffee
+ Tea
+ Milk

```
   

 Default: `false` 
 

### `indent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The indentation of each item.
 

 Default: `0pt` 
 

### `body-indent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The space between the numbering and the body of each item.
 

 Default: `0.5em` 
 

### `spacing`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The spacing between the items of the enumeration.
 

If set to `auto`, uses paragraph [`leading`] for tight enumerations and paragraph [`spacing`] for wide (non-tight) enumerations.
 

 Default: `auto` 
 

### `number-align`   [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The alignment that enum numbers should have.
 

By default, this is set to `end + top`, which aligns enum numbers towards end of the current text direction (in left-to-right script, for example, this is the same as `right`) and at the top of the line. The choice of `end` for horizontal alignment of enum numbers is usually preferred over `start`, as numbers then grow away from the text instead of towards it, avoiding certain visual issues. This option lets you override this behaviour, however. (Also to note is that the [unordered list] uses a different method for this, by giving the `marker` content an alignment directly.).
   View example   
```
#set enum(number-align: start + bottom)

Here are some powers of two:
1. One
2. Two
4. Four
8. Eight
16. Sixteen
32. Thirty two

```
   

 Default: `end + top` 
 

### `children`   [content] or [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The numbered list's items.
 

When using the enum syntax, adjacent items are automatically collected into enumerations, even through constructs like for loops.
   View example   
```
#for phase in (
   "Launch",
   "Orbit",
   "Descent",
) [+ #phase]

```
   

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `item`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

An enumeration item.
 enum.item([][auto][int],[content],) -> [content]  `number`   [auto] or [int]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The item's number.
 

 Default: `auto` 
 `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The item's body.
 [LinkPrevious page] [NumberingNext page]