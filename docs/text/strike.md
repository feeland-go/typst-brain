---
url: https://typst.app/docs/reference/text/strike/
category: text
topic: strike
---


# strike (text)

Strikes through text.

## Signature

`strike(stroke: autolengthcolorgradientstroketilingdictionary, offset: autolength, extent: length, background: bool, content) -> content`

## Parameters

- `stroke` (auto | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the line.

- `offset` (auto | length, optional): The position of the line relative to the baseline. Read from the font tables if auto.

- `extent` (length, optional): The amount by which to extend the line beyond (or within if negative) the content.

- `background` (bool, optional): Whether the line is placed behind the content.

- `body` (content, required): The content to strike through.

## Examples

```typst
This is #strike[not] relevant.
```

```typst
This is #strike(stroke: 1.5pt + red)[very stricken through]. \
This is #strike(stroke: 10pt)[redacted].
```

```typst
#set text(font: "Inria Serif")
This is #strike(offset: auto)[low-ish]. \
This is #strike(offset: -3.5pt)[on-top].
```