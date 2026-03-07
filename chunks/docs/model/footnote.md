---
url: https://typst.app/docs/reference/model/footnote/
category: model
topic: footnote
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Footnote] 
  

# `footnote`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A footnote.
 

Includes additional remarks and references on the same page with footnotes. A footnote will insert a superscript number that links to the note at the bottom of the page. Notes are numbered sequentially throughout your document and can break across multiple pages.
 

To customize the appearance of the entry in the footnote listing, see [`footnote.entry`]. The footnote itself is realized as a normal superscript, so you can use a set rule on the [`super`] function to customize it. You can also apply a show rule to customize only the footnote marker (superscript number) in the running text.
 

## Example 
```
Check the docs for more details.
#footnote[https://typst.app/docs]

```
 

The footnote automatically attaches itself to the preceding word, even if there is a space before it in the markup. To force space, you can use the string `#" "` or explicit [horizontal spacing].
 

By giving a label to a footnote, you can have multiple references to it.
 
```
You can edit Typst documents online.
#footnote[https://typst.app/app] <fn>
Checkout Typst's website. @fn
And the online app. #footnote(<fn>)

```
 

Note: Set and show rules in the scope where `footnote` is called may not apply to the footnote's content. See [here] for more information.
 

## Accessibility 

Footnotes will be read by Assistive Technology (AT) immediately after the spot in the text where they are referenced, just like how they appear in markup.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    footnote([numbering: ][str][function],[label][content],) -> [content]  

### `numbering`   [str] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to number footnotes. Accepts a [numbering pattern or function] taking a single number.
 

By default, the footnote numbering continues throughout your document. If you prefer per-page footnote numbering, you can reset the footnote [counter] in the page [header]. In the future, there might be a simpler way to achieve this.
   View example   
```
#set footnote(numbering: "*")

Footnotes:
#footnote[Star],
#footnote[Dagger]

```
   

 Default: `"1"` 
 

### `body`   [label] or [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The content to put into the footnote. Can also be the label of another footnote this one should point to.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `entry`Element  Question mark    Element functions can be customized with `set` and `show` rules.   

An entry in a footnote list.
 

This function is not intended to be called directly. Instead, it is used in set and show rules to customize footnote listings.
   View example  
```
#show footnote.entry: set text(red)

My footnote listing
#footnote[It's down here]
has red text!

```
  

Note: Footnote entry properties must be uniform across each page run (a page run is a sequence of pages without an explicit pagebreak in between). For this reason, set and show rules for footnote entries should be defined before any page content, typically at the very start of the document.
 footnote.entry([content],[separator: ][content],[clearance: ][length],[gap: ][length],[indent: ][length],) -> [content]  `note`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The footnote for this entry. Its location can be used to determine the footnote counter state.
   View example   
```
#show footnote.entry: it => {
  let loc = it.note.location()
  numbering(
    "1: ",
    ..counter(footnote).at(loc),
  )
  it.note.body
}

Customized #footnote[Hello]
listing #footnote[World! 🌏]

```
   `separator`   [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The separator between the document body and the footnote listing.
   View example   
```
#set footnote.entry(
  separator: repeat[.]
)

Testing a different separator.
#footnote[
  Unconventional, but maybe
  not that bad?
]

```
   

 Default: `line(length: 30% + 0pt, stroke: 0.5pt)` 
 `clearance`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The amount of clearance between the document body and the separator.
   View example   
```
#set footnote.entry(clearance: 3em)

Footnotes also need ...
#footnote[
  ... some space to breathe.
]

```
   

 Default: `1em` 
 `gap`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The gap between footnote entries.
   View example   
```
#set footnote.entry(gap: 0.8em)

Footnotes:
#footnote[Spaced],
#footnote[Apart]

```
   

 Default: `0.5em` 
 `indent`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The indent of each footnote entry.
   View example   
```
#set footnote.entry(indent: 0em)

Footnotes:
#footnote[No],
#footnote[Indent]

```
   

 Default: `1em` 
 [FigurePrevious page] [HeadingNext page]