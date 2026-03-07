---
url: https://typst.app/docs/reference/foundations/str/
category: foundations
topic: str
---


# str (foundations)

A sequence of Unicode codepoints.

## Signature

`str(intfloatstrbyteslabeldecimalversiontype, base: int) -> str value int or float or str or bytes or label or decimal or version or type Required Positional`

## Examples

```typst
#"hello world!" \
#"\"hello\n  world\"!" \
#"1 2 3".split() \
#"1,2;3".split(regex("[,;]")) \
#(regex("\\d+") in "ten euros") \
#(regex("\\d+") in "10 euros")
```

```typst
#str(10) \
#str(4000, base: 16) \
#str(2.7) \
#str(1e8) \
#str(<intro>)
```

```typst
#"a".to-unicode() \
#("a\u{0300}"
   .codepoints()
   .map(str.to-unicode))
```