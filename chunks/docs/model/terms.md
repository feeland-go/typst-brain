---
url: https://typst.app/docs/reference/model/terms/
category: model
topic: terms
---


# terms (model)

A list of terms and their descriptions.

## Signature

`terms(tight: bool, separator: content, indent: length, hanging-indent: length, spacing: autolength, ..contentarray) -> content`

## Parameters

- `tight` (bool, optional): Defines the default spacing of the term list. If it is false, the items are spaced apart with paragraph spacing. If it is true, they use paragraph leading instead. This makes the list more compact, which can look better if the items are short.

- `separator` (content, optional): The separator between the item and the description.

- `indent` (length, optional): The indentation of each item.

- `hanging-indent` (length, optional): The hanging indent of the description.

- `spacing` (auto | length, optional): The spacing between the items of the term list.

- `children` (content | array, required): The term list's children.

## Examples

```typst
/ Ligature: A merged glyph.
/ Kerning: A spacing adjustment
  between two adjacent letters.
```

```typst
/ Fact: If a term list has a lot
  of text, and maybe other inline
  content, it should not be tight
  anymore.

/ Tip: To make it wide, simply
  insert a blank line between the
  items.
```

```typst
#set terms(separator: [: ])

/ Colon: A nice separator symbol.
```