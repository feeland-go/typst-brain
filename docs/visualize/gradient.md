---
url: https://typst.app/docs/reference/visualize/gradient/
category: visualize
topic: gradient
---


# gradient (visualize)

A color gradient.

## Signature

`gradient.linear(..colorarray, space: any, relative: autostr, direction, angle) -> gradient stops color or array Required Positional Variadic`

## Examples

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  square(fill: gradient.linear(..color.map.rainbow)),
  square(fill: gradient.radial(..color.map.rainbow)),
  square(fill: gradient.conic(..color.map.rainbow)),
)
```

```typst
#set text(fill: gradient.linear(red, blue))
#let rainbow(content) = {
  set text(fill: gradient.linear(..color.map.rainbow))
  box(content)
}

This is a gradient on text, but with a #rainbow[twist]!
```

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  square(fill: gradient.linear(red, blue, angle: 0deg)),
  square(fill: gradient.linear(red, blue, angle: 90deg)),
  square(fill: gradient.linear(red, blue, angle: 180deg)),
  square(fill: gradient.linear(red, blue, angle: 270deg)),
)
```