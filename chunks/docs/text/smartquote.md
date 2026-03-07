---
url: https://typst.app/docs/reference/text/smartquote/
category: text
topic: smartquote
---


# smartquote (text)

A language-aware quote that reacts to its context.

## Signature

`smartquote(double: bool, enabled: bool, alternative: bool, quotes: autostrarraydictionary) -> content`

## Parameters

- `double` (bool, optional): Whether this should be a double quote.

- `enabled` (bool, optional): Whether smart quotes are enabled.

- `alternative` (bool, optional): Whether to use alternative quotes.

- `quotes` (auto | str | array | dictionary, optional): The quotes to use.

## Examples

```typst
"This is in quotes."

#set text(lang: "de")
"Das ist in Anführungszeichen."

#set text(lang: "fr")
"C'est entre guillemets."
```

```typst
#set smartquote(enabled: false)

These are "dumb" quotes.
```

```typst
#set text(lang: "de")
#set smartquote(alternative: true)

"Das ist in anderen Anführungszeichen."
```