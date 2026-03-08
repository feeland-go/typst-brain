---
url: https://typst.app/docs/reference/model/document/
category: model
topic: document
---


# document (model)

The root element of a document and its metadata.

## Signature

`document(title: nonecontent, author: strarray, description: nonecontent, keywords: strarray, date: noneautodatetime) -> content`

## Parameters

- `title` (none | content, optional): The document's title. This is rendered as the title of the PDF viewer window or the browser tab of the page.

- `author` (str | array, optional): The document's authors.

- `description` (none | content, optional): The document's description.

- `keywords` (str | array, optional): The document's keywords.

- `date` (none | auto | datetime, optional): The document's creation date.

## Examples

```typst
#set document(title: [Hello])

This has no visible output, but
embeds metadata into the PDF!
```