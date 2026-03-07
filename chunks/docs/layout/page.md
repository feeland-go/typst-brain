---
url: https://typst.app/docs/reference/layout/page/
category: layout
topic: page
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Page] 
  

# `page`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Layouts its child onto one or multiple pages.
 

Although this function is primarily used in set rules to affect page properties, it can also be used to explicitly render its argument onto a set of pages of its own.
 

Pages can be set to use `auto` as their width or height. In this case, the pages will grow to fit their content on the respective axis.
 

The [Guide for Page Setup] explains how to use this and related functions to set up a document with many examples.
 

## Example 
```
#set page("us-letter")

There you go, US friends!

```
 

## Accessibility 

The contents of the page's header, footer, foreground, and background are invisible to Assistive Technology (AT) like screen readers. Only the body of the page is read by AT. Do not include vital information not included elsewhere in the document in these areas.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    page([paper: ][str],[width: ][auto][length],[height: ][auto][length],[flipped: ][bool],[margin: ][auto][relative][dictionary],[binding: ][auto][alignment],[columns: ][int],[fill: ][none][auto][color][gradient][tiling],[numbering: ][none][str][function],[supplement: ][none][auto][content],[number-align: ][alignment],[header: ][none][auto][content],[header-ascent: ][relative],[footer: ][none][auto][content],[footer-descent: ][relative],[background: ][none][content],[foreground: ][none][content],[body: ][content],) -> [content]  

### `paper`   [str]    

A standard paper size to set width and height.
 

This is just a shorthand for setting `width` and `height` and, as such, cannot be retrieved in a context expression.
    View options     

 Default: `"a4"` 
    View paper sizes   `"a0"` , `"a1"` , `"a2"` , `"a3"` , `"a4"` , `"a5"` , `"a6"` , `"a7"` , `"a8"` , `"a9"` , `"a10"` , `"a11"` , `"iso-b1"` , `"iso-b2"` , `"iso-b3"` , `"iso-b4"` , `"iso-b5"` , `"iso-b6"` , `"iso-b7"` , `"iso-b8"` , `"iso-c3"` , `"iso-c4"` , `"iso-c5"` , `"iso-c6"` , `"iso-c7"` , `"iso-c8"` , `"din-d3"` , `"din-d4"` , `"din-d5"` , `"din-d6"` , `"din-d7"` , `"din-d8"` , `"sis-g5"` , `"sis-e5"` , `"ansi-a"` , `"ansi-b"` , `"ansi-c"` , `"ansi-d"` , `"ansi-e"` , `"arch-a"` , `"arch-b"` , `"arch-c"` , `"arch-d"` , `"arch-e1"` , `"arch-e"` , `"jis-b0"` , `"jis-b1"` , `"jis-b2"` , `"jis-b3"` , `"jis-b4"` , `"jis-b5"` , `"jis-b6"` , `"jis-b7"` , `"jis-b8"` , `"jis-b9"` , `"jis-b10"` , `"jis-b11"` , `"sac-d0"` , `"sac-d1"` , `"sac-d2"` , `"sac-d3"` , `"sac-d4"` , `"sac-d5"` , `"sac-d6"` , `"iso-id-1"` , `"iso-id-2"` , `"iso-id-3"` , `"asia-f4"` , `"jp-shiroku-ban-4"` , `"jp-shiroku-ban-5"` , `"jp-shiroku-ban-6"` , `"jp-kiku-4"` , `"jp-kiku-5"` , `"jp-business-card"` , `"cn-business-card"` , `"eu-business-card"` , `"fr-tellière"` , `"fr-couronne-écriture"` , `"fr-couronne-édition"` , `"fr-raisin"` , `"fr-carré"` , `"fr-jésus"` , `"uk-brief"` , `"uk-draft"` , `"uk-foolscap"` , `"uk-quarto"` , `"uk-crown"` , `"uk-book-a"` , `"uk-book-b"` , `"us-letter"` , `"us-legal"` , `"us-tabloid"` , `"us-executive"` , `"us-foolscap-folio"` , `"us-statement"` , `"us-ledger"` , `"us-oficio"` , `"us-gov-letter"` , `"us-gov-legal"` , `"us-business-card"` , `"us-digest"` , `"us-trade"` , `"newspaper-compact"` , `"newspaper-berliner"` , `"newspaper-broadsheet"` , `"presentation-16-9"` , `"presentation-4-3"`   

### `width`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The width of the page.
   View example   
```
#set page(
  width: 3cm,
  margin: (x: 0cm),
)

#for i in range(3) {
  box(square(width: 1cm))
}

```
   

 Default: `595.28pt` 
 

### `height`   [auto] or [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The height of the page.
 

If this is set to `auto`, page breaks can only be triggered manually by inserting a [page break] or by adding another non-empty page set rule. Most examples throughout this documentation use `auto` for the height of the page to dynamically grow and shrink to fit their content.
 

 Default: `841.89pt` 
 

### `flipped`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the page is flipped into landscape orientation.
   View example   
```
#set page(
  "us-business-card",
  flipped: true,
  fill: rgb("f2e5dd"),
)

#set align(bottom + end)
#text(14pt)[*Sam H. Richards*] \
_Procurement Manager_

#set text(10pt)
17 Main Street \
New York, NY 10001 \
+1 555 555 5555

```
   

 Default: `false` 
 

### `margin`   [auto] or [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The page's margins.
  `auto`: The margins are set automatically to 2.5/21 times the smaller dimension of the page. This results in 2.5 cm margins for an A4 page.
 A single length: The same margin on all sides.
 A dictionary: With a dictionary, the margins can be set individually. The dictionary can contain the following keys in order of precedence:  `top`: The top margin.
 `right`: The right margin.
 `bottom`: The bottom margin.
 `left`: The left margin.
 `inside`: The margin at the inner side of the page (where the [binding] is).
 `outside`: The margin at the outer side of the page (opposite to the [binding]).
 `x`: The horizontal margins.
 `y`: The vertical margins.
 `rest`: The margins on all sides except those for which the dictionary explicitly sets a size.
  
  

All keys are optional; omitted keys will use their previously set value, or the default margin if never set. In addition, the values for `left` and `right` are mutually exclusive with the values for `inside` and `outside`.
   View example   
```
#set page(
 width: 3cm,
 height: 4cm,
 margin: (x: 8pt, y: 4pt),
)

#rect(
  width: 100%,
  height: 100%,
  fill: aqua,
)

```
   

 Default: `auto` 
 

### `binding`   [auto] or [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

On which side the pages will be bound.
  `auto`: Equivalent to `left` if the [text direction] is left-to-right and `right` if it is right-to-left.
 `left`: Bound on the left side.
 `right`: Bound on the right side.
  

This affects the meaning of the `inside` and `outside` options for margins.
 

 Default: `auto` 
 

### `columns`   [int]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How many columns the page has.
 

If you need to insert columns into a page or other container, you can also use the [`columns` function].
   View example   
```
#set page(columns: 2, height: 4.8cm)
Climate change is one of the most
pressing issues of our time, with
the potential to devastate
communities, ecosystems, and
economies around the world. It's
clear that we need to take urgent
action to reduce our carbon
emissions and mitigate the impacts
of a rapidly changing climate.

```
   

 Default: `1` 
 

### `fill`   [none] or [auto] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The page's background fill.
 

Setting this to something non-transparent instructs the printer to color the complete page. If you are considering larger production runs, it may be more environmentally friendly and cost-effective to source pre-dyed pages and not set this property.
 

When set to `none`, the background becomes transparent. Note that PDF pages will still appear with a (usually white) background in viewers, but they are actually transparent. (If you print them, no color is used for the background.)
 

The default of `auto` results in `none` for PDF output, and `white` for PNG and SVG.
   View example   
```
#set page(fill: rgb("444352"))
#set text(fill: rgb("fdfdfd"))
*Dark mode enabled.*

```
   

 Default: `auto` 
 

### `numbering`   [none] or [str] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to number the pages. You can refer to the Page Setup Guide for [customizing page numbers].
 

Accepts a [numbering pattern or function] taking one or two numbers:
  The first number is the current page number.
 The second number is the total number of pages. In a numbering pattern, the second number can be omitted. If a function is passed, it will receive one argument in the context of links or references, and two arguments when producing the visible page numbers.
  

These are logical numbers controlled by the page counter, and may thus not match the physical numbers. Specifically, they are the [current] and the [final] value of `counter(page)`. See the [`counter`] documentation for more details.
 

If an explicit [`footer`] (or [`header`] for [top-aligned] numbering) is given, the numbering is ignored.
   View example   
```
#set page(
  height: 100pt,
  margin: (top: 16pt, bottom: 24pt),
  numbering: "1 / 1",
)

#lorem(48)

```
    

 Default: `none` 
 

### `supplement`   [none] or [auto] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

A supplement for the pages.
 

For page references, this is added before the page number.
   View example   
```
#set page(numbering: "1.", supplement: [p.])

= Introduction <intro>
We are on #ref(<intro>, form: "page")!

```
   

 Default: `auto` 
 

### `number-align`   [alignment]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The alignment of the page numbering.
 

If the vertical component is `top`, the numbering is placed into the header and if it is `bottom`, it is placed in the footer. Horizon alignment is forbidden. If an explicit matching `header` or `footer` is given, the numbering is ignored.
   View example   
```
#set page(
  margin: (top: 16pt, bottom: 24pt),
  numbering: "1",
  number-align: right,
)

#lorem(30)

```
   

 Default: `center + bottom` 
 

### `header`   [none] or [auto] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The page's header. Fills the top margin of each page.
  Content: Shows the content as the header.
 `auto`: Shows the page number if a [`numbering`] is set and [`number-align`] is `top`.
 `none`: Suppresses the header.
    View example   
```
#set par(justify: true)
#set page(
  margin: (top: 32pt, bottom: 20pt),
  header: [
    #set text(8pt)
    #smallcaps[Typst Academy]
    #h(1fr) _Exercise Sheet 3_
  ],
)

#lorem(19)

```
   

 Default: `auto` 
 

### `header-ascent`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The amount the header is raised into the top margin.
 

 Default: `30% + 0pt` 
 

### `footer`   [none] or [auto] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The page's footer. Fills the bottom margin of each page.
  Content: Shows the content as the footer.
 `auto`: Shows the page number if a [`numbering`] is set and [`number-align`] is `bottom`.
 `none`: Suppresses the footer.
  

For just a page number, the `numbering` property typically suffices. If you want to create a custom footer but still display the page number, you can directly access the [page counter].
   View example   
```
#set par(justify: true)
#set page(
  height: 100pt,
  margin: 20pt,
  footer: context [
    #set align(right)
    #set text(8pt)
    #counter(page).display(
      "1 of I",
      both: true,
    )
  ]
)

#lorem(48)

```
    

 Default: `auto` 
 

### `footer-descent`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The amount the footer is lowered into the bottom margin.
 

 Default: `30% + 0pt` 
 

### `background`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Content in the page's background.
 

This content will be placed behind the page's body. It can be used to place a background image or a watermark.
   View example   
```
#set page(background: rotate(24deg,
  text(18pt, fill: rgb("FFCBC4"))[
    *CONFIDENTIAL*
  ]
))

= Typst's secret plans
In the year 2023, we plan to take
over the world (of typesetting).

```
   

 Default: `none` 
 

### `foreground`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Content in the page's foreground.
 

This content will overlay the page's body.
   View example   
```
#set page(foreground: text(24pt)[🤓])

Reviewer 2 has marked our paper
"Weak Reject" because they did
not understand our approach...

```
   

 Default: `none` 
 

### `body`   [content]    

The contents of the page(s).
 

Multiple pages will be created if the content does not fit on a single page. A new page with the page properties prior to the function invocation will be created after the body has been typeset.
 

 Default: `[]` 
 [PaddingPrevious page] [Page BreakNext page]