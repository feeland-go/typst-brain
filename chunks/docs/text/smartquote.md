---
url: https://typst.app/docs/reference/text/smartquote/
category: text
topic: smartquote
---

[  ] 
   
  [Reference] 
   
  [Text] 
   
  [Smartquote] 
  

# `smartquote`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A language-aware quote that reacts to its context.
 

Automatically turns into an appropriate opening or closing quote based on the active [text language].
 

## Example 
```
"This is in quotes."

#set text(lang: "de")
"Das ist in Anführungszeichen."

#set text(lang: "fr")
"C'est entre guillemets."

```
 

## Syntax 

This function also has dedicated syntax: The normal quote characters (`'` and `"`). Typst automatically makes your quotes smart.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    smartquote([double: ][bool],[enabled: ][bool],[alternative: ][bool],[quotes: ][auto][str][array][dictionary],) -> [content]  

### `double`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether this should be a double quote.
 

 Default: `true` 
 

### `enabled`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether smart quotes are enabled.
 

To disable smartness for a single quote, you can also escape it with a backslash.
   View example   
```
#set smartquote(enabled: false)

These are "dumb" quotes.

```
   

 Default: `true` 
 

### `alternative`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to use alternative quotes.
 

Does nothing for languages that don't have alternative quotes, or if explicit quotes were set.
   View example   
```
#set text(lang: "de")
#set smartquote(alternative: true)

"Das ist in anderen Anführungszeichen."

```
   

 Default: `false` 
 

### `quotes`   [auto] or [str] or [array] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The quotes to use.
  When set to `auto`, the appropriate single quotes for the [text language] will be used. This is the default.
 Custom quotes can be passed as a string, array, or dictionary of either  [string]: a string consisting of two characters containing the opening and closing double quotes (characters here refer to Unicode grapheme clusters)
 [array]: an array containing the opening and closing double quotes
 [dictionary]: a dictionary containing the double and single quotes, each specified as either `auto`, string, or array
  
    View example   
```
#set text(lang: "de")
'Das sind normale Anführungszeichen.'

#set smartquote(quotes: "()")
"Das sind eigene Anführungszeichen."

#set smartquote(quotes: (single: ("[[", "]]"),  double: auto))
'Das sind eigene Anführungszeichen.'

```
   

 Default: `auto` 
 [Small CapitalsPrevious page] [StrikethroughNext page]