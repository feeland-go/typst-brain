---
url: https://typst.app/docs/reference/foundations/function/
category: foundations
topic: function
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Function] 
  

#  function  

A mapping from argument values to a return value.
 

You can call a function by writing a comma-separated list of function arguments enclosed in parentheses directly after the function name. Additionally, you can pass any number of trailing content block arguments to a function after the normal argument list. If the normal argument list would become empty, it can be omitted. Typst supports positional and named arguments. The former are identified by position and type, while the latter are written as `name: value`.
 

Within math mode, function calls have special behaviour. See the [math documentation] for more details.
 

## Example 
```
// Call a function.
#list([A], [B])

// Named arguments and trailing
// content blocks.
#enum(start: 2)[A][B]

// Version without parentheses.
#list[A][B]

```
 

Functions are a fundamental building block of Typst. Typst provides functions for a variety of typesetting tasks. Moreover, the markup you write is backed by functions and all styling happens through functions. This reference lists all available functions and how you can use them. Please also refer to the documentation about [set] and [show] rules to learn about additional ways you can work with functions in Typst.
 

## Element functions 

Some functions are associated with elements like [headings] or [tables]. When called, these create an element of their respective kind. In contrast to normal functions, they can further be used in [set rules], [show rules], and [selectors].
 

## Function scopes 

Functions can hold related definitions in their own scope, similar to a [module]. Examples of this are [`assert.eq`] or [`list.item`]. However, this feature is currently only available for built-in functions.
 

## Defining functions 

You can define your own function with a [let binding] that has a parameter list after the binding's name. The parameter list can contain mandatory positional parameters, named parameters with default values and [argument sinks].
 

The right-hand side of a function binding is the function body, which can be a block or any other expression. It defines the function's return value and can depend on the parameters. If the function body is a [code block], the return value is the result of joining the values of each expression in the block.
 

Within a function body, the `return` keyword can be used to exit early and optionally specify a return value. If no explicit return value is given, the body evaluates to the result of joining all expressions preceding the `return`.
 

Functions that don't return any meaningful value return [`none`] instead. The return type of such functions is not explicitly specified in the documentation. (An example of this is [`array.push`]).
 
```
#let alert(body, fill: red) = {
  set text(white)
  set align(center)
  rect(
    fill: fill,
    inset: 8pt,
    radius: 4pt,
    [*Warning:\ #body*],
  )
}

#alert[
  Danger is imminent!
]

#alert(fill: blue)[
  KEEP OFF TRACKS
]

```
 

## Importing functions 

Functions can be imported from one file ([`module`]) into another using `import`. For example, assume that we have defined the `alert` function from the previous example in a file called `foo.typ`. We can import it into another file by writing `import "foo.typ": alert`.
 

## Unnamed functions 

You can also create an unnamed function without creating a binding by specifying a parameter list followed by `=>` and the function body. If your function has just one parameter, the parentheses around the parameter list are optional. Unnamed functions are mainly useful for show rules, but also for settable properties that take functions like the page function's [`footer`] property.
 
```
#show "once?": it => [#it #it]
once?

```
 

## Note on function purity 

In Typst, all functions are pure. This means that for the same arguments, they always return the same result. They cannot "remember" things to produce another value when they are called a second time.
 

The only exception are built-in methods like [`array.push(value)`]. These can modify the values they are called on.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  

### `with`

Returns a new function that has the given arguments pre-applied.
 self.with([..]any) -> [function]  `arguments`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The arguments to apply to the function.
 

### `where`

Returns a selector that filters for elements belonging to this function whose fields have the values of the given arguments.
   View example  
```
#show heading.where(level: 2): set text(blue)
= Section
== Subsection
=== Sub-subsection

```
   self.where([..]any) -> [selector]  `fields`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The fields to filter for.
 [FloatPrevious page] [IntegerNext page]