# Getting Started with CeTZ

The minimal starting point for using CeTZ in a `.typ` file is the `canvas` function.

```typst
#import "@preview/cetz:0.4.2"

#cetz.canvas({
  import cetz.draw: *
  
  // Your drawing code here
  circle((0, 0))
  line((0, 0), (2, 1))
})
```

Note: It is recommended to import `cetz.draw: *` inside the canvas scope to avoid name collisions with Typst's built-in functions (like `line`).
