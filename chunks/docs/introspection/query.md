---
url: https://typst.app/docs/reference/introspection/query/
category: introspection
topic: query
---

[  ] 
   
  [Reference] 
   
  [Introspection] 
   
  [Query] 
  

# `query`Contextual  Question mark    Contextual functions can only be used when the context is known   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Finds elements in the document.
 

The `query` function lets you search your document for elements of a particular type or with a particular label. To use it, you first need to ensure that [context] is available.
 

## Finding elements 

In the example below, we manually create a table of contents instead of using the [`outline`] function.
 

To do this, we first query for all headings in the document at level 1 and where `outlined` is true. Querying only for headings at level 1 ensures that, for the purpose of this example, sub-headings are not included in the table of contents. The `outlined` field is used to exclude the "Table of Contents" heading itself.
 

Note that we open a `context` to be able to use the `query` function.
 
```
#set page(numbering: "1")

#heading(outlined: false)[
  Table of Contents
]
#context {
  let chapters = query(
    heading.where(
      level: 1,
      outlined: true,
    )
  )
  for chapter in chapters {
    let loc = chapter.location()
    let nr = numbering(
      loc.page-numbering(),
      ..counter(page).at(loc),
    )
    [#chapter.body #h(1fr) #nr \ ]
  }
}

= Introduction
#lorem(10)
#pagebreak()

== Sub-Heading
#lorem(8)

= Discussion
#lorem(18)

```
  

To get the page numbers, we first get the location of the elements returned by `query` with [`location`]. We then also retrieve the [page numbering] and [page counter] at that location and apply the numbering to the counter.
 

## A word of caution 

To resolve all your queries, Typst evaluates and layouts parts of the document multiple times. However, there is no guarantee that your queries can actually be completely resolved. If you aren't careful a query can affect itself—leading to a result that never stabilizes.
 

In the example below, we query for all headings in the document. We then generate as many headings. In the beginning, there's just one heading, titled `Real`. Thus, `count` is `1` and one `Fake` heading is generated. Typst sees that the query's result has changed and processes it again. This time, `count` is `2` and two `Fake` headings are generated. This goes on and on. As we can see, the output has a finite amount of headings. This is because Typst simply gives up after a few attempts.
 

In general, you should try not to write queries that affect themselves. The same words of caution also apply to other introspection features like [counters] and [state].
 
```
= Real
#context {
  let elems = query(heading)
  let count = elems.len()
  count * [= Fake]
}

```
 

## Command line queries 

You can also perform queries from the command line with the `typst query` command. This command executes an arbitrary query on the document and returns the resulting elements in serialized form. Consider the following `example.typ` file which contains some invisible [metadata]:
 
```
#metadata("This is a note") <note>

```
 

You can execute a query on it as follows using Typst's CLI:
 
```

$ typst query example.typ "<note>"
[
  {
    "func": "metadata",
    "value": "This is a note",
    "label": "<note>"
  }
]

```
 

### Retrieving a specific field 

Frequently, you're interested in only one specific field of the resulting elements. In the case of the `metadata` element, the `value` field is the interesting one. You can extract just this field with the `--field` argument.
 
```

$ typst query example.typ "<note>" --field value
["This is a note"]

```
 

If you are interested in just a single element, you can use the `--one` flag to extract just it.
 
```

$ typst query example.typ "<note>" --field value --one
"This is a note"

```
 

### Querying for a specific export target 

In case you need to query a document when exporting for a specific target, you can use the `--target` argument. Valid values are `paged`, and `html` (if the [`html`] feature is enabled).

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    query([label][selector][location][function]) -> [array]  

### `target`   [label] or [selector] or [location] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Can be
  an element function like a `heading` or `figure`,
 a `<label>`,
 a more complex selector like `heading.where(level: 1)`,
 or `selector(heading).before(here())`.
  

Only [locatable] element functions are supported.
 [MetadataPrevious page] [StateNext page]