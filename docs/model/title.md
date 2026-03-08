---
url: https://typst.app/docs/reference/model/title/
category: model
topic: title
---


# title (model)

A document title.

## Signature

`title(autocontent) -> content`

## Parameters

- `body` (auto | content, optional): The content of the title.

## Examples

```typst
#set document(
  title: [Interstellar Mail Delivery]
)

#title()

= Introduction
In recent years, ...
```

```typst
#set document(title: "Course ABC, Homework 1")
#title[Homework 1]

...
```