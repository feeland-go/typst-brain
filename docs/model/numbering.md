---
url: https://typst.app/docs/reference/model/numbering/
category: model
topic: numbering
---


# numbering (model)

Applies a numbering to a sequence of numbers.

## Signature

`numbering(strfunction, ..int) -> any`

## Parameters

- `numbering` (str | function, required): Defines how the numbering works.

- `numbers` (int, required): The numbers to apply the numbering to. Must be non-negative.

## Examples

```typst
#numbering("1.1)", 1, 2, 3) \
#numbering("1.a.i", 1, 2) \
#numbering("I – 1", 12, 2) \
#numbering(
  (..nums) => nums
    .pos()
    .map(str)
    .join(".") + ")",
  1, 2, 3,
)
```

```typst
#let unary(.., last) = "|" * last
#set heading(numbering: unary)
= First heading
= Second heading
= Third heading
```