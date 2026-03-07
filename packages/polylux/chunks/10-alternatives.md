# `#alternatives` to substitute content

The so far discussed helpers `#later`, `#one-by-one` etc. all build upon
`#uncover`.
There is an analogon to `#one-by-one` that is based on `#only`, namely
`#alternatives`.
You can use it to show some content on one subslide, then substitute it by
something else, then by something else, etc.

Consider this example:

#only(1)[Ann] #only(2)[Bob] #only(3)[Christopher]
likes
#only(1)[chocolate] #only(2)[strawberry] #only(3)[vanilla]
ice cream.

#repeat[| #h(4cm)] // visual reference

Here, we want to display three different sentences with the same structure:
Some person likes some sort of ice cream.

As you can see, the positioning of `likes` and `ice cream` moves
around in the produced slide because, for example, `Ann` takes much less space
than `Christopher` when using `#only` for that job.
This somewhat disturbs the perception of the constant structure of the sentence
and that only the names and kinds of ice cream change.

To avoid such movement and only substitute certain parts of content, you can use
the `#alternatives` function.
With it, our example becomes:

#alternatives[Ann][Bob][Christopher]
likes
#alternatives[chocolate][strawberry][vanilla]
ice cream.

#repeat[| #h(4cm)] // visual reference

resulting in

`#alternatives` will put enough empty space around, for example, `Ann` such that
it uses the same amount of space as `Christopher`.
In a sense, it is like a mix of `#only` and `#uncover` with some reserving of
space.

### Repeat last content

In case you have other dynamic content on a slide that happens after the contents
of `#alternatives` are exhausted, you might want to not have the `#alternatives`
element disappear but instead continue to show its last content argument.
To achieve this, you can use the `repeat-last` parameter:

#alternatives(repeat-last: true)[temporary][transitory][ephemeral][permanent!]

#uncover(5)[Did I miss something?]

resulting in

### Positioning

By default, all elements that enter an `#alternatives` command are aligned at
the bottom left corner.
This might not always be the desired or the most pleasant way to position it, so
you can provide an optional `position` argument to `#alternatives` that takes an
[`alignment` or `2d alignment`](https://typst.app/docs/reference/layout/align/#parameters--alignment).
For example:

We know that
#alternatives(position: center + horizon)[$pi$][$sqrt(2)^2 + 1/3$]
is
#alternatives[irrational][rational].

makes the mathematical terms look better positioned:

All functions described on this page have such a `position` argument.

Similar to `#one-by-one`, `#alternatives` also has an optional `start` argument
that works just the same.

## `#alternatives-match`

`#alternatives` has a couple of "cousins" that might be more convenient in some
situations.
The first one is `#alternatives-match` that has a name inspired by match-statements
in many functional programming languages.
The idea is that you give it a dictionary mapping from subslides to content:

#alternatives-match((
  "1, 3-5": [this text has the majority],
  "2, 6": [this is shown less often]
))

resulting in

Note that it is your responsibility to make sure that the subslide sets are
mutually disjoint.

## `#alternatives-cases`

You can use this function if you want to have one piece of content that changes
only slightly depending of what "case" of subslides you are in.
So instead of

#alternatives-match((
  "1, 3" : [
    Some text
  ],
  "2" : [
    #set text(fill: teal)
    Some text
  ],
))

you can avoid duplication and write

#alternatives-cases(("1, 3", "2"), case => [
  #set text(fill: teal) if case == 1
  Some text
])

using a function that maps the current "case" to content, resulting in

Note that the cases are 0-indexed (as are Typst arrays).

## `#alternatives-fn`

Finally, you can have very fine-grained control over the content depending on
the current subslide by using `#alternatives-fn`.
It accepts a function (hence the name) that maps the current subslide index to
some content.

Similar to `#alternatives`, it accepts an optional `start` parameter that has a
default of `1`.
`#alternatives-fn` only knows for how long to display something, though, if you
provide either the number of subslides (`count` parameter) or the last subslide
index (`end` parameter).
So exactly one of them is necessary.

For example:

We are on subslide:
#alternatives-fn(start: 2, count: 7, subslide => {
  numbering("(i)", subslide)
})

resulting in