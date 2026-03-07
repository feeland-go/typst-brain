---
url: https://typst.app/docs/reference/introspection/metadata/
category: introspection
topic: metadata
---


# metadata (introspection)

Exposes a value to the query system without producing visible content.

## Signature

`metadata(any) -> content`

## Parameters

- `value` (any, required): The value to embed into the document.

## Examples

```typst
// Put metadata somewhere.
#metadata("This is a note") <note>

// And find it from anywhere else.
#context {
  query(<note>).first().value
}
```