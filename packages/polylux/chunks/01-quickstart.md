## Quickstart

For the bare-bones, do-it-yourself experience, all you need is:

// Get Polylux from the official package repository
#import "@preview/polylux:0.4.0": *

// Make the paper dimensions fit for a presentation and the text larger
#set page(paper: "presentation-16-9")
#set text(size: 25pt, font: "Lato")

// Use #slide to create a slide and style it using your favourite Typst functions
#slide[
  #set align(horizon)
  = Very minimalist slides

  A lazy author

  July 23, 2023
]

#slide[
  == First slide

  Some static text on this slide.
]

#slide[
  == This slide changes!

  You can always see this.
  // Make use of features like #uncover, #only, and others to create dynamic content
  #uncover(2)[But this appears later!]
]

This code produces these PDF pages:

From there, you can either start creatively adapting the looks to your likings
or you directly start by using a
template.
The simplest one of them is called
“basic”.
It is still very unintrusive but gives you some sensible defaults.

For dynamic content, Polylux also provides a convenient API for complex
overlays.

If you use pdfpc to display your slides, you can
rely on Polylux’ support for it
and create speaker notes, hide slides, configure the timer and more!

Visit the
book
for more details or take a look at the
demo PDF
where you can see the features of this template in action.

⚠ This package is under active development and there are no backwards
compatibility guarantees!