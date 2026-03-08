---
url: https://typst.app/docs/reference/layout/ratio/
category: layout
topic: ratio
---


# ratio (layout)

A ratio of a whole.

## Examples

```typst
#rect(width: 25%)
```

## Overview

Reference Layout Ratio ratio A ratio of a whole. A ratio is written as a number, followed by a percent sign. Ratios most often appear as part of a relative length, to specify the size of some layout element relative to the page or some container. #rect(width: 25%) However, they can also describe any other property that is relative to some base, e.g. an amount of horizontal scaling or the height of parentheses relative to the height of the content they enclose. Scripting Within your own code, you can use ratios as you like. You can multiply them with various other types as shown below: Multiply byExampleResult ratio27% * 10%2.7% length27% * 100pt27pt relative27% * (10% + 100pt)2.7% + 27pt angle27% * 100deg27deg int27% * 254% float27% * 0.3703710% fraction27% * 3fr0.81fr When ratios are displayed in the document, they are rounded to two significant digits for readability.