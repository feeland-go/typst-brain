# Simple Animations (#pause, #meanwhile)

Touying provides easy-to-use animation commands.

### #pause
Used to display content sequentially on the same slide.

```typst
#slide[
  First
  #pause
  Second
  #pause
  Third
]
```

### #meanwhile
Used to display other content synchronously with the previous pause.

```typst
#slide[
  First
  #pause
  Second
  #meanwhile
  Third (appears with Second)
  #pause
  Fourth
]
```
