# Transformations

You can move, rotate, and scale elements.

```typst
#cetz.canvas({
  import cetz.draw: *
  
  // Group elements and transform them together
  group({
    move((1, 1))
    rotate(45deg)
    scale(1.5)
    rect((0,0), (1,1))
  })
})
```

Transformations are local to the group or block they are defined in.
