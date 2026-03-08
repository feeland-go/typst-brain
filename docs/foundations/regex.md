---
url: https://typst.app/docs/reference/foundations/regex/
category: foundations
topic: regex
---


# regex (foundations)

A regular expression.

## Signature

`regex(str) -> regex regex str Required Positional`

## Examples

```typst
// Works with string methods.
#"a,b;c".split(regex("[,;]"))

// Works with show rules.
#show regex("\\d+"): set text(red)

The numbers 1 to 10.
```