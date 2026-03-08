---
url: https://typst.app/docs/reference/layout/page/
category: layout
topic: page
---


# page (layout)

Layouts its child onto one or multiple pages.

## Signature

`page(paper: str, width: autolength, height: autolength, flipped: bool, margin: autorelativedictionary, binding: autoalignment, columns: int, fill: noneautocolorgradienttiling, numbering: nonestrfunction, supplement: noneautocontent, number-align: alignment, header: noneautocontent, header-ascent: relative, footer: noneautocontent, footer-descent: relative, background: nonecontent, foreground: nonecontent, body: content) -> content`

## Parameters

- `paper` (str, optional): A standard paper size to set width and height.

- `width` (auto | length, optional): The width of the page.

- `height` (auto | length, optional): The height of the page.

- `flipped` (bool, optional): Whether the page is flipped into landscape orientation.

- `margin` (auto | relative | dictionary, optional): The page's margins.

- `binding` (auto | alignment, optional): On which side the pages will be bound.

- `columns` (int, optional): How many columns the page has.

- `fill` (none | auto | color | gradient | tiling, optional): The page's background fill.

- `numbering` (none | str | function, optional): How to number the pages. You can refer to the Page Setup Guide for customizing page numbers.

- `supplement` (none | auto | content, optional): A supplement for the pages.

- `number-align` (alignment, optional): The alignment of the page numbering.

- `header` (none | auto | content, optional): The page's header. Fills the top margin of each page.

- `header-ascent` (relative, optional): The amount the header is raised into the top margin.

- `footer` (none | auto | content, optional): The page's footer. Fills the bottom margin of each page.

- `footer-descent` (relative, optional): The amount the footer is lowered into the bottom margin.

- `background` (none | content, optional): Content in the page's background.

- `foreground` (none | content, optional): Content in the page's foreground.

- `body` (content, optional): The contents of the page(s).

## Examples

```typst
#set page("us-letter")

There you go, US friends!
```

```typst
#set page(
  width: 3cm,
  margin: (x: 0cm),
)

#for i in range(3) {
  box(square(width: 1cm))
}
```

```typst
#set page(
  "us-business-card",
  flipped: true,
  fill: rgb("f2e5dd"),
)

#set align(bottom + end)
#text(14pt)[*Sam H. Richards*] \
_Procurement Manager_

#set text(10pt)
17 Main Street \
New York, NY 10001 \
+1 555 555 5555
```