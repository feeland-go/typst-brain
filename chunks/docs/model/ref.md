---
url: https://typst.app/docs/reference/model/ref/
category: model
topic: ref
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Reference] 
  

# `ref`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A reference to a label or bibliography.
 

Takes a label and cross-references it. There are two kind of references, determined by its [`form`]: `"normal"` and `"page"`.
 

The default, a `"normal"` reference, produces a textual reference to a label. For example, a reference to a heading will yield an appropriate string such as "Section 1" for a reference to the first heading. The word "Section" depends on the [`lang`] setting and is localized accordingly. The references are also links to the respective element. Reference syntax can also be used to [cite] from a bibliography.
 

As the default form requires a supplement and numbering, the label must be attached to a referenceable element. Referenceable elements include [headings], [figures], [equations], and [footnotes]. To create a custom referenceable element like a theorem, you can create a figure of a custom [`kind`] and write a show rule for it. In the future, there might be a more direct way to define a custom referenceable element.
 

If you just want to link to a labelled element and not get an automatic textual reference, consider using the [`link`] function instead.
 

A `"page"` reference produces a page reference to a label, displaying the page number at its location. You can use the [page's supplement] to modify the text before the page number. Unlike a `"normal"` reference, the label can be attached to any element.
 

## Example 
```
#set page(numbering: "1")
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

= Introduction <intro>
Recent developments in
typesetting software have
rekindled hope in previously
frustrated researchers. @distress
As shown in @results (see
#ref(<results>, form: "page")),
we ...

= Results <results>
We discuss our approach in
comparison with others.

== Performance <perf>
@slow demonstrates what slow
software looks like.
$ T(n) = O(2^n) $ <slow>

#bibliography("works.bib")

```
 

## Syntax 

This function also has dedicated syntax: A `"normal"` reference to a label can be created by typing an `@` followed by the name of the label (e.g. `= Introduction <intro>` can be referenced by typing `@intro`).
 

To customize the supplement, add content in square brackets after the reference: `@intro[Chapter]`.
 

## Customization 

When you only ever need to reference pages of a figure/table/heading/etc. in a document, the default `form` field value can be changed to `"page"` with a set rule. If you prefer a short "p." supplement over "page", the [`page.supplement`] field can be used for changing this:
 
```
#set page(
  numbering: "1",
  supplement: "p.",
)
#set ref(form: "page")

#figure(
  stack(
    dir: ltr,
    spacing: 1em,
    circle(),
    square(),
  ),
  caption: [Shapes],
) <shapes>

#pagebreak()

See @shapes for examples
of different shapes.

```
  

If you write a show rule for references, you can access the referenced element through the `element` field of the reference. The `element` may be `none` even if it exists if Typst hasn't discovered it yet, so you always need to handle that case in your code.
 
```
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

#show ref: it => {
  let eq = math.equation
  let el = it.element
  // Skip all other references.
  if el == none or el.func() != eq { return it }
  // Override equation references.
  link(el.location(), numbering(
    el.numbering,
    ..counter(eq).at(el.location())
  ))
}

= Beginnings <beginning>
In @beginning we prove @pythagoras.
$ a^2 + b^2 = c^2 $ <pythagoras>

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    ref([label],[supplement: ][none][auto][content][function],[form: ][str],) -> [content]  

### `target`   [label]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The target label that should be referenced.
 

Can be a label that is defined in the document or, if the [`form`] is set to `"normal"`, an entry from the [`bibliography`].
 

### `supplement`   [none] or [auto] or [content] or [function]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

A supplement for the reference.
 

If the [`form`] is set to `"normal"`:
  For references to headings or figures, this is added before the referenced number.
 For citations, this can be used to add a page number.
  

If the [`form`] is set to `"page"`, then this is added before the page number of the label referenced.
 

If a function is specified, it is passed the referenced element and should return content.
   View example   
```
#set heading(numbering: "1.")
#show ref.where(
  form: "normal"
): set ref(supplement: it => {
  if it.func() == heading {
    "Chapter"
  } else {
    "Thing"
  }
})

= Introduction <intro>
In @intro, we see how to turn
Sections into Chapters. And
in @intro[Part], it is done
manually.

```
   

 Default: `auto` 
 

### `form`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The kind of reference to produce.
   View example   
```
#set page(numbering: "1")

Here <here> we are on
#ref(<here>, form: "page").

```
   VariantDetails`"normal"`

Produces a textual reference to a label.
`"page"`

Produces a page reference to a label.
 

 Default: `"normal"` 
 [QuotePrevious page] [Strong EmphasisNext page]