---
url: https://typst.app/docs/reference/visualize/
category: visualize
topic: index
---


# Visualize (visualize)

Drawing and data visualization.

## Overview

Reference Visualize Visualize Drawing and data visualization. If you want to create more advanced drawings or plots, also have a look at the CeTZ package as well as more specialized packages for your use case. Accessibility All shapes and paths drawn by Typst are automatically marked as artifacts to make them invisible to Assistive Technology (AT) during PDF export. However, their contents (if any) remain accessible. If you are using the functions in this model to create an illustration with semantic meaning, make it accessible by wrapping it in a figure function call. Use its alt parameter to provide an alternative description. Definitions circle A circle with optional content. color A color in a specific color space. curve A curve consisting of movements, lines, and Bézier segments. ellipse An ellipse with optional content. gradient A color gradient. image A raster or vector graphic. line A line from one point to another. path A path through a list of points, connected by Bézier curves. polygon A closed polygon. rect A rectangle with optional content. square A square with optional content. stroke Defines how to draw a line. tiling A repeating tiling fill.