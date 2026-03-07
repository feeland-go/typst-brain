# More sophisticated piecewise revealing

## `#one-by-one`

`#pause` may be considered syntactically a bit cumbersome as it employs a
`show`-rule.
If you prefer to signal the grouping of content appearing together by using
a single function call, you can use `#one-by-one`:

#one-by-one[Do you know ][$pi$ ][to a thousand decimal places?]

resulting in

If we still want to uncover certain elements one after the other but starting
on a later subslide, we can use the optional `start` argument of `#one-by-one`:

#one-by-one(start: 3)[This ][came ][pretty late.]

resulting in

This optional `start` argument exists for all functions displayed on this page.

## `#item-by-item`

`#one-by-one` is especially useful for arbitrary contents that you want to display
in that manner.
Sometimes, it produces a bit too much syntactical noise with all the brackets
between content, though.
That is especially true for lists, enums, and term lists.
Instead of

#one-by-one[
  - first
][
  - second
][
  - third
]

you can also write

#item-by-item[
  - first
  - second
  - third
]

resulting in

A more complex example involving enums and term lists:

#show: columns.with(3)

#set list(marker: sym.arrow)
#item-by-item[
  - first
  - second
    - some
    - detail
  - third
]
#colbreak()

#item-by-item[
  + also
  + works
  + with `enums`
]
#colbreak()

#item-by-item(start: 2)[
  / and: with
  / terms: too
]

Note that the list markers and enum numbers are not hidden.
You can truly consider this a bug or a feature...