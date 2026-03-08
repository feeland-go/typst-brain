---
url: https://typst.app/docs/reference/model/footnote/
category: model
topic: footnote
---


# footnote (model)

A footnote.

## Signature

`footnote(numbering: strfunction, labelcontent) -> content`

## Parameters

- `numbering` (str | function, optional): How to number footnotes. Accepts a numbering pattern or function taking a single number.

- `body` (label | content, required): The content to put into the footnote. Can also be the label of another footnote this one should point to.

## Examples

```typst
Check the docs for more details.
#footnote[https://typst.app/docs]
```

```typst
You can edit Typst documents online.
#footnote[https://typst.app/app] <fn>
Checkout Typst's website. @fn
And the online app. #footnote(<fn>)
```

```typst
#set footnote(numbering: "*")

Footnotes:
#footnote[Star],
#footnote[Dagger]
```