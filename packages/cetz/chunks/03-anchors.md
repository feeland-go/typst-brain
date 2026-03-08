# Anchors

Anchors allow you to refer to positions relative to an element.

### Named Anchors
Common anchors include: `north`, `south`, `east`, `west`, `center`, `north-east`, etc.

### Usage
```typst
#cetz.canvas({
  import cetz.draw: *
  rect((0,0), (2,2), name: "r")
  circle("r.center", radius: 0.5) // Draws at center of rect r
})
```

### Path Anchors
For paths, you can often use a number between 0 and 1 to refer to a position along the path.
