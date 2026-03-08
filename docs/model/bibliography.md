---
url: https://typst.app/docs/reference/model/bibliography/
category: model
topic: bibliography
---


# bibliography (model)

A bibliography / reference listing.

## Signature

`bibliography(strbytesarray, title: noneautocontent, full: bool, style: strbytes) -> content`

## Parameters

- `sources` (str | bytes | array, required): One or multiple paths to or raw bytes for Hayagriva .yaml and/or BibLaTeX .bib files.

- `title` (none | auto | content, optional): The title of the bibliography.

- `full` (bool, optional): Whether to include all works from the given bibliography files, even those that weren't cited in the document.

- `style` (str | bytes, optional): The bibliography style.

## Examples

```typst
This was already noted by
pirates long ago. @arrgh

Multiple sources say ...
@arrgh @netwok.

#bibliography("works.bib")
```