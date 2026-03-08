---
url: https://typst.app/docs/reference/model/cite/
category: model
topic: cite
---


# cite (model)

Cite a work from the bibliography.

## Signature

`cite(label, supplement: nonecontent, form: nonestr, style: autostrbytes) -> content`

## Parameters

- `key` (label, required): The citation key that identifies the entry in the bibliography that shall be cited, as a label.

- `supplement` (none | content, optional): A supplement for the citation such as page or chapter number.

- `form` (none | str, optional): The kind of citation to produce. Different forms are useful in different scenarios: A normal citation is useful as a source at the end of a sentence, while a "prose" citation is more suitable for inclusion in the flow of text.

- `style` (auto | str | bytes, optional): The citation style.

## Examples

```typst
This was already noted by
pirates long ago. @arrgh

Multiple sources say ...
@arrgh @netwok.

You can also call `cite`
explicitly. #cite(<arrgh>)

#bibliography("works.bib")
```

```typst
// All the same
@netwok \
#cite(<netwok>) \
#cite(label("netwok"))
```

```typst
This has been proven. @distress[p.~7]

#bibliography("works.bib")
```