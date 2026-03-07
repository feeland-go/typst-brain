---
url: https://typst.app/docs/reference/visualize/image/
category: visualize
topic: image
---

[  ] 
   
  [Reference] 
   
  [Visualize] 
   
  [Image] 
  

# `image`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A raster or vector graphic.
 

You can wrap the image in a [`figure`] to give it a number and caption.
 

Like most elements, images are block-level by default and thus do not integrate themselves into adjacent paragraphs. To force an image to become inline, put it into a [`box`].
 

## Example 
```
#figure(
  image("molecular.jpg", width: 80%),
  caption: [
    A step in the molecular testing
    pipeline of our lab.
  ],
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    image([str][bytes],[format: ][auto][str][dictionary],[width: ][auto][relative],[height: ][auto][relative][fraction],[alt: ][none][str],[page: ][int],[fit: ][str],[scaling: ][auto][str],[icc: ][auto][str][bytes],) -> [content]  

### `source`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

A [path] to an image file or raw bytes making up an image in one of the supported [formats].
 

Bytes can be used to specify raw pixel data in a row-major, left-to-right, top-to-bottom format.
   View example   
```
#let original = read("diagram.svg")
#let changed = original.replace(
  "#2B80FF", // blue
  green.to-hex(),
)

#image(bytes(original))
#image(bytes(changed))

```
   

### `format`   [auto] or [str] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The image's format.
 

By default, the format is detected automatically. Typically, you thus only need to specify this when providing raw bytes as the [`source`] (even then, Typst will try to figure out the format automatically, but that's not always possible).
 

Supported formats are `"png"`, `"jpg"`, `"gif"`, `"svg"`, `"pdf"`, `"webp"` as well as raw pixel data.
 

Note that several restrictions apply when using PDF files as images:
  When exporting to PDF, any PDF image file used must have a version equal to or lower than the [export target PDF version].
 PDF files as images are currently not supported when exporting with a specific PDF standard, like PDF/A-3 or PDF/UA-1. In these cases, you can instead use SVGs to embed vector images.
 The image file must not be password-protected.
 Tags in your PDF image will not be preserved. Instead, you must provide an [alternative description] to make the image accessible.
  

When providing raw pixel data as the `source`, you must specify a dictionary with the following keys as the `format`:
  `encoding` ([str]): The encoding of the pixel data. One of:  `"rgb8"` (three 8-bit channels: red, green, blue)
 `"rgba8"` (four 8-bit channels: red, green, blue, alpha)
 `"luma8"` (one 8-bit channel)
 `"lumaa8"` (two 8-bit channels: luma and alpha)
  
 `width` ([int]): The pixel width of the image.
 `height` ([int]): The pixel height of the image.
  

The pixel width multiplied by the height multiplied by the channel count for the specified encoding must then match the `source` data.
   View example   
```
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
   VariantDetails`"png"`

Raster format for illustrations and transparent graphics.
`"jpg"`

Lossy raster format suitable for photos.
`"gif"`

Raster format that is typically used for short animated clips. Typst can load GIFs, but they will become static.
`"webp"`

Raster format that supports both lossy and lossless compression.
`"svg"`

The vector graphics format of the web.
`"pdf"`

High-fidelity document and graphics format, with focus on exact reproduction in print.
 

 Default: `auto` 
 

### `width`   [auto] or [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The width of the image.
 

 Default: `auto` 
 

### `height`   [auto] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The height of the image.
 

 Default: `auto` 
 

### `alt`   [none] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

An alternative description of the image.
 

This text is used by Assistive Technology (AT) like screen readers to describe the image to users with visual impairments.
 

When the image is wrapped in a [`figure`], use this parameter rather than the [figure's `alt` parameter] to describe the image. The only exception to this rule is when the image and the other contents in the figure form a single semantic unit. In this case, use the figure's `alt` parameter to describe the entire composition and do not use this parameter.
 

You can learn how to write good alternative descriptions in the [Accessibility Guide].
 

 Default: `none` 
 

### `page`   [int]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The page number that should be embedded as an image. This attribute only has an effect for PDF files.
 

 Default: `1` 
 

### `fit`   [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How the image should adjust itself to a given area (the area is defined by the `width` and `height` fields). Note that `fit` doesn't visually change anything if the area's aspect ratio is the same as the image's one.
   View example   
```
#set page(width: 300pt, height: 50pt, margin: 10pt)
#image("tiger.jpg", width: 100%, fit: "cover")
#image("tiger.jpg", width: 100%, fit: "contain")
#image("tiger.jpg", width: 100%, fit: "stretch")

```
     VariantDetails`"cover"`

The image should completely cover the area (preserves aspect ratio by cropping the image only horizontally or vertically). This is the default.
`"contain"`

The image should be fully contained in the area (preserves aspect ratio; doesn't crop the image; one dimension can be narrower than specified).
`"stretch"`

The image should be stretched so that it exactly fills the area, even if this means that the image will be distorted (doesn't preserve aspect ratio and doesn't crop the image).
 

 Default: `"cover"` 
 

### `scaling`   [auto] or [str]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

A hint to viewers how they should scale the image.
 

When set to `auto`, the default is left up to the viewer. For PNG export, Typst will default to smooth scaling, like most PDF and SVG viewers.
 

Note: The exact look may differ across PDF viewers.
 VariantDetails`"smooth"`

Scale with a smoothing algorithm such as bilinear interpolation.
`"pixelated"`

Scale with nearest neighbor or a similar algorithm to preserve the pixelated look of the image.
 

 Default: `auto` 
 

### `icc`   [auto] or [str] or [bytes]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

An ICC profile for the image.
 

ICC profiles define how to interpret the colors in an image. When set to `auto`, Typst will try to extract an ICC profile from the image.
 

 Default: `auto` 
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `decode` Warning  `image.decode` is deprecated, directly pass bytes to `image` instead; it will be removed in Typst 0.15.0

Decode a raster or vector graphic from bytes or a string.
 image.decode([str][bytes],[format: ][auto][str][dictionary],[width: ][auto][relative],[height: ][auto][relative][fraction],[alt: ][none][str],[fit: ][str],[scaling: ][auto][str],) -> [content]  `data`   [str] or [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The data to decode as an image. Can be a string for SVGs.
 `format`   [auto] or [str] or [dictionary]    

The image's format. Detected automatically by default.
 VariantDetails`"png"`

Raster format for illustrations and transparent graphics.
`"jpg"`

Lossy raster format suitable for photos.
`"gif"`

Raster format that is typically used for short animated clips. Typst can load GIFs, but they will become static.
`"webp"`

Raster format that supports both lossy and lossless compression.
`"svg"`

The vector graphics format of the web.
`"pdf"`

High-fidelity document and graphics format, with focus on exact reproduction in print.
 `width`   [auto] or [relative]    

The width of the image.
 `height`   [auto] or [relative] or [fraction]    

The height of the image.
 `alt`   [none] or [str]    

A text describing the image.
 `fit`   [str]    

How the image should adjust itself to a given area.
 VariantDetails`"cover"`

The image should completely cover the area (preserves aspect ratio by cropping the image only horizontally or vertically). This is the default.
`"contain"`

The image should be fully contained in the area (preserves aspect ratio; doesn't crop the image; one dimension can be narrower than specified).
`"stretch"`

The image should be stretched so that it exactly fills the area, even if this means that the image will be distorted (doesn't preserve aspect ratio and doesn't crop the image).
 `scaling`   [auto] or [str]    

A hint to viewers how they should scale the image.
 VariantDetails`"smooth"`

Scale with a smoothing algorithm such as bilinear interpolation.
`"pixelated"`

Scale with nearest neighbor or a similar algorithm to preserve the pixelated look of the image.
 [GradientPrevious page] [LineNext page]