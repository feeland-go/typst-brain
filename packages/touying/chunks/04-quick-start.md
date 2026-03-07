## Quick start

Before you begin, make sure you have installed the Typst environment. If not, you can use the Web App or the Tinymist LSP extensions for VS Code.

To use Touying, you only need to include the following code in your document:

#import "@preview/touying:0.6.2": *
#import themes.simple: *

#show: simple-theme.with(aspect-ratio: "16-9")

= Title

== First Slide

Hello, Touying!

#pause

Hello, Typst!

It’s simple. Congratulations on creating your first Touying slide! 🎉

Tip: You can use Typst syntax like `#import "config.typ": *` or `#include "content.typ"` to implement Touying’s multi-file architecture.