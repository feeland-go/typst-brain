# Edges and Arrows

Edges connect nodes or coordinates.

### Basic Edge
`edge((0,0), (1,0), "-|>")`

### Arrowhead Styles
- `->`: Standard arrow.
- `->>`: Double arrowhead.
- `->>>`: Triple arrowhead.
- `|->`: Bar-to-arrow.
- `hook->`: Hook arrow.
- `wave`: Wavy line (for Feynman diagrams).

### Labels
`edge((0,0), (1,0), "label text", "-|>")`
Use `label-side: left/right` or `label-pos: 0.5` to adjust.

### Bending
`edge((0,0), (1,0), "-|>", bend: 30deg)`
Positive bend is clockwise.
