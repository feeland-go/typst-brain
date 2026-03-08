---
url: https://typst.app/docs/reference/math/binom/
category: math
topic: binom
---


# binom (math)

A binomial expression.

## Signature

`math.binom(content, ..content) -> content`

## Parameters

- `upper` (content, required): The binomial's upper index.

- `lower` (content, required): The binomial's lower index.

## Examples

```typst
$ binom(n, k) $
$ binom(n, k_1, k_2, k_3, ..., k_m) $
```