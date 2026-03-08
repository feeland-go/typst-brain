---
url: https://typst.app/docs/reference/model/parbreak/
category: model
topic: parbreak
---


# parbreak (model)

A paragraph break.

## Examples

```typst
#for i in range(3) {
  [Blind text #i: ]
  lorem(5)
  parbreak()
}
```

## Overview

Reference Model Paragraph Break parbreakElement A paragraph break. This starts a new paragraph. Especially useful when used within code like for loops. Multiple consecutive paragraph breaks collapse into a single one. Example #for i in range(3) { [Blind text #i: ] lorem(5) parbreak() } Syntax Instead of calling this function, you can insert a blank line into your markup to create a paragraph break.Parameters parbreak() -> content