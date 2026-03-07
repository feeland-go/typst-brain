---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
license: "MIT"
---

# fletcher (v0.5.8)

Draw diagrams with nodes and arrows.

## Import
```typst
#import "@preview/fletcher:0.5.8": *
```

## Example
```typst
#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge
```
```typst
#diagram(cell-size: 15mm, $
	G edge(f, -&gt;) edge("d", pi, -&gt;&gt;) &amp; im(f) \
	G slash ker(f) edge("ur", tilde(f), "hook--&gt;")
$)
```

**Full docs:** https://typst.app/universe/package/fletcher