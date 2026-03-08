---
url: https://typst.app/docs/reference/syntax/
category: syntax
topic: index
---


# Syntax (syntax)

Typst is a markup language. This means that you can use simple syntax to accomplish common layout tasks. The lightweight markup syntax is complemented by set and show rules, which let you style your document easily and automatically. All this is backed by a tightly integrated scripting language with built-in and user-defined functions.

## Examples

```typst
// our data barely supports
// this claim

We show with $p < 0.05$
that the difference is
significant.
```

```typst
Our study design is as follows:
/* Somebody write this up:
   - 1000 participants.
   - 2x2 data design. */
```

```typst
I got an ice cream for
\$1.50! \u{1f600}
```

## Overview

Reference Syntax Syntax Typst is a markup language. This means that you can use simple syntax to accomplish common layout tasks. The lightweight markup syntax is complemented by set and show rules, which let you style your document easily and automatically. All this is backed by a tightly integrated scripting language with built-in and user-defined functions. Modes Typst has three syntactical modes: Markup, math, and code. Markup mode is the default in a Typst document, math mode lets you write mathematical formulas, and code mode lets you use Typst's scripting features. You can switch to a specific mode at any point by referring to the following table: New modeSyntaxExample CodePrefix the code with #Number: #(1 + 2) MathSurround equation with $..$$-x$ is the opposite of $x$ MarkupSurround markup with [..]let name = [*Typst!*] Once you have entered code mode with #, you don't need to use further hashes unless you switched back to markup or math mode in between. Markup Typst provides built-in markup for the most common document elements. Most of the syntax elements are just shortcuts for a corresponding function. The table below lists all markup that is available and links to the best place to learn more about their syntax and usage. NameExampleSee Paragraph breakBlank lineparbreak Strong emphasis*strong*strong Emphasis_emphasis_emph Raw text`print(1)`raw Linkhttps://typst.app/link Label<intro>label Reference@introref Heading= Headingheading Bullet list- itemlist Numbered list+ itemenum Term list/ Term: descriptionterms Math$x^2$Math Line break\linebreak Smart quote'single' or "double"smartquote Symbol shorthand~, ---Symbols Code expression#rect(width: 1cm)Scripting Character escapeTweet at us \#adBelow Comment/* block */, // lineBelow Math mode Math mode is a special markup mode that is used to typeset mathematical formulas. It is entered by wrapping an equation in $ characters. This works both in markup and code. The equation will be typeset into its own block if i...