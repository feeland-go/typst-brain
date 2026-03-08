---
url: https://typst.app/docs/reference/data-loading/yaml/
category: data-loading
topic: yaml
---


# yaml (data-loading)

Reads structured data from a YAML file.

## Signature

`yaml(strbytes) -> any`

## Parameters

- `source` (str | bytes, required): A path to a YAML file or raw YAML bytes.

## Examples

```typst
#let bookshelf(contents) = {
  for (author, works) in contents {
    author
    for work in works [
      - #work.title (#work.published)
    ]
  }
}

#bookshelf(
  yaml("scifi-authors.yaml")
)
```