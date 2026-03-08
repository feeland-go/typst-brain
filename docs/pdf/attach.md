---
url: https://typst.app/docs/reference/pdf/attach/
category: pdf
topic: attach
---


# attach (pdf)

A file that will be attached to the output PDF.

## Signature

`pdf.attach(str, bytes, relationship: nonestr, mime-type: nonestr, description: nonestr) -> content`

## Parameters

- `path` (str, required): The path of the file to be attached.

- `data` (bytes, required): Raw file data, optionally.

- `relationship` (none | str, optional): The relationship of the attached file to the document.

- `mime-type` (none | str, optional): The MIME type of the attached file.

- `description` (none | str, optional): A description for the attached file.