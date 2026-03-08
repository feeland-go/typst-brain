# Coordinate Systems

A coordinate is a position on the canvas. CeTZ supports multiple systems:

### XYZ Coordinates
Simple arrays like `(1, 2)` or `(1, 2, 3)`. Default unit is `1cm`.

### Relative Coordinates
Use `(rel: (1, 1))` to specify a position relative to the previous point.

### Polar Coordinates
Specify angle and distance: `(angle: 45deg, radius: 2)`.

### Anchors
Reference a specific point of a named element: `("element-name.anchor-name")`.
Example: `("my-rect.north-east")`.

### Interpolation
Find a point between two others: `(line: ("A", "B"), number: 0.5)` (the midpoint).
