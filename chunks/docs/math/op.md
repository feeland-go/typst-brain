---
url: https://typst.app/docs/reference/math/op/
category: math
topic: op
---


# op (math)

A text operator in an equation.

## Signature

`math.op(content, limits: bool) -> content`

## Parameters

- `text` (content, required): The operator's text.

- `limits` (bool, optional): Whether the operator should show attachments as limits in display mode.

## Examples

```typst
$ tan x = (sin x)/(cos x) $
$ op("custom",
     limits: #true)_(n->oo) n $
```