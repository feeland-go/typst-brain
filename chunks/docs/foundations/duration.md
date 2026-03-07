---
url: https://typst.app/docs/reference/foundations/duration/
category: foundations
topic: duration
---


# duration (foundations)

Represents a positive or negative span of time.

## Signature

`duration(seconds: int, minutes: int, hours: int, days: int, weeks: int) -> duration seconds int`

## Examples

```typst
#duration(
  days: 3,
  hours: 12,
).hours()
```