# Sections

Another way of expressing where we are in a presentation is working with sections.

In your presentation, you can incorporate the following features from the
`toolbox` module:

First, whenever you want to start a new section, you can call

#toolbox.register-section(the-section-name)

with whatever name you want.

Based on that, you can then display what section the presenter is currently in
by using:

#toolbox.current-section

If no section has been registered so far, this is empty content (`[]`).

And finally, you might want to display some kind of overview over all the
sections.
This is achieved by:

#toolbox.all-sections((sections, current) => [some content])

`all-sections` takes a function with two arguments and uses that to produce
some content based on all sections in the presentation and the current one.

For example:

#let sections-band = toolbox.all-sections( (sections, current) => {
  set text(fill: gray, size: .8em)
  sections
    .map(s => if s == current { strong(s) } else { s })
    .join([ • ])
})

#set page(footer: sections-band)

#slide[
  #toolbox.register-section[The beginning]

  #lorem(5)
]

#slide[
  #lorem(3)
]

#slide[
  #toolbox.register-section[The middle]

  #lorem(6)
]

#slide[
  #toolbox.register-section[The end]

  #lorem(4)
]

Another example, producing a table of contents and title slides for each new
section:

#let my-new-section(name) = slide[
  #set align(horizon)
  #set text(size: 2em)
  #toolbox.register-section(name)

  #strong(name)
]

#slide[
  #toolbox.all-sections((sections, current) => {
    enum(..sections)
  })
]

#my-new-section[The beginning]

#slide[
  We are currently in Section "#toolbox.current-section" and I like it so far.
]

#slide[
  Still in the same section.
]

#my-new-section[The middle]

#slide[
  Oh, new section. What comes after "#toolbox.current-section"?
]

#my-new-section[The end]

#slide[
  You might have guessed this, to be honest.
]