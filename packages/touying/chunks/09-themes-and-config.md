# Themes and Configurations

Touying comes with several built-in themes:
- `simple`
- `university`
- `metropolis`
- `dewdrop` (with navigation bar)
- `aqua`

### Configuration
```typst
#show: university-theme.with(
  aspect-ratio: "16-9",
  align: horizon,
  config-info(
    title: [Title],
    author: [Authors],
    logo: emoji.school,
  ),
)
```

### Dewdrop Navigation Bar
The `dewdrop` theme provides a specialized navigation bar at the top or bottom.
