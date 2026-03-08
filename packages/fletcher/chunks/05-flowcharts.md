# Flowcharts and State Machines

Fletcher is highly suitable for flowcharts and state machines.

### Flowchart Example
```typst
#import fletcher.shapes: diamond
#diagram(
  node-stroke: 1pt,
  node((0,0), [Start], corner-radius: 2pt),
  edge("-|>"),
  node((0,1), [Is it a trap?], shape: diamond),
  edge("d,r,u,l", "-|>", [Yes], label-pos: 0.1)
)
```

### State Machine Example
```typst
#diagram(
  node-stroke: .1em,
  node((0,0), `reading`, radius: 2em),
  edge(`read()`, "-|>"),
  node((1,0), `eof`, radius: 2em),
  edge((0,0), (0,0), `read()`, "--|>", bend: 130deg),
)
```
