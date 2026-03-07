---
url: https://typst.app/docs/reference/model/strong/
category: model
topic: strong
---


# strong (model)

Strongly emphasizes content by increasing the font weight.

## Signature

`strong(delta: int, content) -> content`

## Parameters

- `delta` (int, optional): The delta to apply on the font weight.

- `body` (content, required): The content to strongly emphasize.

## Examples

```typst
This is *strong.* \
This is #strong[too.] \

#show strong: set text(red)
And this is *evermore.*
```

```typst
#set strong(delta: 0)
No *effect!*
```