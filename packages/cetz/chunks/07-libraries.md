# CeTZ Libraries

CeTZ provides specialized libraries for complex drawings.

### Plotting
Used for creating 2D and 3D plots.
`#import "@preview/cetz-plot:0.1.0": plot`

### Charts
For bar charts, pie charts, etc.

### Tree
For hierarchical diagrams.
```typst
#import cetz.draw: *
#cetz.tree.tree(
  (
    [Root],
    ([Child 1],),
    ([Child 2], ([Grandchild],)),
  )
)
```

### Venn Diagrams
Available via `cetz-venn`.
