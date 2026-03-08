---
url: https://typst.app/docs/reference/styling/
category: styling
topic: index
---


# Styling (styling)

Typst includes a flexible styling system that automatically applies styling of your choice to your document. With set rules, you can configure basic properties of elements. This way, you create most common styles. However, there might not be a built-in property for everything you wish to do. For this reason, Typst further supports show rules that can completely redefine the appearance of elements.

## Examples

```typst
#set heading(numbering: "I.")
#set text(
  font: "New Computer Modern"
)

= Introduction
With set rules, you can style
your document.
```

```typst
This list is affected: #[
  #set list(marker: [--])
  - Dash
]

This one is not:
- Bullet
```

```typst
#let task(body, critical: false) = {
  set text(red) if critical
  [- #body]
}

#task(critical: true)[Food today?]
#task(critical: false)[Work deadline]
```

## Overview

Reference Styling Styling Typst includes a flexible styling system that automatically applies styling of your choice to your document. With set rules, you can configure basic properties of elements. This way, you create most common styles. However, there might not be a built-in property for everything you wish to do. For this reason, Typst further supports show rules that can completely redefine the appearance of elements. Set rules With set rules, you can customize the appearance of elements. They are written as a function call to an element function preceded by the set keyword (or #set in markup). Only optional parameters of that function can be provided to the set rule. Refer to each function's documentation to see which parameters are optional. In the example below, we use two set rules to change the font family and heading numbering. #set heading(numbering: "I.") #set text( font: "New Computer Modern" ) = Introduction With set rules, you can style your document. A top level set rule stays in effect until the end of the file. When nested inside of a block, it is only in effect until the end of that block. With a block, you can thus restrict the effect of a rule to a particular segment of your document. Below, we use a content block to scope the list styling to one particular list. This list is affected: #[ #set list(marker: [--]) - Dash ] This one is not: - Bullet Sometimes, you'll want to apply a set rule conditionally. For this, you can use a set-if rule. #let task(body, critical: false) = { set text(red) if critical [- #body] } #task(critical: true)[Food today?] #task(critical: false)[Work deadline] Show rules With show rules, you can deeply customize the look of a type of element. The most basic form of show rule is a show-set rule. Such a rule is written as the show keyword followed by a selector, a colon and then a set rule. The most basic form of selector is an element function. This lets the set rule only apply to the selected element. In the example bel...