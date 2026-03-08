---
url: https://typst.app/docs/reference/visualize/color/
category: visualize
topic: color
---


# color (visualize)

A color in a specific color space.

## Signature

`color.luma(intratio, ratio, color) -> color lightness int or ratio Required Positional`

## Examples

```typst
#rect(fill: aqua)
```

```typst
#circle(fill: gradient.linear(..color.map.crest))
```

```typst
#for x in range(250, step: 50) {
  box(square(fill: luma(x)))
}
```