---
url: https://typst.app/docs/reference/model/enum/
category: model
topic: enum
---


# enum (model)

A numbered list.

## Signature

`enum(tight: bool, numbering: strfunction, start: autoint, full: bool, reversed: bool, indent: length, body-indent: length, spacing: autolength, number-align: alignment, ..contentarray) -> content`

## Parameters

- `tight` (bool, optional): Defines the default spacing of the enumeration. If it is false, the items are spaced apart with paragraph spacing. If it is true, they use paragraph leading instead. This makes the list more compact, which can look better if the items are short.

- `numbering` (str | function, optional): How to number the enumeration. Accepts a numbering pattern or function.

- `start` (auto | int, optional): Which number to start the enumeration with.

- `full` (bool, optional): Whether to display the full numbering, including the numbers of all parent enumerations.

- `reversed` (bool, optional): Whether to reverse the numbering for this enumeration.

- `indent` (length, optional): The indentation of each item.

- `body-indent` (length, optional): The space between the numbering and the body of each item.

- `spacing` (auto | length, optional): The spacing between the items of the enumeration.

- `number-align` (alignment, optional): The alignment that enum numbers should have.

- `children` (content | array, required): The numbered list's items.

## Examples

```typst
Automatically numbered:
+ Preparations
+ Analysis
+ Conclusions

Manually numbered:
2. What is the first step?
5. I am confused.
+  Moving on ...

Multiple lines:
+ This enum item has multiple
  lines because the next line
  is indented.

Function call.
#enum[First][Second]
```

```typst
#set enum(numbering: "a)")

+ Starting off ...
+ Don't forget step two
```

```typst
#enum(
  enum.item(1)[First step],
  enum.item(5)[Fifth step],
  enum.item(10)[Tenth step]
)
```