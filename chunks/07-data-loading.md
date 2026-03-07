---
typst_min_version: "0.11"
typst_max_version: null
updated_at: "2025-03-07"
token_count: 620
see_also:
  - 01-syntax-scripting.md
  - 06-introspection.md
---

# Data Loading

## CSV
```typst
#let data = csv("data.csv")
#let data = csv("data.csv", delimiter: ";")
// Returns: ((col1, col2), (val1, val2), ...)
```

## JSON
```typst
#let config = json("config.json")
#config.key
#config.nested.property
// Supports objects, arrays, strings, numbers, bools, null
```

## YAML
```typst
#let data = yaml("data.yaml")
#data.title
#data.items.at(0)
// Supports all YAML types
```

## TOML
```typst
#let settings = toml("settings.toml")
#settings.section.key
// Returns dict with nested tables
```

## XML
```typst
#let doc = xml("data.xml")
// Returns: ((tag-name, (attributes), children...), ...)
#let (tag, attrs, ..children) = doc.at(0)
#attrs.at("id")
```

## read() (Raw File)
```typst
#let content = read("file.txt")
#let bytes = read("binary.bin", encoding: none)
// Returns string or bytes
```

## Path Handling
```typst
// Paths relative to current file
#json("../data/config.json")
#csv("/absolute/path.csv")

// Work with paths
#path("folder", "file.txt")
```

## Data Processing Example
```typst
#let records = csv("data.csv")
#table(
  columns: data.first().len(),
  ..data.flatten()
)

#let users = json("users.json")
#for user in users {
  - #user.name (#user.email)
}
```

---
See also: [01-syntax-scripting](01-syntax-scripting.md), [06-introspection](06-introspection.md)
