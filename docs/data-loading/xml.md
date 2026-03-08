---
url: https://typst.app/docs/reference/data-loading/xml/
category: data-loading
topic: xml
---


# xml (data-loading)

Reads structured data from an XML file.

## Signature

`xml(strbytes) -> any`

## Parameters

- `source` (str | bytes, required): A path to an XML file or raw XML bytes.

## Examples

```typst
#let find-child(elem, tag) = {
  elem.children
    .find(e => "tag" in e and e.tag == tag)
}

#let article(elem) = {
  let title = find-child(elem, "title")
  let author = find-child(elem, "author")
  let pars = find-child(elem, "content")

  [= #title.children.first()]
  text(10pt, weight: "medium")[
    Published by
    #author.children.first()
  ]

  for p in pars.children {
    if type(p) == dictionary {
      parbreak()
      p.children.first()
    }
  }
}

#let data = xml("example.xml")
#for elem in data.first().children {
  if type(elem) == dictionary {
    article(elem)
  }
}
```