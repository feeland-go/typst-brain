# Styling in CeTZ

All elements that draw something typically have `stroke` and `fill` styling.

### Basic Styling
```typst
#cetz.canvas({
  import cetz.draw: *
  
  // Fill and stroke
  rect((0,0), (2,2), fill: blue.lighten(80%), stroke: blue)
  
  // Setting default styles for subsequent elements
  set-style(stroke: (thickness: 2pt, dash: "dashed"))
  circle((4, 1)) 
})
```

### Common Styles
- `stroke`: Color, thickness, dash pattern.
- `fill`: Color or gradient.
- `radius`: For circles and rounded rectangles.
