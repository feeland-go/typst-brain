# Quick Start

To use Touying, include the following code in your document:

```typst
#import "@preview/touying:0.6.2": *
#import themes.simple: *

#show: simple-theme.with(aspect-ratio: "16-9")

= Title

== First Slide
Hello, Touying!
#pause
Hello, Typst!
```

It's simple. Congratulations on creating your first Touying slide! 🎉

### Multi-file Architecture
You can use Typst syntax like `#import "config.typ": *` or `#include "content.typ"` to implement Touying’s multi-file architecture.
