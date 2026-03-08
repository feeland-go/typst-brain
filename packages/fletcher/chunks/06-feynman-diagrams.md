# Feynman Diagrams

Fletcher supports wavy lines and specific arrow placements for physics diagrams.

```typst
#diagram($
  e^- edge("rd", "-<|-") & & & edge("ld", "-|>-") e^+ \\
  & edge(gamma, "wave") \\
  e^+ edge("ru", "-|>-") & & & edge("lu", "-<|-") e^- \\
$)
```
Using `"wave"` style for the photon line and specialized arrow marks for electron/positron paths.
