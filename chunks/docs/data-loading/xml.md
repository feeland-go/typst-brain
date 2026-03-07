---
url: https://typst.app/docs/reference/data-loading/xml/
category: data-loading
topic: xml
---

[  ] 
   
  [Reference] 
   
  [Data Loading] 
   
  [XML] 
  

# `xml`

Reads structured data from an XML file.
 

The XML file is parsed into an array of dictionaries and strings. XML nodes can be elements or strings. Elements are represented as dictionaries with the following keys:
  `tag`: The name of the element as a string.
 `attrs`: A dictionary of the element's attributes as strings.
 `children`: An array of the element's child nodes.
  

The XML file in the example contains a root `news` tag with multiple `article` tags. Each article has a `title`, `author`, and `content` tag. The `content` tag contains one or more paragraphs, which are represented as `p` tags.
 

## Example 
```
#let find-child(elem, tag) = {
  elem.children
    .find(e => "tag" in e and e.tag == tag)
}

#let article(elem) = {
  let title = find-child(elem, "title")
  let author = find-child(elem, "author")
  let pars = find-child(elem, "content")

  [= #title.children.first()]
  text(10pt, weight: "medium")[
    Published by
    #author.children.first()
  ]

  for p in pars.children {
    if type(p) == dictionary {
      parbreak()
      p.children.first()
    }
  }
}

#let data = xml("example.xml")
#for elem in data.first().children {
  if type(elem) == dictionary {
    article(elem)
  }
}

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  xml([str][bytes]) -> any  

### `source`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A [path] to an XML file or raw XML bytes.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `decode` Warning  `xml.decode` is deprecated, directly pass bytes to `xml` instead; it will be removed in Typst 0.15.0

Reads structured data from an XML string/bytes.
 xml.decode([str][bytes]) -> any  `data`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

XML data.
 [TOMLPrevious page] [YAMLNext page]