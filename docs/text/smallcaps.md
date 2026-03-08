---
url: https://typst.app/docs/reference/text/smallcaps/
category: text
topic: smallcaps
---


# smallcaps (text)

Displays text in small capitals.

## Signature

`smallcaps(all: bool, content) -> content`

## Parameters

- `all` (bool, optional): Whether to turn uppercase letters into small capitals as well.

- `body` (content, required): The content to display in small capitals.

## Examples

```typst
Hello \
#smallcaps[Hello]
```

```typst
#set par(justify: true)
#set heading(numbering: "I.")

#show heading: smallcaps
#show heading: set align(center)
#show heading: set text(
  weight: "regular"
)

= Introduction
#lorem(40)
```

```typst
#smallcaps(all: true)[UNICEF] is an
agency of #smallcaps(all: true)[UN].
```