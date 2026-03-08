# Commutative Diagrams (Math Mode)

Fletcher excels at commutative diagrams by leveraging Typst's math mode alignment (`&` and `\`).

```typst
#diagram(cell-size: 15mm, $
  G edge(f, ->) edge("d", pi, ->>) & im(f) \\
  G slash ker(f) edge("ur", tilde(f), "hook-->")
$)
```

In math mode:
- `&` moves to the next column.
- `\\` moves to the next row.
- `edge("d", ...)` means edge going **down**.
- `edge("ur", ...)` means edge going **up and right**.
