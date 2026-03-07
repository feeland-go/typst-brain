---
url: https://typst.app/docs/reference/foundations/eval/
category: foundations
topic: eval
---


# eval (foundations)

Evaluates a string as Typst code.

## Signature

`eval(str, mode: str, scope: dictionary) -> any`

## Parameters

- `source` (str, required): A string of Typst code to evaluate.

- `mode` (str, optional): The syntactical mode in which the string is parsed.

- `scope` (dictionary, optional): A scope of definitions that are made available.

## Examples

```typst
#eval("1 + 1") \
#eval("(1, 2, 3, 4)").len() \
#eval("*Markup!*", mode: "markup") \
```

```typst
#eval("= Heading", mode: "markup")
#eval("1_2^3", mode: "math")
```

```typst
#eval("x + 1", scope: (x: 2)) \
#eval(
  "abc/xyz",
  mode: "math",
  scope: (
    abc: $a + b + c$,
    xyz: $x + y + z$,
  ),
)
```