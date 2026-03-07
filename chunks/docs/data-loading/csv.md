---
url: https://typst.app/docs/reference/data-loading/csv/
category: data-loading
topic: csv
---


# csv (data-loading)

Reads structured data from a CSV file.

## Signature

`csv(strbytes, delimiter: str, row-type: type) -> array`

## Parameters

- `source` (str | bytes, required): A path to a CSV file or raw CSV bytes.

- `delimiter` (str, optional): The delimiter that separates columns in the CSV file. Must be a single ASCII character.

- `row-type` (type, optional): How to represent the file's rows.

## Examples

```typst
#let results = csv("example.csv")

#table(
  columns: 2,
  [*Condition*], [*Result*],
  ..results.flatten(),
)
```