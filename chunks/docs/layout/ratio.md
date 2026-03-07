---
url: https://typst.app/docs/reference/layout/ratio/
category: layout
topic: ratio
---

[  ] 
   
  [Reference] 
   
  [Layout] 
   
  [Ratio] 
  

#  ratio  

A ratio of a whole.
 

A ratio is written as a number, followed by a percent sign. Ratios most often appear as part of a [relative length], to specify the size of some layout element relative to the page or some container.
 
```
#rect(width: 25%)

```
 

However, they can also describe any other property that is relative to some base, e.g. an amount of [horizontal scaling] or the [height of parentheses] relative to the height of the content they enclose.
 

## Scripting 

Within your own code, you can use ratios as you like. You can multiply them with various other types as shown below:
 Multiply byExampleResult [`ratio`]`27% * 10%``2.7%` [`length`]`27% * 100pt``27pt` [`relative`]`27% * (10% + 100pt)``2.7% + 27pt` [`angle`]`27% * 100deg``27deg` [`int`]`27% * 2``54%` [`float`]`27% * 0.37037``10%` [`fraction`]`27% * 3fr``0.81fr`  

When ratios are [displayed] in the document, they are rounded to two significant digits for readability.
 [PlacePrevious page] [Relative LengthNext page]