---
url: https://typst.app/docs/reference/html/elem/
category: html
topic: elem
---

[  ] 
   
  [Reference] 
   
  [HTML] 
   
  [Elem] 
  

# `elem`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

An HTML element that can contain Typst content.
 

Typst's HTML export automatically generates the appropriate tags for most elements. However, sometimes, it is desirable to retain more control. For example, when using Typst to generate your blog, you could use this function to wrap each article in an `<article>` tag.
 

Typst is aware of what is valid HTML. A tag and its attributes must form syntactically valid HTML. Some tags, like `meta` do not accept content. Hence, you must not provide a body for them. We may add more checks in the future, so be sure that you are generating valid HTML when using this function.
 

Normally, Typst will generate `html`, `head`, and `body` tags for you. If you instead create them with this function, Typst will omit its own tags.
 
```
#html.elem("div", attrs: (style: "background: aqua"))[
  A div with _Typst content_ inside!
]

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    html.elem([str],[attrs: ][dictionary],[][none][content],) -> [content]  

### `tag`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The element's tag.
 

### `attrs`   [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The element's HTML attributes.
 

 Default: `(:)` 
 

### `body`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The contents of the HTML element.
 

The body can be arbitrary Typst content.
 

 Default: `none` 
 [HTMLPrevious page] [FrameNext page]