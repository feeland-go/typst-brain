---
url: https://typst.app/docs/reference/text/text/
category: text
topic: text
---


# text (text)

Customizes the look and layout of text in a variety of ways.

## Signature

`text(font: strarraydictionary, fallback: bool, style: str, weight: intstr, stretch: ratio, size: length, fill: colorgradienttiling, stroke: nonelengthcolorgradientstroketilingdictionary, tracking: length, spacing: relative, cjk-latin-spacing: noneauto, baseline: length, overhang: bool, top-edge: lengthstr, bottom-edge: lengthstr, lang: str, region: nonestr, script: autostr, dir: autodirection, hyphenate: autobool, costs: dictionary, kerning: bool, alternates: bool, stylistic-set: noneintarray, ligatures: bool, discretionary-ligatures: bool, historical-ligatures: bool, number-type: autostr, number-width: autostr, slashed-zero: bool, fractions: bool, features: arraydictionary, body: content, str) -> content`

## Parameters

- `font` (str | array | dictionary, optional): A font family descriptor or priority list of font family descriptors.

- `fallback` (bool, optional): Whether to allow last resort font fallback when the primary font list contains no match. This lets Typst search through all available fonts for the most similar one that has the necessary glyphs.

- `style` (str, optional): The desired font style.

- `weight` (int | str, optional): The desired thickness of the font's glyphs. Accepts an integer between 100 and 900 or one of the predefined weight names. When the desired weight is not available, Typst selects the font from the family that is closest in weight.

- `stretch` (ratio, optional): The desired width of the glyphs. Accepts a ratio between 50% and 200%. When the desired width is not available, Typst selects the font from the family that is closest in stretch. This will only stretch the text if a condensed or expanded version of the font is available.

- `size` (length, optional): The size of the glyphs. This value forms the basis of the em unit: 1em is equivalent to the font size.

- `fill` (color | gradient | tiling, optional): The glyph fill paint.

- `stroke` (none | length | color | gradient | stroke | tiling | dictionary, optional): How to stroke the text.

- `tracking` (length, optional): The amount of space that should be added between characters.

- `spacing` (relative, optional): The amount of space between words.

- `cjk-latin-spacing` (none | auto, optional): Whether to automatically insert spacing between CJK and Latin characters.

- `baseline` (length, optional): An amount to shift the text baseline by.

- `overhang` (bool, optional): Whether certain glyphs can hang over into the margin in justified text. This can make justification visually more pleasing.

- `top-edge` (length | str, optional): The top end of the conceptual frame around the text used for layout and positioning. This affects the size of containers that hold text.

- `bottom-edge` (length | str, optional): The bottom end of the conceptual frame around the text used for layout and positioning. This affects the size of containers that hold text.

- `lang` (str, optional): An ISO 639-1/2/3 language code.

- `region` (none | str, optional): An ISO 3166-1 alpha-2 region code.

- `script` (auto | str, optional): The OpenType writing script.

- `dir` (auto | direction, optional): The dominant direction for text and inline objects. Possible values are:

- `hyphenate` (auto | bool, optional): Whether to hyphenate text to improve line breaking. When auto, text will be hyphenated if and only if justification is enabled.

- `costs` (dictionary, optional): The "cost" of various choices when laying out text. A higher cost means the layout engine will make the choice less often. Costs are specified as a ratio of the default cost, so 50% will make text layout twice as eager to make a given choice, while 200% will make it half as eager.

- `kerning` (bool, optional): Whether to apply kerning.

- `alternates` (bool, optional): Whether to apply stylistic alternates.

- `stylistic-set` (none | int | array, optional): Which stylistic sets to apply. Font designers can categorize alternative glyphs forms into stylistic sets. As this value is highly font-specific, you need to consult your font to know which sets are available.

- `ligatures` (bool, optional): Whether standard ligatures are active.

- `discretionary-ligatures` (bool, optional): Whether ligatures that should be used sparingly are active. Setting this to true enables the OpenType dlig font feature.

- `historical-ligatures` (bool, optional): Whether historical ligatures are active. Setting this to true enables the OpenType hlig font feature.

- `number-type` (auto | str, optional): Which kind of numbers / figures to select. When set to auto, the default numbers for the font are used.

- `number-width` (auto | str, optional): The width of numbers / figures. When set to auto, the default numbers for the font are used.

- `slashed-zero` (bool, optional): Whether to have a slash through the zero glyph. Setting this to true enables the OpenType zero font feature.

- `fractions` (bool, optional): Whether to turn numbers into fractions. Setting this to true enables the OpenType frac font feature.

- `features` (array | dictionary, optional): Raw OpenType features to apply.

- `body` (content, optional): Content in which all text is styled according to the other arguments.

- `text` (str, required): The text.

## Examples

```typst
#set text(18pt)
With a set rule.

#emph(text(blue)[
  With a function call.
])
```

```typst
#set text(font: "PT Sans")
This is sans-serif.

#set text(font: (
  "Inria Serif",
  "Noto Sans Arabic",
))

This is Latin. \
هذا عربي.

// Change font only for numbers.
#set text(font: (
  (name: "PT Sans", covers: regex("[0-9]")),
  "Libertinus Serif"
))

The number 123.

// Mix Latin and CJK fonts.
#set text(font: (
  (name: "Inria Serif", covers: "latin-in-cjk"),
  "Noto Serif CJK SC"
))
分别设置“中文”和English字体
```

```typst
#set text(font: "Inria Serif")
هذا عربي

#set text(fallback: false)
هذا عربي
```