---
url: https://typst.app/docs/reference/layout/block/
category: layout
topic: block
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Block] 
  

# `block`Element  Question mark    Element functions can be customized with `set` and `show` rules.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

A block-level container.
 

Such a container can be used to separate content, size it, and give it a background or border.
 

Blocks are also the primary way to control whether text becomes part of a paragraph or not. See [the paragraph documentation] for more details.
 

## Examples 

With a block, you can give a background to content while still allowing it to break across multiple pages.
 
```
#set page(height: 100pt)
#block(
  fill: luma(230),
  inset: 8pt,
  radius: 4pt,
  lorem(30),
)

```
  

Blocks are also useful to force elements that would otherwise be inline to become block-level, especially when writing show rules.
 
```
#show heading: it => it.body
= Blockless
More text.

#show heading: it => block(it.body)
= Blocky
More text.

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.    block([width: ][auto][relative],[height: ][auto][relative][fraction],[breakable: ][bool],[fill: ][none][color][gradient][tiling],[stroke: ][none][length][color][gradient][stroke][tiling][dictionary],[radius: ][relative][dictionary],[inset: ][relative][dictionary],[outset: ][relative][dictionary],[spacing: ][relative][fraction],[above: ][auto][relative][fraction],[below: ][auto][relative][fraction],[clip: ][bool],[sticky: ][bool],[][none][content],) -> [content]  

### `width`   [auto] or [relative]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The block's width.
   View example   
```
#set align(center)
#block(
  width: 60%,
  inset: 8pt,
  fill: silver,
  lorem(10),
)

```
   

 Default: `auto` 
 

### `height`   [auto] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The block's height. When the height is larger than the remaining space on a page and [`breakable`] is `true`, the block will continue on the next page with the remaining height.
   View example   
```
#set page(height: 80pt)
#set align(center)
#block(
  width: 80%,
  height: 150%,
  fill: aqua,
)

```
    

 Default: `auto` 
 

### `breakable`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether the block can be broken and continue on the next page.
   View example   
```
#set page(height: 80pt)
The following block will
jump to its own page.
#block(
  breakable: false,
  lorem(15),
)

```
    

 Default: `true` 
 

### `fill`   [none] or [color] or [gradient] or [tiling]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The block's background color. See the [rectangle's documentation] for more details.
 

 Default: `none` 
 

### `stroke`   [none] or [length] or [color] or [gradient] or [stroke] or [tiling] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The block's border color. See the [rectangle's documentation] for more details.
 

 Default: `(:)` 
 

### `radius`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to round the block's corners. See the [rectangle's documentation] for more details.
 

 Default: `(:)` 
 

### `inset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to pad the block's content. See the [box's documentation] for more details.
 

 Default: `(:)` 
 

### `outset`   [relative] or [dictionary]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

How much to expand the block's size without affecting the layout. See the [box's documentation] for more details.
 

 Default: `(:)` 
 

### `spacing`   [relative] or [fraction]    

The spacing around the block. When `auto`, inherits the paragraph [`spacing`].
 

For two adjacent blocks, the larger of the first block's `above` and the second block's `below` spacing wins. Moreover, block spacing takes precedence over paragraph [`spacing`].
 

Note that this is only a shorthand to set `above` and `below` to the same value. Since the values for `above` and `below` might differ, a [context] block only provides access to `block.above` and `block.below`, not to `block.spacing` directly.
 

This property can be used in combination with a show rule to adjust the spacing around arbitrary block-level elements.
   View example   
```
#set align(center)
#show math.equation: set block(above: 8pt, below: 16pt)

This sum of $x$ and $y$:
$ x + y = z $
A second paragraph.

```
   

 Default: `1.2em` 
 

### `above`   [auto] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The spacing between this block and its predecessor.
 

 Default: `auto` 
 

### `below`   [auto] or [relative] or [fraction]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The spacing between this block and its successor.
 

 Default: `auto` 
 

### `clip`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether to clip the content inside the block.
 

Clipping is useful when the block's content is larger than the block itself, as any content that exceeds the block's bounds will be hidden.
   View example   
```
#block(
  width: 50pt,
  height: 50pt,
  clip: true,
  image("tiger.jpg", width: 100pt, height: 100pt)
)

```
   

 Default: `false` 
 

### `sticky`   [bool]   Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

Whether this block must stick to the following one, with no break in between.
 

This is, by default, set on heading blocks to prevent orphaned headings at the bottom of the page.
   View example   
```
// Disable stickiness of headings.
#show heading: set block(sticky: false)
#lorem(20)

= Chapter
#lorem(10)

```
    

 Default: `false` 
 

### `body`   [none] or [content]   Positional  Question mark    Positional parameters are specified in order, without names.     Settable  Question mark    Settable parameters can be customized for all following uses of the function with a `set` rule.      

The contents of the block.
 

 Default: `none` 
 [AnglePrevious page] [BoxNext page]