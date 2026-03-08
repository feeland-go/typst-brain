# Getting Started with Fletcher

Import the necessary functions from the package:

```typst
#import "@preview/fletcher:0.5.9" as fletcher: diagram, node, edge
```

### Basic Diagram Template
```typst
#diagram(
  node((0,0), [Start]),
  edge((0,0), (1,0), "-|>"),
  node((1,0), [End]),
)
```
Nodes can be positioned using (x, y) coordinates. Edges connect these coordinates or specific nodes.
