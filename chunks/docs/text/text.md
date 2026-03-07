---
url: https://typst.app/docs/reference/text/text/
category: text
topic: text
---

[  ] 
   
  [Reference] 
   
  [Text] 
   
  [Text] 
  

# `text`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Customizes the look and layout of text in a variety of ways.
 

This function is used frequently, both with set rules and directly. While the set rule is often the simpler choice, calling the `text` function directly can be useful when passing text as an argument to another function.
 

## Example 
```
#set text(18pt)
With a set rule.

#emph(text(blue)[
  With a function call.
])

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    text([font: ][str][array][dictionary],[fallback: ][bool],[style: ][str],[weight: ][int][str],[stretch: ][ratio],[size: ][length],[fill: ][color][gradient][tiling],[stroke: ][none][length][color][gradient][stroke][tiling][dictionary],[tracking: ][length],[spacing: ][relative],[cjk-latin-spacing: ][none][auto],[baseline: ][length],[overhang: ][bool],[top-edge: ][length][str],[bottom-edge: ][length][str],[lang: ][str],[region: ][none][str],[script: ][auto][str],[dir: ][auto][direction],[hyphenate: ][auto][bool],[costs: ][dictionary],[kerning: ][bool],[alternates: ][bool],[stylistic-set: ][none][int][array],[ligatures: ][bool],[discretionary-ligatures: ][bool],[historical-ligatures: ][bool],[number-type: ][auto][str],[number-width: ][auto][str],[slashed-zero: ][bool],[fractions: ][bool],[features: ][array][dictionary],[body: ][content],[str],) -> [content]  

### `font`   [str] or [array] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

A font family descriptor or priority list of font family descriptors.
 

A font family descriptor can be a plain string representing the family name or a dictionary with the following keys:
  `name` (required): The font family name.
 `covers` (optional): Defines the Unicode codepoints for which the family shall be used. This can be:  A predefined coverage set:  `"latin-in-cjk"` covers all codepoints except for those which exist in Latin fonts, but should preferably be taken from CJK fonts.
  
 A [regular expression] that defines exactly which codepoints shall be covered. Accepts only the subset of regular expressions which consist of exactly one dot, letter, or character class.
  
  

When processing text, Typst tries all specified font families in order until it finds a font that has the necessary glyphs. In the example below, the font `Inria Serif` is preferred, but since it does not contain Arabic glyphs, the arabic text uses `Noto Sans Arabic` instead.
 

The collection of available fonts differs by platform:
   

In the web app, you can see the list of available fonts by clicking on the "Ag" button. You can provide additional fonts by uploading `.ttf` or `.otf` files into your project. They will be discovered automatically. The priority is: project fonts > server fonts.
 
  

Locally, Typst uses your installed system fonts or embedded fonts in the CLI, which are `Libertinus Serif`, `New Computer Modern`, `New Computer Modern Math`, and `DejaVu Sans Mono`. In addition, you can use the `--font-path` argument or `TYPST_FONT_PATHS` environment variable to add directories that should be scanned for fonts. The priority is: `--font-paths` > system fonts > embedded fonts. Run `typst fonts` to see the fonts that Typst has discovered on your system. Note that you can pass the `--ignore-system-fonts` parameter to the CLI to ensure Typst won't search for system fonts.
 
    View example   
```
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
   

 Default: `"libertinus serif"` 
 

### `fallback`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to allow last resort font fallback when the primary font list contains no match. This lets Typst search through all available fonts for the most similar one that has the necessary glyphs.
 

Note: Currently, there are no warnings when fallback is disabled and no glyphs are found. Instead, your text shows up in the form of "tofus": Small boxes that indicate the lack of an appropriate glyph. In the future, you will be able to instruct Typst to issue warnings so you know something is up.
   View example   
```
#set text(font: "Inria Serif")
هذا عربي

#set text(fallback: false)
هذا عربي

```
   

 Default: `true` 
 

### `style`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The desired font style.
 

When an italic style is requested and only an oblique one is available, it is used. Similarly, the other way around, an italic style can stand in for an oblique one. When neither an italic nor an oblique style is available, Typst selects the normal style. Since most fonts are only available either in an italic or oblique style, the difference between italic and oblique style is rarely observable.
 

If you want to emphasize your text, you should do so using the [emph] function instead. This makes it easy to adapt the style later if you change your mind about how to signify the emphasis.
   View example   
```
#text(font: "Libertinus Serif", style: "italic")[Italic]
#text(font: "DejaVu Sans", style: "oblique")[Oblique]

```
   VariantDetails`"normal"`

The default, typically upright style.
`"italic"`

A cursive style with custom letterform.
`"oblique"`

Just a slanted version of the normal style.
 

 Default: `"normal"` 
 

### `weight`   [int] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The desired thickness of the font's glyphs. Accepts an integer between `100` and `900` or one of the predefined weight names. When the desired weight is not available, Typst selects the font from the family that is closest in weight.
 

If you want to strongly emphasize your text, you should do so using the [strong] function instead. This makes it easy to adapt the style later if you change your mind about how to signify the strong emphasis.
   View example   
```
#set text(font: "IBM Plex Sans")

#text(weight: "light")[Light] \
#text(weight: "regular")[Regular] \
#text(weight: "medium")[Medium] \
#text(weight: 500)[Medium] \
#text(weight: "bold")[Bold]

```
   VariantDetails`"thin"`

Thin weight (100).
`"extralight"`

Extra light weight (200).
`"light"`

Light weight (300).
`"regular"`

Regular weight (400).
`"medium"`

Medium weight (500).
`"semibold"`

Semibold weight (600).
`"bold"`

Bold weight (700).
`"extrabold"`

Extrabold weight (800).
`"black"`

Black weight (900).
 

 Default: `"regular"` 
 

### `stretch`   [ratio]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The desired width of the glyphs. Accepts a ratio between `50%` and `200%`. When the desired width is not available, Typst selects the font from the family that is closest in stretch. This will only stretch the text if a condensed or expanded version of the font is available.
 

If you want to adjust the amount of space between characters instead of stretching the glyphs itself, use the [`tracking`] property instead.
   View example   
```
#text(stretch: 75%)[Condensed] \
#text(stretch: 100%)[Normal]

```
   

 Default: `100%` 
 

### `size`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The size of the glyphs. This value forms the basis of the `em` unit: `1em` is equivalent to the font size.
 

You can also give the font size itself in `em` units. Then, it is relative to the previous font size.
   View example   
```
#set text(size: 20pt)
very #text(1.5em)[big] text

```
   

 Default: `11pt` 
 

### `fill`   [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The glyph fill paint.
   View example   
```
#set text(fill: red)
This text is red.

```
   

 Default: `luma(0%)` 
 

### `stroke`   [none] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How to stroke the text.
   View example   
```
#text(stroke: 0.5pt + red)[Stroked]

```
   

 Default: `none` 
 

### `tracking`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The amount of space that should be added between characters.
   View example   
```
#set text(tracking: 1.5pt)
Distant text.

```
   

 Default: `0pt` 
 

### `spacing`   [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The amount of space between words.
 

Can be given as an absolute length, but also relative to the width of the space character in the font.
 

If you want to adjust the amount of space between characters rather than words, use the [`tracking`] property instead.
   View example   
```
#set text(spacing: 200%)
Text with distant words.

```
   

 Default: `100% + 0pt` 
 

### `cjk-latin-spacing`   [none] or [auto]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to automatically insert spacing between CJK and Latin characters.
   View example   
```
#set text(cjk-latin-spacing: auto)
第4章介绍了基本的API。

#set text(cjk-latin-spacing: none)
第4章介绍了基本的API。

```
   

 Default: `auto` 
 

### `baseline`   [length]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

An amount to shift the text baseline by.
   View example   
```
A #text(baseline: 3pt)[lowered]
word.

```
   

 Default: `0pt` 
 

### `overhang`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether certain glyphs can hang over into the margin in justified text. This can make justification visually more pleasing.
   View example   
```
#set page(width: 220pt)

#set par(justify: true)
This justified text has a hyphen in
the paragraph's second line. Hanging
the hyphen slightly into the margin
results in a clearer paragraph edge.

#set text(overhang: false)
This justified text has a hyphen in
the paragraph's second line. Hanging
the hyphen slightly into the margin
results in a clearer paragraph edge.

```
   

 Default: `true` 
 

### `top-edge`   [length] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The top end of the conceptual frame around the text used for layout and positioning. This affects the size of containers that hold text.
   View example   
```
#set rect(inset: 0pt)
#set text(size: 20pt)

#set text(top-edge: "ascender")
#rect(fill: aqua)[Typst]

#set text(top-edge: "cap-height")
#rect(fill: aqua)[Typst]

```
   VariantDetails`"ascender"`

The font's ascender, which typically exceeds the height of all glyphs.
`"cap-height"`

The approximate height of uppercase letters.
`"x-height"`

The approximate height of non-ascending lowercase letters.
`"baseline"`

The baseline on which the letters rest.
`"bounds"`

The top edge of the glyph's bounding box.
 

 Default: `"cap-height"` 
 

### `bottom-edge`   [length] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The bottom end of the conceptual frame around the text used for layout and positioning. This affects the size of containers that hold text.
   View example   
```
#set rect(inset: 0pt)
#set text(size: 20pt)

#set text(bottom-edge: "baseline")
#rect(fill: aqua)[Typst]

#set text(bottom-edge: "descender")
#rect(fill: aqua)[Typst]

```
   VariantDetails`"baseline"`

The baseline on which the letters rest.
`"descender"`

The font's descender, which typically exceeds the depth of all glyphs.
`"bounds"`

The bottom edge of the glyph's bounding box.
 

 Default: `"baseline"` 
 

### `lang`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

An [ISO 639-1/2/3 language code.]
 

Setting the correct language affects various parts of Typst:
  The text processing pipeline can make more informed choices.
 Hyphenation will use the correct patterns for the language.
 [Smart quotes] turns into the correct quotes for the language.
 And all other things which are language-aware.
  

Choosing the correct language is important for accessibility. For example, screen readers will use it to choose a voice that matches the language of the text. If your document is in another language than English (the default), you should set the text language at the start of your document, before any other content. You can, for example, put it right after the `#set document(/* ... */)` rule that [sets your document's title].
 

If your document contains passages in a different language than the main language, you should locally change the text language just for those parts, either with a set rule [scoped to a block] or using a direct text function call such as `#text(lang: "de")[...]`.
 

If multiple codes are available for your language, you should prefer the two-letter code (ISO 639-1) over the three-letter codes (ISO 639-2/3). When you have to use a three-letter code and your language differs between ISO 639-2 and ISO 639-3, use ISO 639-2 for PDF 1.7 (Typst's default for PDF export) and below and ISO 639-3 for PDF 2.0 and HTML export.
 

The language code is case-insensitive, and will be lowercased when accessed through [context].
   View example: Setting the text language to German   
```
#set text(lang: "de")
#outline()

= Einleitung
In diesem Dokument, ...

```
   

 Default: `"en"` 
 

### `region`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

An [ISO 3166-1 alpha-2 region code.]
 

This lets the text processing pipeline make more informed choices.
 

The region code is case-insensitive, and will be uppercased when accessed through [context].
 

 Default: `none` 
 

### `script`   [auto] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The OpenType writing script.
 

The combination of `lang` and `script` determine how font features, such as glyph substitution, are implemented. Frequently the value is a modified (all-lowercase) ISO 15924 script identifier, and the `math` writing script is used for features appropriate for mathematical symbols.
 

When set to `auto`, the default and recommended setting, an appropriate script is chosen for each block of characters sharing a common Unicode script property.
   View example   
```
#set text(
  font: "Libertinus Serif",
  size: 20pt,
)

#let scedilla = [Ş]
#scedilla // S with a cedilla

#set text(lang: "ro", script: "latn")
#scedilla // S with a subscript comma

#set text(lang: "ro", script: "grek")
#scedilla // S with a cedilla

```
   

 Default: `auto` 
 

### `dir`   [auto] or [direction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The dominant direction for text and inline objects. Possible values are:
  `auto`: Automatically infer the direction from the `lang` property.
 `ltr`: Layout text from left to right.
 `rtl`: Layout text from right to left.
  

When writing in right-to-left scripts like Arabic or Hebrew, you should set the [text language] or direction. While individual runs of text are automatically layouted in the correct direction, setting the dominant direction gives the bidirectional reordering algorithm the necessary information to correctly place punctuation and inline objects. Furthermore, setting the direction affects the alignment values `start` and `end`, which are equivalent to `left` and `right` in `ltr` text and the other way around in `rtl` text.
 

If you set this to `rtl` and experience bugs or in some way bad looking output, please get in touch with us through the [Forum], [Discord server], or our [contact form].
   View example   
```
#set text(dir: rtl)
هذا عربي.

```
   

 Default: `auto` 
 

### `hyphenate`   [auto] or [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to hyphenate text to improve line breaking. When `auto`, text will be hyphenated if and only if justification is enabled.
 

Setting the [text language] ensures that the correct hyphenation patterns are used.
   View example   
```
#set page(width: 200pt)

#set par(justify: true)
This text illustrates how
enabling hyphenation can
improve justification.

#set text(hyphenate: false)
This text illustrates how
enabling hyphenation can
improve justification.

```
   

 Default: `auto` 
 

### `costs`   [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The "cost" of various choices when laying out text. A higher cost means the layout engine will make the choice less often. Costs are specified as a ratio of the default cost, so `50%` will make text layout twice as eager to make a given choice, while `200%` will make it half as eager.
 

Currently, the following costs can be customized:
  `hyphenation`: splitting a word across multiple lines
 `runt`: ending a paragraph with a line with a single word
 `widow`: leaving a single line of paragraph on the next page
 `orphan`: leaving single line of paragraph on the previous page
  

Hyphenation is generally avoided by placing the whole word on the next line, so a higher hyphenation cost can result in awkward justification spacing. Note: Hyphenation costs will only be applied when the [`linebreaks`] are set to "optimized". (For example by default implied by [`justify`].)
 

Runts are avoided by placing more or fewer words on previous lines, so a higher runt cost can result in more awkward in justification spacing.
 

Text layout prevents widows and orphans by default because they are generally discouraged by style guides. However, in some contexts they are allowed because the prevention method, which moves a line to the next page, can result in an uneven number of lines between pages. The `widow` and `orphan` costs allow disabling these modifications. (Currently, `0%` allows widows/orphans; anything else, including the default of `100%`, prevents them. More nuanced cost specification for these modifications is planned for the future.)
   View example   
```
#set text(hyphenate: true, size: 11.4pt)
#set par(justify: true)

#lorem(10)

// Set hyphenation to ten times the normal cost.
#set text(costs: (hyphenation: 1000%))

#lorem(10)

```
   

 Default: `( hyphenation: 100%, runt: 100%, widow: 100%, orphan: 100%, )` 
 

### `kerning`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to apply kerning.
 

When enabled, specific letter pairings move closer together or further apart for a more visually pleasing result. The example below demonstrates how decreasing the gap between the "T" and "o" results in a more natural look. Setting this to `false` disables kerning by turning off the OpenType `kern` font feature.
   View example   
```
#set text(size: 25pt)
Totally

#set text(kerning: false)
Totally

```
   

 Default: `true` 
 

### `alternates`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to apply stylistic alternates.
 

Sometimes fonts contain alternative glyphs for the same codepoint. Setting this to `true` switches to these by enabling the OpenType `salt` font feature.
   View example   
```
#set text(
  font: "IBM Plex Sans",
  size: 20pt,
)

0, a, g, ß

#set text(alternates: true)
0, a, g, ß

```
   

 Default: `false` 
 

### `stylistic-set`   [none] or [int] or [array]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Which stylistic sets to apply. Font designers can categorize alternative glyphs forms into stylistic sets. As this value is highly font-specific, you need to consult your font to know which sets are available.
 

This can be set to an integer or an array of integers, all of which must be between `1` and `20`, enabling the corresponding OpenType feature(s) from `ss01` to `ss20`. Setting this to `none` will disable all stylistic sets.
   View example   
```
#set text(font: "IBM Plex Serif")
ß vs #text(stylistic-set: 5)[ß] \
10 years ago vs #text(stylistic-set: (1, 2, 3))[10 years ago]

```
   

 Default: `()` 
 

### `ligatures`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether standard ligatures are active.
 

Certain letter combinations like "fi" are often displayed as a single merged glyph called a ligature. Setting this to `false` disables these ligatures by turning off the OpenType `liga` and `clig` font features.
   View example   
```
#set text(size: 20pt)
A fine ligature.

#set text(ligatures: false)
A fine ligature.

```
   

Note that some programming fonts use other OpenType font features to implement "ligatures," including the contextual alternates (`calt`) feature, which is also enabled by default. Use the general [`features`] parameter to control such features.
 

 Default: `true` 
 

### `discretionary-ligatures`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether ligatures that should be used sparingly are active. Setting this to `true` enables the OpenType `dlig` font feature.
 

 Default: `false` 
 

### `historical-ligatures`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether historical ligatures are active. Setting this to `true` enables the OpenType `hlig` font feature.
 

 Default: `false` 
 

### `number-type`   [auto] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Which kind of numbers / figures to select. When set to `auto`, the default numbers for the font are used.
   View example   
```
#set text(font: "Noto Sans", 20pt)
#set text(number-type: "lining")
Number 9.

#set text(number-type: "old-style")
Number 9.

```
   VariantDetails`"lining"`

Numbers that fit well with capital text (the OpenType `lnum` font feature).
`"old-style"`

Numbers that fit well into a flow of upper- and lowercase text (the OpenType `onum` font feature).
 

 Default: `auto` 
 

### `number-width`   [auto] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The width of numbers / figures. When set to `auto`, the default numbers for the font are used.
   View example   
```
#set text(font: "Noto Sans", 20pt)
#set text(number-width: "proportional")
A 12 B 34. \
A 56 B 78.

#set text(number-width: "tabular")
A 12 B 34. \
A 56 B 78.

```
   VariantDetails`"proportional"`

Numbers with glyph-specific widths (the OpenType `pnum` font feature).
`"tabular"`

Numbers of equal width (the OpenType `tnum` font feature).
 

 Default: `auto` 
 

### `slashed-zero`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to have a slash through the zero glyph. Setting this to `true` enables the OpenType `zero` font feature.
   View example   
```
0, #text(slashed-zero: true)[0]

```
   

 Default: `false` 
 

### `fractions`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to turn numbers into fractions. Setting this to `true` enables the OpenType `frac` font feature.
 

It is not advisable to enable this property globally as it will mess with all appearances of numbers after a slash (e.g., in URLs). Instead, enable it locally when you want a fraction.
   View example   
```
1/2 \
#text(fractions: true)[1/2]

```
   

 Default: `false` 
 

### `features`   [array] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Raw OpenType features to apply.
  If given an array of strings, sets the features identified by the strings to `1`.
 If given a dictionary mapping to numbers, sets the features identified by the keys to the values.
    View example: Give an array of strings   
```
// Enable the `frac` feature manually.
#set text(features: ("frac",))
1/2

```
      View example: Give a dictionary mapping to numbers   
```
#set text(font: "Cascadia Code")
=>
// Disable the contextual alternates (`calt`) feature.
#set text(features: (calt: 0))
=>

```
   

 Default: `(:)` 
 

### `body`   [content]    

Content in which all text is styled according to the other arguments.
 

 Default: `[]` 
 

### `text`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The text.
 [SuperscriptPrevious page] [UnderlineNext page]