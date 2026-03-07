---
url: https://typst.app/docs/reference/foundations/dictionary/
category: foundations
topic: dictionary
---


# dictionary (foundations)

A map from string keys to values.

## Signature

`dictionary(module) -> dictionary value module Required Positional`

## Examples

```typst
#let dict = (
  name: "Typst",
  born: 2019,
)

#dict.name \
#(dict.launch = 20)
#dict.len() \
#dict.keys() \
#dict.values() \
#dict.at("born") \
#dict.insert("city", "Berlin")
#("name" in dict)
```

```typst
#dictionary(sys).at("version")
```