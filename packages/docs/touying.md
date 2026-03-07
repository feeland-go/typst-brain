---
package: touying
version: 0.6.2
url: https://typst.app/universe/package/touying
---

# touying
0.6.2  A powerful package for creating presentation slides in Typst.

  Featured Package

     
Touying (投影 in chinese, /tóuyǐng/, meaning projection) is a user-friendly, powerful and efficient package for creating presentation slides in Typst.

If you like it, consider giving a star on GitHub. Touying is a community-driven project, feel free to suggest any ideas and contribute.

## Document

Read touying documentation to learn all about Touying. If you have any questions, you can also ask on DeepWiki or Zread for AI help.

We will maintain English and Chinese versions of the documentation for Touying, and for each major version, we will maintain a documentation copy. This allows you to easily refer to old versions of the Touying documentation and migrate to new versions.

Note that the documentation may be outdated, and you can also use Tinymist to view Touying’s annotated documentation by hovering over the code.

## Gallery

Touying offers a gallery page via wiki, where you can browse elegant slides created by Touying users. You’re also encouraged to contribute your own beautiful slides here!

## Special Features

* Split slides by headings document

= Section

== Subsection

=== First Slide

Hello, Touying!

=== Second Slide

Hello, Typst!

* `#pause` and `#meanwhile` animations document

#slide[
  First

  #pause

  Second

  #meanwhile

  Third

  #pause

  Fourth
]

* Math Equation Animation document

* `touying-reducer` Cetz and Fletcher Animations document

* Correct outline and bookmark (no duplicate and correct page number)

* Dewdrop Theme Navigation Bar document

* Semi-transparent cover mode document

* Speaker notes for dual-screen document

* Export slides to PPTX and HTML formats and show presentation online. touying-exporter touying-template online

* Instantly share touying slides on git, example with gistd

## Quick start

Before you begin, make sure you have installed the Typst environment. If not, you can use the Web App or the Tinymist LSP extensions for VS Code.

To use Touying, you only need to include the following code in your document:

#import "@preview/touying:0.6.2": *
#import themes.simple: *

#show: simple-theme.with(aspect-ratio: "16-9")

= Title

== First Slide

Hello, Touying!

#pause

Hello, Typst!

It’s simple. Congratulations on creating your first Touying slide! 🎉

Tip: You can use Typst syntax like `#import "config.typ": *` or `#include "content.typ"` to implement Touying’s multi-file architecture.

## More Complex Examples

In fact, Touying provides various styles for writing slides. For example, the above example uses first-level and second-level titles to create new slides. However, you can also use the `#slide[..]` format to access more powerful features provided by Touying.

#import "@preview/touying:0.6.2": *
#import themes.university: *
#import "@preview/cetz:0.4.2"
#import "@preview/fletcher:0.5.8" as fletcher: node, edge
#import "@preview/numbly:0.1.0": numbly
#import "@preview/theorion:0.4.1": *
#import cosmos.clouds: *
#show: show-theorion

// cetz and fletcher bindings for touying
#let cetz-canvas = touying-reducer.with(reduce: cetz.canvas, cover: cetz.draw.hide.with(bounds: true))
#let fletcher-diagram = touying-reducer.with(reduce: fletcher.diagram, cover: fletcher.hide)

#show: university-theme.with(
  aspect-ratio: "16-9",
  // align: horizon,
  // config-common(handout: true),
  config-common(frozen-counters: (theorem-counter,)),  // freeze theorem counter for animation
  config-info(
    title: [Title],
    subtitle: [Subtitle],
    author: [Authors],
    date: datetime.today(),
    institution: [Institution],
    logo: emoji.school,
  ),
)

#set heading(numbering: numbly("{1}.", default: "1.1"))

#title-slide()

== Outline 

#components.adaptive-columns(outline(title: none, indent: 1em))

= Animation

== Simple Animation

We can use `#pause` to #pause display something later.

#pause

Just like this.

#meanwhile

Meanwhile, #pause we can also use `#meanwhile` to #pause display other content synchronously.

#speaker-note[
  + This is a speaker note.
  + You won't see it unless you use `config-common(show-notes-on-second-screen: right)`
]

== Complex Animation

At subslide #touying-fn-wrapper((self: none) => str(self.subslide)), we can

use #uncover("2-")[`#uncover` function] for reserving space,

use #only("2-")[`#only` function] for not reserving space,

#alternatives[call `#only` multiple times \u{2717}][use `#alternatives` function #sym.checkmark] for choosing one of the alternatives.

== Callback Style Animation

#slide(
  repeat: 3,
  self => [
    #let (uncover, only, alternatives) = utils.methods(self)

    At subslide #self.subslide, we can

    use #uncover("2-")[`#uncover` function] for reserving space,

    use #only("2-")[`#only` function] for not reserving space,

    #alternatives[call `#only` multiple times \u{2717}][use `#alternatives` function #sym.checkmark] for choosing one of the alternatives.
  ],
)

== Math Equation Animation

Equation with `pause`:

$
  f(x) &= pause x^2 + 2x + 1 \
  &= pause (x + 1)^2 \
$

#meanwhile

Here, #pause we have the expression of $f(x)$.

#pause

By factorizing, we can obtain this result.

== CeTZ Animation

CeTZ Animation in Touying:

#cetz-canvas({
  import cetz.draw: *

  rect((0, 0), (5, 5))

  (pause,)

  rect((0, 0), (1, 1))
  rect((1, 1), (2, 2))
  rect((2, 2), (3, 3))

  (pause,)

  line((0, 0), (2.5, 2.5), name: "line")
})

== Fletcher Animation

Fletcher Animation in Touying:

#fletcher-diagram(
  node-stroke: .1em,
  node-fill: gradient.radial(blue.lighten(80%), blue, center: (30%, 20%), radius: 80%),
  spacing: 4em,
  edge((-1, 0), "r", "-|>", `open(path)`, label-pos: 0, label-side: center),
  node((0, 0), `reading`, radius: 2em),
  edge((0, 0), (0, 0), `read()`, "--|>", bend: 130deg),
  pause,
  edge(`read()`, "-|>"),
  node((1, 0), `eof`, radius: 2em),
  pause,
  edge(`close()`, "-|>"),
  node((2, 0), `closed`, radius: 2em, extrude: (-2.5, 0)),
  edge((0, 0), (2, 0), `close()`, "-|>", bend: -40deg),
)

= Theorems

== Prime numbers

#definition[
  A natural number is called a #highlight[_prime number_] if it is greater
  than 1 and cannot be written as the product of two smaller natural numbers.
]
#example[
  The numbers $2$, $3$, and $17$ are prime.
  @cor_largest_prime shows that this list is not exhaustive!
]

#theorem(title: "Euclid")[
  There are infinitely many primes.
]
#pagebreak(weak: true)
#proof[
  Suppose to the contrary that $p_1, p_2, dots, p_n$ is a finite enumeration
  of all primes. Set $P = p_1 p_2 dots p_n$. Since $P + 1$ is not in our list,
  it cannot be prime. Thus, some prime factor $p_j$ divides $P + 1$. Since
  $p_j$ also divides $P$, it must divide the difference $(P + 1) - P = 1$, a
  contradiction.
]

#corollary[
  There is no largest prime number.
] 
#corollary[
  There are infinitely many composite numbers.
]

#theorem[
  There are arbitrarily long stretches of composite numbers.
]

#proof[
  For any $n > 2$, consider $
    n! + 2, quad n! + 3, quad ..., quad n! + n
  $
]

= Others

== Side-by-side

#slide(composer: (1fr, 1fr))[
  First column.
][
  Second column.
]

== Multiple Pages

#lorem(200)

#show: appendix

= Appendix

== Appendix

Please pay attention to the current slide number.

## Acknowledgements

Thanks to…

* @andreasKroepelin for the `polylux` package

* @enklht for many fixes and improvements

* @Enivex for the `metropolis` theme

* @drupol for the `university` theme

* @pride7 for the `aqua` theme

* @Coekjan and @QuadnucYard for the `stargazer` theme

* @ntjess for contributing to `fit-to-height`, `fit-to-width` and `cover-with-rect`

## Poster

View Code

## Star History

 
   
   
   
 
     

### How to add
 Copy this into your project and use the import as  `touying`

  
```typst
#import "@preview/touying:0.6.2"
```
      Check the docs for  
more information on how to import packages

.

   

### About
   Authors:  OrangeX4, enklht, Andreas Kröpelin, ntjess, Enivex, Pol Dellaiera, pride7, &amp; Coekjan   License: MIT Current version: 0.6.2 Last updated: March 4, 2026 First released: January 11, 2024  Minimum Typst version: 0.12.0  Archive size:  309 kB        Repository:   GitHub      Category:   * Presentation
      Explore more packages by
OrangeX4, enklht, Andreas Kröpelin, ntjess, Enivex, Pol Dellaiera, pride7, & Coekjan

    

### Where to report issues?
 This package is a project of OrangeX4, enklht, Andreas Kröpelin, ntjess, Enivex, Pol Dellaiera, pride7, and Coekjan.
 
Report issues on their repository.
 
You can also try to ask for help with this package on the  Forum.

 Please report this package to the Typst team using the  contact form 
if you believe it is a safety hazard or infringes upon your rights.

   

### Version history
    Version Release Date      0.6.2   March 4, 2026     0.6.1    February 25, 2025     0.6.0    February 20, 2025     0.5.5    December 19, 2024     0.5.4    December 18, 2024     0.5.3    October 15, 2024     0.5.2    September 3, 2024     0.5.1    September 3, 2024     0.5.0    September 2, 2024     0.4.2    May 27, 2024     0.4.1    May 13, 2024     0.4.0    April 6, 2024     0.3.3    March 26, 2024     0.3.2    March 15, 2024     0.3.1    March 7, 2024     0.3.0    March 6, 2024     0.2.1    February 17, 2024     0.2.0    January 20, 2024     0.1.0    January 11, 2024       Typst GmbH did not create this package and cannot guarantee
          correct functionality of this package or compatibility with any
          version of the Typst compiler or app.