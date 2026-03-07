# Full width block

Sometimes you want content that spans the whole physical width of your slide,
disregarding the page margin.
This can be achieved using some annoying calculatings involving `page.margin`
which are luckily already done for you if you use `#toolbox.full-width-block`!

Note that this only works when the left and right page margin are explicitly
specified (i.e. both are neither `none` nor `auto`).

This can be very useful for headers and footers.

#set page(
  paper: "presentation-16-9",
  margin: 2cm,
  header: align(top,    toolbox.full-width-block(fill: aqua, inset: 8pt)[I'm up high]),
  footer: align(bottom, toolbox.full-width-block(fill: lime, inset: 8pt)[I'm down low]),
)

#slide[
  #lorem(10)
]