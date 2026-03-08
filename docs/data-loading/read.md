---
url: https://typst.app/docs/reference/data-loading/read/
category: data-loading
topic: read
---


# read (data-loading)

Reads plain text or data from a file.

## Signature

`read(str, encoding: nonestr) -> strbytes`

## Parameters

- `path` (str, required): Path to a file.

- `encoding` (none | str, optional): The encoding to read the file with.

## Examples

```typst
An example for a HTML file: \
#let text = read("example.html")
#raw(text, block: true, lang: "html")

Raw bytes:
#read("tiger.jpg", encoding: none)
```