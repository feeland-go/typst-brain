---
url: https://typst.app/docs/reference/layout/scale/
category: layout
topic: scale
---


# scale (layout)

Scales content without affecting layout.

## Signature

`scale(factor: autolengthratio, x: autolengthratio, y: autolengthratio, origin: alignment, reflow: bool, content) -> content`

## Parameters

- `factor` (auto | length | ratio, optional): The scaling factor for both axes, as a positional argument. This is just an optional shorthand notation for setting x and y to the same value.

- `x` (auto | length | ratio, optional): The horizontal scaling factor.

- `y` (auto | length | ratio, optional): The vertical scaling factor.

- `origin` (alignment, optional): The origin of the transformation.

- `reflow` (bool, optional): Whether the scaling impacts the layout.

- `body` (content, required): The content to scale.

## Examples

```typst
#set align(center)
#scale(x: -100%)[This is mirrored.]
#scale(x: -100%, reflow: true)[This is mirrored.]
```

```typst
A#box(scale(75%)[A])A \
B#box(scale(75%, origin: bottom + left)[B])B
```

```typst
Hello #scale(x: 20%, y: 40%, reflow: true)[World]!
```