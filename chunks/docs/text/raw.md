---
url: https://typst.app/docs/reference/text/raw/
category: text
topic: raw
---


# raw (text)

Raw text with optional syntax highlighting.

## Signature

`raw(str, block: bool, lang: nonestr, align: alignment, syntaxes: strbytesarray, theme: noneautostrbytes, tab-size: int) -> content`

## Parameters

- `text` (str, required): The raw text.

- `block` (bool, optional): Whether the raw text is displayed as a separate block.

- `lang` (none | str, optional): The language to syntax-highlight in.

- `align` (alignment, optional): The horizontal alignment that each line in a raw block should have. This option is ignored if this is not a raw block (if specified block: false or single backticks were used in markup mode).

- `syntaxes` (str | bytes | array, optional): Additional syntax definitions to load. The syntax definitions should be in the sublime-syntax file format.

- `theme` (none | auto | str | bytes, optional): The theme to use for syntax highlighting. Themes should be in the tmTheme file format.

- `tab-size` (int, optional): The size for a tab stop in spaces. A tab is replaced with enough spaces to align with the next multiple of the size.

## Examples

```typst
Adding `rbx` to `rcx` gives
the desired result.

What is ```rust fn main()``` in Rust
would be ```c int main()``` in C.

```rust
fn main() {
    println!("Hello World!");
}
```

This has ``` `backticks` ``` in it
(but the spaces are trimmed). And
``` here``` the leading space is
also trimmed.
```

```typst
#raw("fn " + "main() {}", lang: "rust")
```

```typst
// Switch to Cascadia Code for both
// inline and block raw.
#show raw: set text(font: "Cascadia Code")

// Reset raw blocks to the same size as normal text,
// but keep inline raw at the reduced size.
#show raw.where(block: true): set text(1em / 0.8)

Now using the `Cascadia Code` font for raw text.
Here's some Python code. It looks larger now:

```py
def python():
  return 5 + 5
```
```