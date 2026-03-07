---
url: https://typst.app/docs/reference/model/cite/
category: model
topic: cite
---

[  ] 
   
  [Reference] 
   
  [Model] 
   
  [Cite] 
  

# `cite`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Cite a work from the bibliography.
 

Before you starting citing, you need to add a [bibliography] somewhere in your document.
 

## Example 
```
This was already noted by
pirates long ago. @arrgh

Multiple sources say ...
@arrgh @netwok.

You can also call `cite`
explicitly. #cite(<arrgh>)

#bibliography("works.bib")

```
 

If your source name contains certain characters such as slashes, which are not recognized by the `<>` syntax, you can explicitly call `label` instead.
 
```
Computer Modern is an example of a modernist serif typeface.
#cite(label("DBLP:books/lib/Knuth86a")).

```
 

## Syntax 

This function indirectly has dedicated syntax. [References] can be used to cite works from the bibliography. The label then corresponds to the citation key.

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    cite([label],[supplement: ][none][content],[form: ][none][str],[style: ][auto][str][bytes],) -> [content]  

### `key`   [label]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The citation key that identifies the entry in the bibliography that shall be cited, as a label.
   View example   
```
// All the same
@netwok \
#cite(<netwok>) \
#cite(label("netwok"))

```
   

### `supplement`   [none] or [content]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

A supplement for the citation such as page or chapter number.
 

In reference syntax, the supplement can be added in square brackets:
   View example   
```
This has been proven. @distress[p.~7]

#bibliography("works.bib")

```
   

 Default: `none` 
 

### `form`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The kind of citation to produce. Different forms are useful in different scenarios: A normal citation is useful as a source at the end of a sentence, while a "prose" citation is more suitable for inclusion in the flow of text.
 

If set to `none`, the cited work is included in the bibliography, but nothing will be displayed.
   View example   
```
#cite(<netwok>, form: "prose")
show the outsized effects of
pirate life on the human psyche.

```
   VariantDetails`"normal"`

Display in the standard way for the active style.
`"prose"`

Produces a citation that is suitable for inclusion in a sentence.
`"full"`

Mimics a bibliography entry, with full information about the cited work.
`"author"`

Shows only the cited work's author(s).
`"year"`

Shows only the cited work's year.
 

 Default: `"normal"` 
 

### `style`   [auto] or [str] or [bytes]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The citation style.
 

This can be:
  `auto` to automatically use the [bibliography's style] for citations.
 A string with the name of one of the built-in styles (see below). Some of the styles listed below appear twice, once with their full name and once with a short alias.
 A path string to a [CSL file]. For more details about paths, see the [Paths section].
 Raw bytes from which a CSL style should be decoded.
     View options   VariantDetails`"alphanumeric"`

Alphanumeric
`"american-anthropological-association"`

American Anthropological Association
`"american-chemical-society"`

American Chemical Society
`"american-geophysical-union"`

American Geophysical Union
`"american-institute-of-aeronautics-and-astronautics"`

American Institute of Aeronautics and Astronautics
`"american-institute-of-physics"`

American Institute of Physics 4th edition
`"american-medical-association"`

American Medical Association 11th edition
`"american-meteorological-society"`

American Meteorological Society
`"american-physics-society"`

American Physical Society
`"american-physiological-society"`

American Physiological Society
`"american-political-science-association"`

American Political Science Association
`"american-psychological-association"`

American Psychological Association 7th edition
`"apa"`

A short alias of `american-psychological-association`
`"american-society-for-microbiology"`

American Society for Microbiology
`"american-society-of-civil-engineers"`

American Society of Civil Engineers
`"american-society-of-mechanical-engineers"`

American Society of Mechanical Engineers
`"american-sociological-association"`

American Sociological Association 6th/7th edition
`"angewandte-chemie"`

Angewandte Chemie International Edition
`"annual-reviews"`

Annual Reviews (sorted by order of appearance)
`"annual-reviews-author-date"`

Annual Reviews (author-date)
`"associacao-brasileira-de-normas-tecnicas"`

Associação Brasileira de Normas Técnicas (Português - Brasil)
`"association-for-computing-machinery"`

Association for Computing Machinery
`"biomed-central"`

BioMed Central
`"bristol-university-press"`

Bristol University Press
`"british-medical-journal"`

BMJ
`"bmj"`

A short alias of `british-medical-journal`
`"cell"`

Cell
`"chicago-author-date"`

Chicago Manual of Style 18th edition (author-date)
`"chicago-notes"`

Chicago Manual of Style 18th edition (notes and bibliography)
`"chicago-fullnotes"`

A short alias of `chicago-notes`
`"chicago-shortened-notes"`

Chicago Manual of Style 18th edition (shortened notes and bibliography)
`"copernicus"`

Copernicus Publications
`"council-of-science-editors"`

Council of Science Editors, Citation-Sequence (numeric, brackets)
`"council-of-science-editors-author-date"`

Council of Science Editors, Name-Year 9th edition (author-date)
`"current-opinion"`

Current Opinion journals
`"deutsche-gesellschaft-für-psychologie"`

Deutsche Gesellschaft für Psychologie 5. Auflage (Deutsch)
`"deutsche-sprache"`

Deutsche Sprache (Deutsch)
`"elsevier-harvard"`

Elsevier - Harvard (with titles)
`"elsevier-vancouver"`

Elsevier - Vancouver
`"elsevier-with-titles"`

Elsevier (numeric, with titles)
`"frontiers"`

Frontiers journals
`"future-medicine"`

Future Medicine journals
`"future-science"`

Future Science Group
`"gb-7714-2005-numeric"`

China National Standard GB/T 7714-2005 (numeric, 中文)
`"gb-7714-2015-author-date"`

China National Standard GB/T 7714-2015 (author-date, 中文)
`"gb-7714-2015-note"`

China National Standard GB/T 7714-2015 (note, 中文)
`"gb-7714-2015-numeric"`

China National Standard GB/T 7714-2015 (numeric, 中文)
`"gost-r-705-2008-numeric"`

Russian GOST R 7.0.5-2008 (numeric)
`"harvard-cite-them-right"`

Cite Them Right 12th edition - Harvard
`"institute-of-electrical-and-electronics-engineers"`

IEEE
`"ieee"`

A short alias of `institute-of-electrical-and-electronics-engineers`
`"institute-of-physics-numeric"`

Institute of Physics (numeric)
`"iso-690-author-date"`

ISO-690 (author-date, English)
`"iso-690-numeric"`

ISO-690 (numeric, English)
`"karger"`

Karger journals
`"mary-ann-liebert-vancouver"`

Mary Ann Liebert - Vancouver
`"modern-humanities-research-association-notes"`

Modern Humanities Research Association 4th edition (notes)
`"modern-humanities-research-association"`

A short alias of `modern-humanities-research-association-notes`
`"modern-language-association"`

Modern Language Association 9th edition (in-text citations)
`"mla"`

A short alias of `modern-language-association`
`"modern-language-association-8"`

Modern Language Association 8th edition
`"mla-8"`

A short alias of `modern-language-association-8`
`"multidisciplinary-digital-publishing-institute"`

Multidisciplinary Digital Publishing Institute
`"nature"`

Nature
`"pensoft"`

Pensoft Journals
`"public-library-of-science"`

Public Library of Science
`"plos"`

A short alias of `public-library-of-science`
`"royal-society-of-chemistry"`

Royal Society of Chemistry
`"sage-vancouver"`

SAGE - Vancouver
`"sist02"`

SIST02 (日本語)
`"spie"`

SPIE journals
`"springer-basic"`

Springer - Basic (numeric, brackets)
`"springer-basic-author-date"`

Springer - Basic (author-date)
`"springer-fachzeitschriften-medizin-psychologie"`

Springer - Fachzeitschriften Medizin Psychologie (Deutsch)
`"springer-humanities-author-date"`

Springer - Humanities (author-date)
`"springer-lecture-notes-in-computer-science"`

Springer - Lecture Notes in Computer Science
`"springer-mathphys"`

Springer - MathPhys (numeric, brackets)
`"springer-socpsych-author-date"`

Springer - SocPsych (author-date)
`"springer-vancouver"`

Springer - Vancouver (brackets)
`"taylor-and-francis-chicago-author-date"`

Taylor & Francis Journals Standard Reference Style Guide: Chicago author-date version 2.0
`"taylor-and-francis-national-library-of-medicine"`

Taylor & Francis - National Library of Medicine
`"the-institution-of-engineering-and-technology"`

The Institution of Engineering and Technology
`"the-lancet"`

The Lancet
`"thieme"`

Thieme-German (Deutsch)
`"trends"`

Trends journals
`"turabian-author-date"`

Chicago Manual of Style 17th edition (author-date)
`"turabian-fullnote-8"`

Chicago Manual of Style 17th edition (notes and bibliography, subsequent author-title)
`"vancouver"`

Vancouver
`"vancouver-superscript"`

Vancouver (superscript)
   

 Default: `auto` 
 [Bullet ListPrevious page] [DocumentNext page]