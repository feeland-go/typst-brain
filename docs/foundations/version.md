---
url: https://typst.app/docs/reference/foundations/version/
category: foundations
topic: version
---


# version (foundations)

A version with an arbitrary number of components.

## Signature

`version(..intarray) -> version components int or array Required Positional Variadic`

## Examples

```typst
#version() \
#version(1) \
#version(1, 2, 3, 4) \
#version((1, 2, 3, 4)) \
#version((1, 2), 3)
```

```typst
Current version: #sys.version \
#(sys.version >= version(0, 14, 0)) \
#(version(3, 2, 0) > version(4, 1, 0))
```