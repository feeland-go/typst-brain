---
url: https://typst.app/docs/reference/model/quote/
category: model
topic: quote
---


# quote (model)

Displays a quote alongside an optional attribution.

## Signature

`quote(block: bool, quotes: autobool, attribution: nonelabelcontent, content) -> content`

## Parameters

- `block` (bool, optional): Whether this is a block quote.

- `quotes` (auto | bool, optional): Whether double quotes should be added around this quote.

- `attribution` (none | label | content, optional): The attribution of this quote, usually the author or source. Can be a label pointing to a bibliography entry or any content. By default only displayed for block quotes, but can be changed using a show rule.

- `body` (content, required): The quote.

## Examples

```typst
Plato is often misquoted as the author of #quote[I know that I know
nothing], however, this is a derivation form his original quote:

#set quote(block: true)

#quote(attribution: [Plato])[
  ... ἔοικα γοῦν τούτου γε σμικρῷ τινι αὐτῷ τούτῳ σοφώτερος εἶναι, ὅτι
  ἃ μὴ οἶδα οὐδὲ οἴομαι εἰδέναι.
]
#quote(attribution: [from the Henry Cary literal translation of 1897])[
  ... I seem, then, in just this little thing to be wiser than this man at
  any rate, that what I do not know I do not think I know either.
]
```

```typst
#set quote(block: true)
#show quote: set align(center)
#show quote: set pad(x: 5em)

#quote[
  You cannot pass... I am a servant of the Secret Fire, wielder of the
  flame of Anor. You cannot pass. The dark fire will not avail you,
  flame of Udûn. Go back to the Shadow! You cannot pass.
]
```

```typst
An inline citation would look like
this: #quote(
  attribution: [René Descartes]
)[
  cogito, ergo sum
], and a block equation like this:
#quote(
  block: true,
  attribution: [JFK]
)[
  Ich bin ein Berliner.
]
```