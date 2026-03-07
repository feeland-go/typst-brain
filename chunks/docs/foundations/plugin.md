---
url: https://typst.app/docs/reference/foundations/plugin/
category: foundations
topic: plugin
---


# plugin (foundations)

Loads a WebAssembly module.

## Signature

`plugin(strbytes) -> module`

## Parameters

- `source` (str | bytes, required): A path to a WebAssembly file or raw WebAssembly bytes.

## Examples

```typst
#let myplugin = plugin("hello.wasm")
#let concat(a, b) = str(
  myplugin.concatenate(
    bytes(a),
    bytes(b),
  )
)

#concat("hello", "world")
```