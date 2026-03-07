---
url: https://typst.app/docs/reference/model/list/
category: model
topic: list
---


# list (model)

A bullet list.

## Signature

`list(tight: bool, marker: contentarrayfunction, indent: length, body-indent: length, spacing: autolength, ..content) -> content`

## Parameters

- `tight` (bool, optional): Defines the default spacing of the list. If it is false, the items are spaced apart with paragraph spacing. If it is true, they use paragraph leading instead. This makes the list more compact, which can look better if the items are short.

- `marker` (content | array | function, optional): The marker which introduces each item.

- `indent` (length, optional): The indent of each item.

- `body-indent` (length, optional): The spacing between the marker and the body of each item.

- `spacing` (auto | length, optional): The spacing between the items of the list.

- `children` (content, required): The bullet list's children.

## Examples

```typst
Normal list.
- Text
- Math
- Layout
- ...

Multiple lines.
- This list item spans multiple
  lines because it is indented.

Function call.
#list(
  [Foundations],
  [Calculate],
  [Construct],
  [Data Loading],
)
```

```typst
- If a list has a lot of text, and
  maybe other inline content, it
  should not be tight anymore.

- To make a list wide, simply insert
  a blank line between the items.
```

```typst
#set list(marker: [--])
- A more classic list
- With en-dashes

#set list(marker: ([•], [--]))
- Top-level
  - Nested
  - Items
- Items
```