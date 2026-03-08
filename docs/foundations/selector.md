---
url: https://typst.app/docs/reference/foundations/selector/
category: foundations
topic: selector
---


# selector (foundations)

A filter for selecting elements within the document.

## Signature

`selector(strregexlabelselectorlocationfunction) -> selector target str or regex or label or selector or location or function Required Positional`

## Examples

```typst
#context query(
  heading.where(level: 1)
    .or(heading.where(level: 2))
)

= This will be found
== So will this
=== But this will not.
```