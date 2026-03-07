---
typst_min_version: "0.11"
typst_max_version: null
updated_at: "2025-03-07"
token_count: 680
see_also:
  - 03-table-figure.md
  - 01-syntax-scripting.md
---

# Introspection

## Counter
```typst
#let heading-counter = counter("heading")
#counter(heading).display()
#counter(heading).display("1.1")
#counter(heading).update(n => n + 1)
#counter(heading).step(level: 2)
```

## Page Counter
```typst
#counter(page).display()
#set page(numbering: "1")
#set page(numbering: (..nums) => numbering("i", nums.pos()))
```

## Query (Find Elements)
```typst
#locate(loc => {
  query(heading, loc)   // all headings before loc
  query(label, loc)     // elements with label
  query(heading.where(level: 1), loc)
})
```

## State
```typst
#let s = state("mystate", 0)
#s.display()
#s.update(x => x + 1)  // function update
#s.update(5)           // direct update
```

## Context (Reactive)
```typst
#context counter(page).get()
#context {
  let p = counter(page).get()
  if p == 1 { [First page] }
}
```

## Metadata
```typst
#metadata("value") <label>
#locate(loc => {
  let items = query(<label>, loc)
  items.first().value
})
```

## Locator
```typst
#locate(loc => {
  // loc is a location in the document
  query(selector, loc)  // query from location
})
```

## Custom Counter Example
```typst
#let figure-counter = counter("myfigure")
#let myfigure(body, caption) = {
  figure-counter.step()
  [#figure-counter.display() #body: #caption]
}
```

---
See also: [03-table-figure](03-table-figure.md), [01-syntax-scripting](01-syntax-scripting.md)
