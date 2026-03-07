## Quick start

To use Touying, you only need to include the following code in your document:

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

**Tip:** You can use Typst syntax like `#import "config.typ": *` or `#include "content.typ"` to implement Touying's multi-file architecture.
