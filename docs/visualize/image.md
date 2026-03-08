---
url: https://typst.app/docs/reference/visualize/image/
category: visualize
topic: image
---


# image (visualize)

A raster or vector graphic.

## Signature

`image(strbytes, format: autostrdictionary, width: autorelative, height: autorelativefraction, alt: nonestr, page: int, fit: str, scaling: autostr, icc: autostrbytes) -> content`

## Parameters

- `source` (str | bytes, required): A path to an image file or raw bytes making up an image in one of the supported formats.

- `format` (auto | str | dictionary, optional): The image's format.

- `width` (auto | relative, optional): The width of the image.

- `height` (auto | relative | fraction, optional): The height of the image.

- `alt` (none | str, optional): An alternative description of the image.

- `page` (int, optional): The page number that should be embedded as an image. This attribute only has an effect for PDF files.

- `fit` (str, optional): How the image should adjust itself to a given area (the area is defined by the width and height fields). Note that fit doesn't visually change anything if the area's aspect ratio is the same as the image's one.

- `scaling` (auto | str, optional): A hint to viewers how they should scale the image.

- `icc` (auto | str | bytes, optional): An ICC profile for the image.

## Examples

```typst
#figure(
  image("molecular.jpg", width: 80%),
  caption: [
    A step in the molecular testing
    pipeline of our lab.
  ],
)
```

```typst
#let original = read("diagram.svg")
#let changed = original.replace(
  "#2B80FF", // blue
  green.to-hex(),
)

#image(bytes(original))
#image(bytes(changed))
```

```typst
#image(
  read(
    "tetrahedron.svg",
    encoding: none,
  ),
  format: "svg",
  width: 2cm,
)

#image(
  bytes(range(16).map(x => x * 16)),
  format: (
    encoding: "luma8",
    width: 4,
    height: 4,
  ),
  width: 2cm,
)
```