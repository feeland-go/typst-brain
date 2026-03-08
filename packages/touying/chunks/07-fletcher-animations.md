# Fletcher Animation Integration

Touying can animate Fletcher diagrams using `touying-reducer`.

```typst
#import "@preview/fletcher:0.5.8" as fletcher: node, edge

#let fletcher-diagram = touying-reducer.with(
  reduce: fletcher.diagram, 
  cover: fletcher.hide
)

== Fletcher Animation
#fletcher-diagram(
  node-stroke: .1em,
  node((0, 0), `reading`, radius: 2em),
  pause,
  edge(`read()`, "-|>"),
  node((1, 0), `eof`, radius: 2em),
)
```
