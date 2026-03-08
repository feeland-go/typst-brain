---
url: https://typst.app/docs/reference/context/
category: context
topic: index
---


# Context (context)

Sometimes, we want to create content that reacts to its location in the document. This could be a localized phrase that depends on the configured text language or something as simple as a heading number which prints the right value based on how many headings came before it. However, Typst code isn't directly aware of its location in the document. Some code at the beginning of the source text could yield content that ends up at the back of the document.

## Examples

```typst
#set text(lang: "de")
#context text.lang
```

```typst
#let value = context text.lang
#value

#set text(lang: "de")
#value

#set text(lang: "fr")
#value
```

```typst
#set heading(numbering: "1.")

= Introduction
#lorem(5)

#context counter(heading).get()

= Background
#lorem(5)

#context counter(heading).get()
```

## Overview

Reference Context Context Sometimes, we want to create content that reacts to its location in the document. This could be a localized phrase that depends on the configured text language or something as simple as a heading number which prints the right value based on how many headings came before it. However, Typst code isn't directly aware of its location in the document. Some code at the beginning of the source text could yield content that ends up at the back of the document. To produce content that is reactive to its surroundings, we must thus specifically instruct Typst: We do this with the context keyword, which precedes an expression and ensures that it is computed with knowledge of its environment. In return, the context expression itself ends up opaque. We cannot directly access whatever results from it in our code, precisely because it is contextual: There is no one correct result, there may be multiple results in different places of the document. For this reason, everything that depends on the contextual data must happen inside of the context expression. Aside from explicit context expressions, context is also established implicitly in some places that are also aware of their location in the document: Show rules provide context1 and numberings in the outline, for instance, also provide the proper context to resolve counters. Style context With set rules, we can adjust style properties for parts or the whole of our document. We cannot access these without a known context, as they may change throughout the course of the document. When context is available, we can retrieve them simply by accessing them as fields on the respective element function. #set text(lang: "de") #context text.lang As explained above, a context expression is reactive to the different environments it is placed into. In the example below, we create a single context expression, store it in the value variable and use it multiple times. Each use properly reacts to the current surroundings. #...