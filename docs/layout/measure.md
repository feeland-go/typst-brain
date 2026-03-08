---
url: https://typst.app/docs/reference/layout/measure/
category: layout
topic: measure
---


# measureContextual (layout)

Measures the layouted size of content.

## Signature

`measure(width: autolength, height: autolength, content) -> dictionary`

## Parameters

- `width` (auto | length, optional): The width available to layout the content.

- `height` (auto | length, optional): The height available to layout the content.

- `content` (content, required): The content whose size to measure.

## Examples

```typst
#let content = [Hello!]
#content
#set text(14pt)
#content
```

```typst
#let thing(body) = context {
  let size = measure(body)
  [Width of "#body" is #size.width]
}

#thing[Hey] \
#thing[Welcome]
```

```typst
#context measure(lorem(100), width: 400pt)

#context measure(block(lorem(100), width: 400pt))
```