# Nodes and Shapes

Nodes represent the points/objects in your diagram.

### Basic Node
`node((0,0), [Label], stroke: 1pt, fill: blue.lighten(80%))`

### Custom Shapes
Import shapes like `diamond` for flowcharts:
```typst
#import fletcher.shapes: diamond
#diagram(
  node((0,0), [Decision], shape: diamond, stroke: 1pt)
)
```

### Options
- `shape`: `rect` (default), `circle`, `diamond`, etc.
- `radius`: For circles or rounded corners.
- `extrude`: Add extra space around the node.
