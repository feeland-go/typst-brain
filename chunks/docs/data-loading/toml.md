---
url: https://typst.app/docs/reference/data-loading/toml/
category: data-loading
topic: toml
---


# toml (data-loading)

Reads structured data from a TOML file.

## Signature

`toml(strbytes) -> dictionary`

## Parameters

- `source` (str | bytes, required): A path to a TOML file or raw TOML bytes.

## Examples

```typst
#let details = toml("details.toml")

Title: #details.title \
Version: #details.version \
Authors: #(details.authors
  .join(", ", last: " and "))
```