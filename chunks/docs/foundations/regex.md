---
url: https://typst.app/docs/reference/foundations/regex/
category: foundations
topic: regex
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Regex] 
  

#  regex  

A regular expression.
 

Can be used as a [show rule selector] and with [string methods] like `find`, `split`, and `replace`.
 

[See here] for a specification of the supported syntax.
 

## Example 
```
// Works with string methods.
#"a,b;c".split(regex("[,;]"))

// Works with show rules.
#show regex("\\d+"): set text(red)

The numbers 1 to 10.

```
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Create a regular expression from a string.
 regex([str]) -> [regex]  `regex`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The regular expression as a string.
 

Both Typst strings and regular expressions use backslashes for escaping. To produce a regex escape sequence that is also valid in Typst, you need to escape the backslash itself (e.g., writing `regex("\\\\")` for the regex `\\`). Regex escape sequences that are not valid Typst escape sequences (e.g., `\d` and `\b`) can be entered into strings directly, but it's good practice to still escape them to avoid ambiguity (i.e., `regex("\\b\\d")`). See the [list of valid string escape sequences].
 

If you need many escape sequences, you can also create a raw element and extract its text to use it for your regular expressions: `regex(`\d+\.\d+\.\d+`.text)`.
 [PluginPrevious page] [RepresentationNext page]