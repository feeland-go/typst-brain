---
url: https://typst.app/docs/reference/foundations/array/
category: foundations
topic: array
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Array] 
  

#  array  

A sequence of values.
 

You can construct an array by enclosing a comma-separated sequence of values in parentheses. The values do not have to be of the same type.
 

You can access and update array items with the `.at()` method. Indices are zero-based and negative indices wrap around to the end of the array. You can iterate over an array using a [for loop]. Arrays can be added together with the `+` operator, [joined together] and multiplied with integers.
 

Note: An array of length one needs a trailing comma, as in `(1,)`. This is to disambiguate from a simple parenthesized expressions like `(1 + 2) * 3`. An empty array is written as `()`.
 

## Example 
```
#let values = (1, 7, 4, -3, 2)

#values.at(0) \
#(values.at(0) = 3)
#values.at(-1) \
#values.find(calc.even) \
#values.filter(calc.odd) \
#values.map(calc.abs) \
#values.rev() \
#(1, (2, 3)).flatten() \
#(("A", "B", "C")
    .join(", ", last: " and "))

```
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value to an array.
 

Note that this function is only intended for conversion of a collection-like value to an array, not for creation of an array from individual items. Use the array syntax `(1, 2, 3)` (or `(1,)` for a single-element array) instead.
   View example  
```
#let hi = "Hello 😃"
#array(bytes(hi))

```
   array([bytes][array][version]) -> [array]  `value`   [bytes] or [array] or [version]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that should be converted to an array.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `len`

The number of values in the array.
 self.len() -> [int]  

### `first`

Returns the first item in the array. May be used on the left-hand side an assignment. Returns the default value if the array is empty or fails with an error is no default value was specified.
 self.first([default: ]any) -> any  `default`   any    

A default value to return if the array is empty.
 

### `last`

Returns the last item in the array. May be used on the left-hand side of an assignment. Returns the default value if the array is empty or fails with an error is no default value was specified.
 self.last([default: ]any) -> any  `default`   any    

A default value to return if the array is empty.
 

### `at`

Returns the item at the specified index in the array. May be used on the left-hand side of an assignment. Returns the default value if the index is out of bounds or fails with an error if no default value was specified.
 self.at([int],[default: ]any,) -> any  `index`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The index at which to retrieve the item. If negative, indexes from the back.
 `default`   any    

A default value to return if the index is out of bounds.
 

### `push`

Adds a value to the end of the array.
 self.push(any)  `value`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value to insert at the end of the array.
 

### `pop`

Removes the last item from the array and returns it. Fails with an error if the array is empty.
 self.pop() -> any  

### `insert`

Inserts a value into the array at the specified index, shifting all subsequent elements to the right. Fails with an error if the index is out of bounds.
 

To replace an element of an array, use [`at`].
 self.insert([int],any,)  `index`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The index at which to insert the item. If negative, indexes from the back.
 `value`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value to insert into the array.
 

### `remove`

Removes the value at the specified index from the array and return it.
 self.remove([int],[default: ]any,) -> any  `index`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The index at which to remove the item. If negative, indexes from the back.
 `default`   any    

A default value to return if the index is out of bounds.
 

### `slice`

Extracts a subslice of the array. Fails with an error if the start or end index is out of bounds.
 self.slice([int],[none][int],[count: ][int],) -> [array]  `start`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The start index (inclusive). If negative, indexes from the back.
 `end`   [none] or [int]   Positional  Question mark    Positional parameters are specified in order, without names.      

The end index (exclusive). If omitted, the whole slice until the end of the array is extracted. If negative, indexes from the back.
 

 Default: `none` 
 `count`   [int]    

The number of items to extract. This is equivalent to passing `start + count` as the `end` position. Mutually exclusive with `end`.
 

### `contains`

Whether the array contains the specified value.
 

This method also has dedicated syntax: You can write `2 in (1, 2, 3)` instead of `(1, 2, 3).contains(2)`.
 self.contains(any) -> [bool]  `value`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value to search for.
 

### `find`

Searches for an item for which the given function returns `true` and returns the first match or `none` if there is no match.
 self.find([function]) -> any[none]  `searcher`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The function to apply to each item. Must return a boolean.
 

### `position`

Searches for an item for which the given function returns `true` and returns the index of the first match or `none` if there is no match.
 self.position([function]) -> [none][int]  `searcher`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The function to apply to each item. Must return a boolean.
 

### `range`

Create an array consisting of a sequence of numbers.
 

If you pass just one positional parameter, it is interpreted as the `end` of the range. If you pass two, they describe the `start` and `end` of the range.
 

This function is available both in the array function's scope and globally.
   View example  
```
#range(5) \
#range(2, 5) \
#range(20, step: 4) \
#range(21, step: 4) \
#range(5, 2, step: -1)

```
   array.range([int],[int],[step: ][int],) -> [array]  `start`   [int]   Positional  Question mark    Positional parameters are specified in order, without names.      

The start of the range (inclusive).
 

 Default: `0` 
 `end`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The end of the range (exclusive).
 `step`   [int]    

The distance between the generated numbers.
 

 Default: `1` 
 

### `filter`

Produces a new array with only the items from the original one for which the given function returns true.
 self.filter([function]) -> [array]  `test`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The function to apply to each item. Must return a boolean.
 

### `map`

Produces a new array in which all items from the original one were transformed with the given function.
 self.map([function]) -> [array]  `mapper`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The function to apply to each item.
 

### `enumerate`

Returns a new array with the values alongside their indices.
 

The returned array consists of `(index, value)` pairs in the form of length-2 arrays. These can be [destructured] with a let binding or for loop.
   View example  
```
#for (i, value) in ("A", "B", "C").enumerate() {
  [#i: #value \ ]
}

#("A", "B", "C").enumerate(start: 1)

```
   self.enumerate([start: ][int]) -> [array]  `start`   [int]    

The index returned for the first pair of the returned list.
 

 Default: `0` 
 

### `zip`

Zips the array with other arrays.
 

Returns an array of arrays, where the `i`th inner array contains all the `i`th elements from each original array.
 

If the arrays to be zipped have different lengths, they are zipped up to the last element of the shortest array and all remaining elements are ignored.
 

This function is variadic, meaning that you can zip multiple arrays together at once: `(1, 2).zip(("A", "B"), (10, 20))` yields `((1, "A", 10), (2, "B", 20))`.
 self.zip([exact: ][bool],[..][array],) -> [array]  `exact`   [bool]    

Whether all arrays have to have the same length. For example, `(1, 2).zip((1, 2, 3), exact: true)` produces an error.
 

 Default: `false` 
 `others`   [array]  Required  Positional  Question mark    Positional parameters are specified in order, without names.     Variadic  Question mark    Variadic parameters can be specified multiple times.      

The arrays to zip with.
 

### `fold`

Folds all items into a single value using an accumulator function.
   View example  
```
#let array = (1, 2, 3, 4)
#array.fold(0, (acc, x) => acc + x)

```
   self.fold(any,[function],) -> any  `init`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The initial value to start with.
 `folder`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The folding function. Must have two parameters: One for the accumulated value and one for an item.
 

### `sum`

Sums all items (works for all types that can be added).
 self.sum([default: ]any) -> any  `default`   any    

What to return if the array is empty. Must be set if the array can be empty.
 

### `product`

Calculates the product of all items (works for all types that can be multiplied).
 self.product([default: ]any) -> any  `default`   any    

What to return if the array is empty. Must be set if the array can be empty.
 

### `any`

Whether the given function returns `true` for any item in the array.
 self.any([function]) -> [bool]  `test`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The function to apply to each item. Must return a boolean.
 

### `all`

Whether the given function returns `true` for all items in the array.
 self.all([function]) -> [bool]  `test`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The function to apply to each item. Must return a boolean.
 

### `flatten`

Combine all nested arrays into a single flat one.
 self.flatten() -> [array]  

### `rev`

Return a new array with the same items, but in reverse order.
 self.rev() -> [array]  

### `split`

Split the array at occurrences of the specified value.
   View example  
```
#(1, 1, 2, 3, 2, 4, 5).split(2)

```
   self.split(any) -> [array]  `at`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value to split at.
 

### `join`

Combine all items in the array into one.
 self.join(any[none],[last: ]any,[default: ]any[none],) -> any  `separator`   any or [none]   Positional  Question mark    Positional parameters are specified in order, without names.      

A value to insert between each item of the array.
 

 Default: `none` 
 `last`   any    

An alternative separator between the last two items.
 `default`   any or [none]    

What to return if the array is empty.
 

 Default: `none` 
 

### `intersperse`

Returns an array with a copy of the separator value placed between adjacent elements.
   View example  
```
#("A", "B", "C").intersperse("-")

```
   self.intersperse(any) -> [array]  `separator`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that will be placed between each adjacent element.
 

### `chunks`

Splits an array into non-overlapping chunks, starting at the beginning, ending with a single remainder chunk.
 

All chunks but the last have `chunk-size` elements. If `exact` is set to `true`, the remainder is dropped if it contains less than `chunk-size` elements.
   View example  
```
#let array = (1, 2, 3, 4, 5, 6, 7, 8)
#array.chunks(3) \
#array.chunks(3, exact: true)

```
   self.chunks([int],[exact: ][bool],) -> [array]  `chunk-size`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

How many elements each chunk may at most contain.
 `exact`   [bool]    

Whether to keep the remainder if its size is less than `chunk-size`.
 

 Default: `false` 
 

### `windows`

Returns sliding windows of `window-size` elements over an array.
 

If the array length is less than `window-size`, this will return an empty array.
   View example  
```
#let array = (1, 2, 3, 4, 5, 6, 7, 8)
#array.windows(5)

```
   self.windows([int]) -> [array]  `window-size`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

How many elements each window will contain.
 

### `sorted`

Return a sorted version of this array, optionally by a given key function. The sorting algorithm used is stable.
 

Returns an error if a pair of values selected for comparison could not be compared, or if the key or comparison function (if given) yield an error.
 

To sort according to multiple criteria at once, e.g. in case of equality between some criteria, the key function can return an array. The results are in lexicographic order.
   View example  
```
#let array = (
  (a: 2, b: 4),
  (a: 1, b: 5),
  (a: 2, b: 3),
)
#array.sorted(key: it => (it.a, it.b))

```
   self.sorted([key: ][function],[by: ][function],) -> [array]  `key`   [function]    

If given, applies this function to each element in the array to determine the keys to sort by.
 `by`   [function]    

If given, uses this function to compare every two elements in the array.
 

The function will receive two elements in the array for comparison, and should return a boolean indicating their order: `true` indicates that the elements are in order, while `false` indicates that they should be swapped. To keep the sort stable, if the two elements are equal, the function should return `true`.
 

If this function does not order the elements properly (e.g., by returning `false` for both `(x, y)` and `(y, x)`, or for `(x, x)`), the resulting array will be in unspecified order.
 

When used together with `key`, `by` will be passed the keys instead of the elements.
   View example   
```
#(
  "sorted",
  "by",
  "decreasing",
  "length",
).sorted(
  key: s => s.len(),
  by: (l, r) => l >= r,
)

```
   

### `dedup`

Deduplicates all items in the array.
 

Returns a new array with all duplicate items removed. Only the first element of each duplicate is kept.
   View example  
```
#(3, 3, 1, 2, 3).dedup()

```
   self.dedup([key: ][function]) -> [array]  `key`   [function]    

If given, applies this function to each element in the array to determine the keys to deduplicate by.
   View example   
```
#("apple", "banana", " apple ").dedup(key: s => s.trim())

```
   

### `to-dict`

Converts an array of pairs into a dictionary. The first value of each pair is the key, the second the value.
 

If the same key occurs multiple times, the last value is selected.
   View example  
```
#(
  ("apples", 2),
  ("peaches", 3),
  ("apples", 5),
).to-dict()

```
   self.to-dict() -> [dictionary]  

### `reduce`

Reduces the elements to a single one, by repeatedly applying a reducing operation.
 

If the array is empty, returns `none`, otherwise, returns the result of the reduction.
 

The reducing function is a closure with two arguments: an "accumulator", and an element.
 

For arrays with at least one element, this is the same as [`array.fold`] with the first element of the array as the initial accumulator value, folding every subsequent element into it.
   View example  
```
#let array = (2, 1, 4, 3)
#array.reduce((acc, x) => calc.max(acc, x))

```
   self.reduce([function]) -> any  `reducer`   [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The reducing function. Must have two parameters: One for the accumulated value and one for an item.
 [ArgumentsPrevious page] [AssertNext page]