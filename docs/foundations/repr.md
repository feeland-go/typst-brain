---
url: https://typst.app/docs/reference/foundations/repr/
category: foundations
topic: repr
---


# repr (foundations)

Returns the string representation of a value.

## Signature

`repr(any) -> str`

## Parameters

- `value` (any, required): The value whose string representation to produce.

## Examples

```typst
#none vs #repr(none) \
#"hello" vs #repr("hello") \
#(1, 2) vs #repr((1, 2)) \
#[*Hi*] vs #repr([*Hi*])
```

```typst
#assert(2pt / 3 < 0.67pt)
#repr(2pt / 3)

#repr(x => x + 1)
```