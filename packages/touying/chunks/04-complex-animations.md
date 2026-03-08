# Complex Animations (uncover, only, alternatives)

For more control over animations, use the `#uncover`, `#only`, and `#alternatives` functions.

```typst
== Complex Animation
At subslide #touying-fn-wrapper((self: none) => str(self.subslide)), we can use:

- #uncover("2-")[`#uncover` function] for reserving space.
- #only("2-")[`#only` function] for NOT reserving space.
- #alternatives[First Alternative][Second Alternative] for choosing one based on subslide.
```

### Callback Style
You can also use a callback to access `self.subslide` directly.

```typst
#slide(
  repeat: 3,
  self => [
    #let (uncover, only, alternatives) = utils.methods(self)
    At subslide #self.subslide, we can use functions...
  ],
)
```
