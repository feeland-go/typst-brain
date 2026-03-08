---
url: https://typst.app/docs/reference/model/figure/
category: model
topic: figure
---


# figure (model)

A figure with an optional caption.

## Signature

`figure(content, alt: nonestr, placement: noneautoalignment, scope: str, caption: nonecontent, kind: autostrfunction, supplement: noneautocontentfunction, numbering: nonestrfunction, gap: length, outlined: bool) -> content`

## Parameters

- `body` (content, required): The content of the figure. Often, an image.

- `alt` (none | str, optional): An alternative description of the figure.

- `placement` (none | auto | alignment, optional): The figure's placement on the page.

- `scope` (str, optional): Relative to which containing scope the figure is placed.

- `caption` (none | content, optional): The figure's caption.

- `kind` (auto | str | function, optional): The kind of figure this is.

- `supplement` (none | auto | content | function, optional): The figure's supplement.

- `numbering` (none | str | function, optional): How to number the figure. Accepts a numbering pattern or function taking a single number.

- `gap` (length, optional): The vertical gap between the body and caption.

- `outlined` (bool, optional): Whether the figure should appear in an outline of figures.

## Examples

```typst
@glacier shows a glacier. Glaciers
are complex systems.

#figure(
  image("glacier.jpg", width: 80%),
  caption: [A curious figure.],
) <glacier>
```

```typst
#figure(
  table(
    columns: 4,
    [t], [1], [2], [3],
    [y], [0.3s], [0.4s], [0.8s],
  ),
  caption: [Timing results],
)
```

```typst
#show figure.caption: emph

#figure(
  rect[Hello],
  caption: [I am emphasized!],
)
```