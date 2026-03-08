---
url: https://typst.app/docs/reference/layout/layout/
category: layout
topic: layout
---


# layout (layout)

Provides access to the current outer container's (or page's, if none) dimensions (width and height).

## Signature

`layout(function) -> content`

## Parameters

- `func` (function, required): A function to call with the outer container's size. Its return value is displayed in the document.

## Examples

```typst
#let text = lorem(30)
#layout(size => [
  #let (height,) = measure(
    width: size.width,
    text,
  )
  This text is #height high with
  the current page width: \
  #text
])
```

```typst
#set page(height: 150pt)

#lorem(20)

#block(height: 1fr, layout(size => [
  Remaining height: #size.height
]))
```

```typst
#layout(size => {
  let half = 50% * size.width
  [Half a page is #half wide.]
})
```