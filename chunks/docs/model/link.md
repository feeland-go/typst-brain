---
url: https://typst.app/docs/reference/model/link/
category: model
topic: link
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Link] 
  

# `link`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Links to a URL or a location in the document.
 

By default, links do not look any different from normal text. However, you can easily apply a style of your choice with a show rule.
 

## Example 
```
#show link: underline

https://example.com \

#link("https://example.com") \
#link("https://example.com")[
  See example.com
]

```
 

## Syntax 

This function also has dedicated syntax: Text that starts with `http://` or `https://` is automatically turned into a link.
 

## Hyphenation 

If you enable hyphenation or justification, by default, it will not apply to links to prevent unwanted hyphenation in URLs. You can opt out of this default via `show link: set text(hyphenate: true)`.
 

## Accessibility 

The destination of a link should be clear from the link text itself, or at least from the text immediately surrounding it. In PDF export, Typst will automatically generate a tooltip description for links based on their destination. For links to URLs, the URL itself will be used as the tooltip.
 

## Links in HTML export 

In HTML export, a link to a [label] or [location] will be turned into a fragment link to a named anchor point. To support this, targets without an existing ID will automatically receive an ID in the DOM. How this works varies by which kind of HTML node(s) the link target turned into:
   

If the link target turned into a single HTML element, that element will receive the ID. This is, for instance, typically the case when linking to a top-level heading (which turns into a single `<h2>` element).
 
  

If the link target turned into a single text node, the node will be wrapped in a `<span>`, which will then receive the ID.
 
  

If the link target turned into multiple nodes, the first node will receive the ID.
 
  

If the link target turned into no nodes at all, an empty span will be generated to serve as a link target.
 
  

If you rely on a specific DOM structure, you should ensure that the link target turns into one or multiple elements, as the compiler makes no guarantees on the precise segmentation of text into text nodes.
 

If present, the automatic ID generation tries to reuse the link target's label to create a human-readable ID. A label can be reused if:
   

All characters are alphabetic or numeric according to Unicode, or a hyphen, or an underscore.
 
  

The label does not start with a digit or hyphen.
 
  

These rules ensure that the label is both a valid CSS identifier and a valid URL fragment for linking.
 

As IDs must be unique in the DOM, duplicate labels might need disambiguation when reusing them as IDs. The precise rules for this are as follows:
   

If a label can be reused and is unique in the document, it will directly be used as the ID.
 
  

If it's reusable, but not unique, a suffix consisting of a hyphen and an integer will be added. For instance, if the label `<mylabel>` exists twice, it would turn into `mylabel-1` and `mylabel-2`.
 
  

Otherwise, a unique ID of the form `loc-` followed by an integer will be generated.
 
 

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    link([str][label][location][dictionary],[content],) -> [content]  

### `dest`   [str] or [label] or [location] or [dictionary]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The destination the link points to.
   

To link to web pages, `dest` should be a valid URL string. If the URL is in the `mailto:` or `tel:` scheme and the `body` parameter is omitted, the email address or phone number will be the link's body, without the scheme.
 
  

To link to another part of the document, `dest` can take one of three forms:
   

A [label] attached to an element. If you also want automatic text for the link based on the element, consider using a [reference] instead.
 
  

A [`location`] (typically retrieved from [`here`], [`locate`] or [`query`]).
 
  

A dictionary with a `page` key of type [integer] and `x` and `y` coordinates of type [length]. Pages are counted from one, and the coordinates are relative to the page's top left corner.
 
  
    View example   
```
= Introduction <intro>
#link("mailto:hello@typst.app") \
#link(<intro>)[Go to intro] \
#link((page: 1, x: 0pt, y: 0pt))[
  Go to top
]

```
   

### `body`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content that should become a link.
 

If `dest` is an URL string, the parameter can be omitted. In this case, the URL will be shown as the link.
 [HeadingPrevious page] [Numbered ListNext page]