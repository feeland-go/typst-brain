---
typst_min_version: "0.11"
typst_max_version: null
updated_at: "2025-03-07"
token_count: 650
see_also:
  - 06-introspection.md
  - 07-data-loading.md
---

# Syntax & Scripting

## Variables & Binding
```typst
#let name = "value"           // immutable binding
#let (a, b) = (1, 2)          // destructuring
#let func(x) = x * 2          // function definition
#let add(a, b) = { a + b }    // function with block body
```

## Functions
```typst
// Named/positional params, defaults, spread
#let greet(name, greeting: "Hello") = [
  #greeting, #name!
]
#greet("World")
#greet("Typst", greeting: "Hi")

// Return content or values
#let double(x) = x * 2
#let styled(text) = [*#text*]
```

## Control Flow
```typst
#if condition { ... } else { ... }
#for i in range(5) { ... }
#for (k, v) in dict { ... }
#while cond { ... }

// Break/continue in loops
#for i in range(10) {
  if i == 3 { break }
  if i < 2 { continue }
}
```

## Code Blocks & Content
```typst
// Code block returns last expression
#let result = { 1 + 2 }  // 3

// Content block with embedded code
#let doc = [Hello #name!]

// Interpolation
#let val = 5
The value is #val.
Sum: #(1 + 2)
```

## Modules & Import
```typst
#import "utils.typ": func1, func2
#import "utils.typ": *        // import all
#include "chapter.typ"        // include content

// Module access
#import "@preview/package:0.1.0" as pkg
#pkg.function()
```

## Dictionaries & Arrays
```typst
#let arr = (1, 2, 3)
#let dict = (key: "val", num: 5)
#arr.at(0)       // access with default
#dict.key        // dot access
#dict.at("key")  // string key
```

---
See also: [06-introspection](06-introspection.md), [07-data-loading](07-data-loading.md)
