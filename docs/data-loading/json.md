---
url: https://typst.app/docs/reference/data-loading/json/
category: data-loading
topic: json
---


# json (data-loading)

Reads structured data from a JSON file.

## Signature

`json(strbytes) -> any`

## Parameters

- `source` (str | bytes, required): A path to a JSON file or raw JSON bytes.

## Examples

```typst
#let forecast(day) = block[
  #box(square(
    width: 2cm,
    inset: 8pt,
    fill: if day.weather == "sunny" {
      yellow
    } else {
      aqua
    },
    align(
      bottom + right,
      strong(day.weather),
    ),
  ))
  #h(6pt)
  #set text(22pt, baseline: -8pt)
  #day.temperature °#day.unit
]

#forecast(json("monday.json"))
#forecast(json("tuesday.json"))
```