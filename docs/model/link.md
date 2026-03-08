---
url: https://typst.app/docs/reference/model/link/
category: model
topic: link
---


# link (model)

Links to a URL or a location in the document.

## Signature

`link(strlabellocationdictionary, content) -> content`

## Parameters

- `dest` (str | label | location | dictionary, required): The destination the link points to.

- `body` (content, required): The content that should become a link.

## Examples

```typst
#show link: underline

https://example.com \

#link("https://example.com") \
#link("https://example.com")[
  See example.com
]
```

```typst
= Introduction <intro>
#link("mailto:hello@typst.app") \
#link(<intro>)[Go to intro] \
#link((page: 1, x: 0pt, y: 0pt))[
  Go to top
]
```