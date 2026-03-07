---
url: https://typst.app/docs/reference/visualize/color/
category: visualize
topic: color
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Color] 
  

#  color  

A color in a specific color space.
 

Typst supports:
  sRGB through the [`rgb` function]
 Device CMYK through the [`cmyk` function]
 D65 Gray through the [`luma` function]
 Oklab through the [`oklab` function]
 Oklch through the [`oklch` function]
 Linear RGB through the [`color.linear-rgb` function]
 HSL through the [`color.hsl` function]
 HSV through the [`color.hsv` function]
  

## Example 
```
#rect(fill: aqua)

```
 

## Predefined colors 

Typst defines the following built-in colors:
 ColorDefinition `black``luma(0)` `gray``luma(170)` `silver``luma(221)` `white``luma(255)` `navy``rgb("#001f3f")` `blue``rgb("#0074d9")` `aqua``rgb("#7fdbff")` `teal``rgb("#39cccc")` `eastern``rgb("#239dad")` `purple``rgb("#b10dc9")` `fuchsia``rgb("#f012be")` `maroon``rgb("#85144b")` `red``rgb("#ff4136")` `orange``rgb("#ff851b")` `yellow``rgb("#ffdc00")` `olive``rgb("#3d9970")` `green``rgb("#2ecc40")` `lime``rgb("#01ff70")`  

The predefined colors and the most important color constructors are available globally and also in the color type's scope, so you can write either `color.red` or just `red`.
  

## Predefined color maps 

Typst also includes a number of preset color maps that can be used for [gradients]. These are simply arrays of colors defined in the module `color.map`.
 
```
#circle(fill: gradient.linear(..color.map.crest))

```
MapDetails `turbo`A perceptually uniform rainbow-like color map. Read [this blog post] for more details. `cividis`A blue to gray to yellow color map. See [this blog post] for more details. `rainbow`Cycles through the full color spectrum. This color map is best used by setting the interpolation color space to [HSL]. The rainbow gradient is not suitable for data visualization because it is not perceptually uniform, so the differences between values become unclear to your readers. It should only be used for decorative purposes. `spectral`Red to yellow to blue color map. `viridis`A purple to teal to yellow color map. `inferno`A black to red to yellow color map. `magma`A black to purple to yellow color map. `plasma`A purple to pink to yellow color map. `rocket`A black to red to white color map. `mako`A black to teal to white color map. `vlag`A light blue to white to red color map. `icefire`A light teal to black to orange color map. `flare`A orange to purple color map that is perceptually uniform. `crest`A light green to blue color map.  

Some popular presets are not included because they are not available under a free licence. Others, like [Jet], are not included because they are not color blind friendly. Feel free to use or create a package with other presets that are useful to you!
  

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  

### `luma`

Create a grayscale color.
 

A grayscale color is represented internally by a single `lightness` component.
 

These components are also available using the [`components`] method.
   View example  
```
#for x in range(250, step: 50) {
  box(square(fill: luma(x)))
}

```
   color.luma([int][ratio],[ratio],[color],) -> [color]  `lightness`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The lightness component.
 `alpha`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The alpha component.
 `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to grayscale.
 

If this is given, the `lightness` should not be given.
 

### `oklab`

Create an [Oklab] color.
 

This color space is well suited for the following use cases:
  Color manipulation such as saturating while keeping perceived hue
 Creating grayscale images with uniform perceived lightness
 Creating smooth and uniform color transition and gradients
  

A linear Oklab color is represented internally by an array of four components:
  lightness ([`ratio`])
 a ([`float`] or [`ratio`]. Ratios are relative to `0.4`; meaning `50%` is equal to `0.2`)
 b ([`float`] or [`ratio`]. Ratios are relative to `0.4`; meaning `50%` is equal to `0.2`)
 alpha ([`ratio`])
  

These components are also available using the [`components`] method.
   View example  
```
#square(
  fill: oklab(27%, 20%, -3%, 50%)
)

```
   color.oklab([ratio],[float][ratio],[float][ratio],[ratio],[color],) -> [color]  `lightness`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The lightness component.
 `a`   [float] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The a ("green/red") component.
 `b`   [float] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The b ("blue/yellow") component.
 `alpha`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The alpha component.
 `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to Oklab.
 

If this is given, the individual components should not be given.
 

### `oklch`

Create an [Oklch] color.
 

This color space is well suited for the following use cases:
  Color manipulation involving lightness, chroma, and hue
 Creating grayscale images with uniform perceived lightness
 Creating smooth and uniform color transition and gradients
  

A linear Oklch color is represented internally by an array of four components:
  lightness ([`ratio`])
 chroma ([`float`] or [`ratio`]. Ratios are relative to `0.4`; meaning `50%` is equal to `0.2`)
 hue ([`angle`])
 alpha ([`ratio`])
  

These components are also available using the [`components`] method.
   View example  
```
#square(
  fill: oklch(40%, 0.2, 160deg, 50%)
)

```
   color.oklch([ratio],[float][ratio],[angle],[ratio],[color],) -> [color]  `lightness`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The lightness component.
 `chroma`   [float] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The chroma component.
 `hue`   [angle]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The hue component.
 `alpha`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The alpha component.
 `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to Oklch.
 

If this is given, the individual components should not be given.
 

### `linear-rgb`

Create an RGB(A) color with linear luma.
 

This color space is similar to sRGB, but with the distinction that the color component are not gamma corrected. This makes it easier to perform color operations such as blending and interpolation. Although, you should prefer to use the [`oklab` function] for these.
 

A linear RGB(A) color is represented internally by an array of four components:
  red ([`ratio`])
 green ([`ratio`])
 blue ([`ratio`])
 alpha ([`ratio`])
  

These components are also available using the [`components`] method.
   View example  
```
#square(fill: color.linear-rgb(
  30%, 50%, 10%,
))

```
   color.linear-rgb([int][ratio],[int][ratio],[int][ratio],[int][ratio],[color],) -> [color]  `red`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The red component.
 `green`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The green component.
 `blue`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The blue component.
 `alpha`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The alpha component.
 `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to linear RGB(A).
 

If this is given, the individual components should not be given.
 

### `rgb`

Create an RGB(A) color.
 

The color is specified in the sRGB color space.
 

An RGB(A) color is represented internally by an array of four components:
  red ([`ratio`])
 green ([`ratio`])
 blue ([`ratio`])
 alpha ([`ratio`])
  

These components are also available using the [`components`] method.
   View example  
```
#square(fill: rgb("#b1f2eb"))
#square(fill: rgb(87, 127, 230))
#square(fill: rgb(25%, 13%, 65%))

```
   color.rgb([int][ratio],[int][ratio],[int][ratio],[int][ratio],[str],[color],) -> [color]  `red`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The red component.
 `green`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The green component.
 `blue`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The blue component.
 `alpha`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The alpha component.
 `hex`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color in hexadecimal notation.
 

Accepts three, four, six or eight hexadecimal digits and optionally a leading hash.
 

If this is given, the individual components should not be given.
   View example   
```
#text(16pt, rgb("#239dad"))[
  *Typst*
]

```
   `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to RGB(a).
 

If this is given, the individual components should not be given.
 

### `cmyk`

Create a CMYK color.
 

This is useful if you want to target a specific printer. The conversion to RGB for display preview might differ from how your printer reproduces the color.
 

A CMYK color is represented internally by an array of four components:
  cyan ([`ratio`])
 magenta ([`ratio`])
 yellow ([`ratio`])
 key ([`ratio`])
  

These components are also available using the [`components`] method.
 

Note that CMYK colors are not currently supported when PDF/A output is enabled.
   View example  
```
#square(
  fill: cmyk(27%, 0%, 3%, 5%)
)

```
   color.cmyk([ratio],[ratio],[ratio],[ratio],[color],) -> [color]  `cyan`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The cyan component.
 `magenta`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The magenta component.
 `yellow`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The yellow component.
 `key`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The key component.
 `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to CMYK.
 

If this is given, the individual components should not be given.
 

### `hsl`

Create an HSL color.
 

This color space is useful for specifying colors by hue, saturation and lightness. It is also useful for color manipulation, such as saturating while keeping perceived hue.
 

An HSL color is represented internally by an array of four components:
  hue ([`angle`])
 saturation ([`ratio`])
 lightness ([`ratio`])
 alpha ([`ratio`])
  

These components are also available using the [`components`] method.
   View example  
```
#square(
  fill: color.hsl(30deg, 50%, 60%)
)

```
   color.hsl([angle],[int][ratio],[int][ratio],[int][ratio],[color],) -> [color]  `hue`   [angle]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The hue angle.
 `saturation`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The saturation component.
 `lightness`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The lightness component.
 `alpha`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The alpha component.
 `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to HSL.
 

If this is given, the individual components should not be given.
 

### `hsv`

Create an HSV color.
 

This color space is useful for specifying colors by hue, saturation and value. It is also useful for color manipulation, such as saturating while keeping perceived hue.
 

An HSV color is represented internally by an array of four components:
  hue ([`angle`])
 saturation ([`ratio`])
 value ([`ratio`])
 alpha ([`ratio`])
  

These components are also available using the [`components`] method.
   View example  
```
#square(
  fill: color.hsv(30deg, 50%, 60%)
)

```
   color.hsv([angle],[int][ratio],[int][ratio],[int][ratio],[color],) -> [color]  `hue`   [angle]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The hue angle.
 `saturation`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The saturation component.
 `value`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value component.
 `alpha`   [int] or [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The alpha component.
 `color`   [color]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

Alternatively: The color to convert to HSL.
 

If this is given, the individual components should not be given.
 

### `components`

Extracts the components of this color.
 

The size and values of this array depends on the color space. You can obtain the color space using [`space`]. Below is a table of the color spaces and their components:
 Color spaceC1C2C3C4 [`luma`]Lightness [`oklab`]Lightness`a``b`Alpha [`oklch`]LightnessChromaHueAlpha [`linear-rgb`]RedGreenBlueAlpha [`rgb`]RedGreenBlueAlpha [`cmyk`]CyanMagentaYellowKey [`hsl`]HueSaturationLightnessAlpha [`hsv`]HueSaturationValueAlpha  

For the meaning and type of each individual value, see the documentation of the corresponding color space. The alpha component is optional and only included if the `alpha` argument is `true`. The length of the returned array depends on the number of components and whether the alpha component is included.
   View example  
```
// note that the alpha component is included by default
#rgb(40%, 60%, 80%).components()

```
   self.components([alpha: ][bool]) -> [array]  `alpha`   [bool]    

Whether to include the alpha component.
 

 Default: `true` 
 

### `space`

Returns the constructor function for this color's space.
 

Returns one of:
  [`luma`]
 [`oklab`]
 [`oklch`]
 [`linear-rgb`]
 [`rgb`]
 [`cmyk`]
 [`hsl`]
 [`hsv`]
    View example  
```
#let color = cmyk(1%, 2%, 3%, 4%)
#(color.space() == cmyk)

```
   self.space() -> any  

### `to-hex`

Returns the color's RGB(A) hex representation (such as `#ffaa32` or `#020304fe`). The alpha component (last two digits in `#020304fe`) is omitted if it is equal to `ff` (255 / 100%).
 self.to-hex() -> [str]  

### `lighten`

Lightens a color by a given factor.
 self.lighten([ratio]) -> [color]  `factor`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The factor to lighten the color by.
 

### `darken`

Darkens a color by a given factor.
 self.darken([ratio]) -> [color]  `factor`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The factor to darken the color by.
 

### `saturate`

Increases the saturation of a color by a given factor.
 self.saturate([ratio]) -> [color]  `factor`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The factor to saturate the color by.
 

### `desaturate`

Decreases the saturation of a color by a given factor.
 self.desaturate([ratio]) -> [color]  `factor`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The factor to desaturate the color by.
 

### `negate`

Produces the complementary color using a provided color space. You can think of it as the opposite side on a color wheel.
   View example  
```
#square(fill: yellow)
#square(fill: yellow.negate())
#square(fill: yellow.negate(space: rgb))

```
   self.negate([space: ]any) -> [color]  `space`   any    

The color space used for the transformation. By default, a perceptual color space is used.
 

 Default: `oklab` 
 

### `rotate`

Rotates the hue of the color by a given angle.
 self.rotate([angle],[space: ]any,) -> [color]  `angle`   [angle]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The angle to rotate the hue by.
 `space`   any    

The color space used to rotate. By default, this happens in a perceptual color space ([`oklch`]).
 

 Default: `oklch` 
 

### `mix`

Create a color by mixing two or more colors.
 

In color spaces with a hue component (hsl, hsv, oklch), only two colors can be mixed at once. Mixing more than two colors in such a space will result in an error!
   View example  
```
#set block(height: 20pt, width: 100%)
#block(fill: red.mix(blue))
#block(fill: red.mix(blue, space: rgb))
#block(fill: color.mix(red, blue, white))
#block(fill: color.mix((red, 70%), (blue, 30%)))

```
   color.mix([..][color][array],[space: ]any,) -> [color]  `colors`   [color] or [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The colors, optionally with weights, specified as a pair (array of length two) of color and weight (float or ratio).
 

The weights do not need to add to `100%`, they are relative to the sum of all weights.
 `space`   any    

The color space to mix in. By default, this happens in a perceptual color space ([`oklab`]).
 

 Default: `oklab` 
 

### `transparentize`

Makes a color more transparent by a given factor.
 

This method is relative to the existing alpha value. If the scale is positive, calculates `alpha - alpha * scale`. Negative scales behave like `color.opacify(-scale)`.
   View example  
```
#block(fill: red)[opaque]
#block(fill: red.transparentize(50%))[half red]
#block(fill: red.transparentize(75%))[quarter red]

```
   self.transparentize([ratio]) -> [color]  `scale`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The factor to change the alpha value by.
 

### `opacify`

Makes a color more opaque by a given scale.
 

This method is relative to the existing alpha value. If the scale is positive, calculates `alpha + scale - alpha * scale`. Negative scales behave like `color.transparentize(-scale)`.
   View example  
```
#let half-red = red.transparentize(50%)
#block(fill: half-red.opacify(100%))[opaque]
#block(fill: half-red.opacify(50%))[three quarters red]
#block(fill: half-red.opacify(-50%))[one quarter red]

```
   self.opacify([ratio]) -> [color]  `scale`   [ratio]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The scale to change the alpha value by.
 [CirclePrevious page] [CurveNext page]