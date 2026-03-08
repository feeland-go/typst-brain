---
url: https://typst.app/docs/reference/scripting/
category: scripting
topic: index
---


# Scripting (scripting)

Typst embeds a powerful scripting language. You can automate your documents and create more sophisticated styles with code. Below is an overview over the scripting concepts.

## Examples

```typst
#emph[Hello] \
#emoji.face \
#"hello".len()
```

```typst
#{
  let a = [from]
  let b = [*world*]
  [hello ]
  a + [ the ] + b
}
```

```typst
#let name = "Typst"
This is #name's documentation.
It explains #name.

#let my-add(x, y) = x + y
Sum is #my-add(2, 3).
```

## Overview

Reference Scripting Scripting Typst embeds a powerful scripting language. You can automate your documents and create more sophisticated styles with code. Below is an overview over the scripting concepts. Expressions In Typst, markup and code are fused into one. All but the most common elements are created with functions. To make this as convenient as possible, Typst provides compact syntax to embed a code expression into markup: An expression is introduced with a hash (#) and normal markup parsing resumes after the expression is finished. If a character would continue the expression but should be interpreted as text, the expression can forcibly be ended with a semicolon (;). You can escape a literal # or ; with a backslash. #emph[Hello] \ #emoji.face \ #"hello".len() The example above shows a few of the available expressions, including function calls, field accesses, and method calls. More kinds of expressions are discussed in the remainder of this chapter. A few kinds of expressions are not compatible with the hash syntax (e.g. binary operator expressions). To embed these into markup, you can use parentheses, as in #(1 + 2). Blocks To structure your code and embed markup into it, Typst provides two kinds of blocks: Code block: { let x = 1; x + 2 } When writing code, you'll probably want to split up your computation into multiple statements, create some intermediate variables and so on. Code blocks let you write multiple expressions where one is expected. The individual expressions in a code block should be separated by line breaks or semicolons. The output values of the individual expressions in a code block are joined to determine the block's value. Expressions without useful output, like let bindings yield none, which can be joined with any value without effect. Content block: [*Hey* there!] With content blocks, you can handle markup/content as a programmatic value, store it in variables and pass it to functions. Content blocks are delimited by square brackets an...