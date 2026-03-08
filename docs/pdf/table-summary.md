---
url: https://typst.app/docs/reference/pdf/table-summary/
category: pdf
topic: table-summary
---


# table-summary (pdf)

A summary of the purpose and structure of a complex table.

## Signature

`pdf.table-summary(summary: str, content) -> content`

## Parameters

- `summary` (str | content, required): The table.

## Examples

```typst
#figure(
  pdf.table-summary(
    // The summary just provides orientation and structural
    // information for AT users.
    summary: "The first two columns list the names of each participant. The last column contains cells spanning multiple rows for their assigned group.",
    table(
      columns: 3,
      table.header[First Name][Given Name][Group],
      [Mike], [Davis], table.cell(rowspan: 3)[Sales],
      [Anna], [Smith],
      [John], [Johnson],
      [Sara], [Wilkins], table.cell(rowspan: 2)[Operations],
      [Tom], [Brown],
    ),
  ),
  // This is the key takeaway of the table, so we put it in the caption.
  caption: [The Sales org now has a new member],
)
```