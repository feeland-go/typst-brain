# CeTZ Animation Integration

Touying can animate CeTZ drawings using `touying-reducer`.

```typst
#import "@preview/cetz:0.4.2"

#let cetz-canvas = touying-reducer.with(
  reduce: cetz.canvas, 
  cover: cetz.draw.hide.with(bounds: true)
)

== CeTZ Animation
#cetz-canvas({
  import cetz.draw: *
  rect((0, 0), (5, 5))
  (pause,)
  rect((0, 0), (1, 1))
  rect((1, 1), (2, 2))
  (pause,)
  line((0, 0), (2.5, 2.5), name: "line")
})
```
