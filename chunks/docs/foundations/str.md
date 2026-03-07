---
url: https://typst.app/docs/reference/foundations/str/
category: foundations
topic: str
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [String] 
  

#  str  

A sequence of Unicode codepoints.
 

You can iterate over the grapheme clusters of the string using a [for loop]. Grapheme clusters are basically characters but keep together things that belong together, e.g. multiple codepoints that together form a flag emoji. Strings can be added with the `+` operator, [joined together] and multiplied with integers.
 

Typst provides utility methods for string manipulation. Many of these methods (e.g., [`split`], [`trim`] and [`replace`]) operate on patterns: A pattern can be either a string or a [regular expression]. This makes the methods quite versatile.
 

All lengths and indices are expressed in terms of UTF-8 bytes. Indices are zero-based and negative indices wrap around to the end of the string.
 

You can convert a value to a string with this type's constructor.
 

## Example 
```
#"hello world!" \
#"\"hello\n  world\"!" \
#"1 2 3".split() \
#"1,2;3".split(regex("[,;]")) \
#(regex("\\d+") in "ten euros") \
#(regex("\\d+") in "10 euros")

```
 

## Escape sequences 

Just like in markup, you can escape a few symbols in strings:
  `\\` for a backslash
 `\"` for a quote
 `\n` for a newline
 `\r` for a carriage return
 `\t` for a tab
 `\u{1f600}` for a hexadecimal Unicode escape sequence
  

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value to a string.
  Integers are formatted in base 10. This can be overridden with the optional `base` parameter.
 Floats are formatted in base 10 and never in exponential notation.
 Negative integers and floats are formatted with the Unicode minus sign ("−" U+2212) instead of the ASCII minus sign ("-" U+002D).
 From labels the name is extracted.
 Bytes are decoded as UTF-8.
  

If you wish to convert from and to Unicode code points, see the [`to-unicode`] and [`from-unicode`] functions.
   View example  
```
#str(10) \
#str(4000, base: 16) \
#str(2.7) \
#str(1e8) \
#str(<intro>)

```
   str([int][float][str][bytes][label][decimal][version][type],[base: ][int],) -> [str]  `value`   [int] or [float] or [str] or [bytes] or [label] or [decimal] or [version] or [type]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that should be converted to a string.
 `base`   [int]    

The base (radix) to display integers in, between 2 and 36.
 

 Default: `10` 
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `len`

The length of the string in UTF-8 encoded bytes.
 self.len() -> [int]  

### `first`

Extracts the first grapheme cluster of the string.
 

Returns the provided default value if the string is empty or fails with an error if no default value was specified.
 self.first([default: ][str]) -> [str]  `default`   [str]    

A default value to return if the string is empty.
 

### `last`

Extracts the last grapheme cluster of the string.
 

Returns the provided default value if the string is empty or fails with an error if no default value was specified.
 self.last([default: ][str]) -> [str]  `default`   [str]    

A default value to return if the string is empty.
 

### `at`

Extracts the first grapheme cluster after the specified index. Returns the default value if the index is out of bounds or fails with an error if no default value was specified.
 self.at([int],[default: ]any,) -> any  `index`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The byte index. If negative, indexes from the back.
 `default`   any    

A default value to return if the index is out of bounds.
 

### `slice`

Extracts a substring of the string. Fails with an error if the start or end index is out of bounds.
 self.slice([int],[none][int],[count: ][int],) -> [str]  `start`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The start byte index (inclusive). If negative, indexes from the back.
 `end`   [none] or [int]   Positional  Question mark    Positional parameters are specified in order, without names.      

The end byte index (exclusive). If omitted, the whole slice until the end of the string is extracted. If negative, indexes from the back.
 

 Default: `none` 
 `count`   [int]    

The number of bytes to extract. This is equivalent to passing `start + count` as the `end` position. Mutually exclusive with `end`.
 

### `clusters`

Returns the grapheme clusters of the string as an array of substrings.
 self.clusters() -> [array]  

### `codepoints`

Returns the Unicode codepoints of the string as an array of substrings.
 self.codepoints() -> [array]  

### `to-unicode`

Converts a character into its corresponding code point.
   View example  
```
#"a".to-unicode() \
#("a\u{0300}"
   .codepoints()
   .map(str.to-unicode))

```
   str.to-unicode([str]) -> [int]  `character`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The character that should be converted.
 

### `from-unicode`

Converts a unicode code point into its corresponding string.
   View example  
```
#str.from-unicode(97)

```
   str.from-unicode([int]) -> [str]  `value`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The code point that should be converted.
 

### `normalize`

Normalizes the string to the given Unicode normal form.
 

This is useful when manipulating strings containing Unicode combining characters.
   View example  
```
#assert.eq("é".normalize(form: "nfd"), "e\u{0301}")
#assert.eq("ſ́".normalize(form: "nfkc"), "ś")

```
   self.normalize([form: ][str]) -> [str]  `form`   [str]    VariantDetails`"nfc"`

Canonical composition where e.g. accented letters are turned into a single Unicode codepoint.
`"nfd"`

Canonical decomposition where e.g. accented letters are split into a separate base and diacritic.
`"nfkc"`

Like NFC, but using the Unicode compatibility decompositions.
`"nfkd"`

Like NFD, but using the Unicode compatibility decompositions.
 

 Default: `"nfc"` 
 

### `contains`

Whether the string contains the specified pattern.
 

This method also has dedicated syntax: You can write `"bc" in "abcd"` instead of `"abcd".contains("bc")`.
 self.contains([str][regex]) -> [bool]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to search for.
 

### `starts-with`

Whether the string starts with the specified pattern.
 self.starts-with([str][regex]) -> [bool]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern the string might start with.
 

### `ends-with`

Whether the string ends with the specified pattern.
 self.ends-with([str][regex]) -> [bool]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern the string might end with.
 

### `find`

Searches for the specified pattern in the string and returns the first match as a string or `none` if there is no match.
 self.find([str][regex]) -> [none][str]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to search for.
 

### `position`

Searches for the specified pattern in the string and returns the index of the first match as an integer or `none` if there is no match.
 self.position([str][regex]) -> [none][int]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to search for.
 

### `match`

Searches for the specified pattern in the string and returns a dictionary with details about the first match or `none` if there is no match.
 

The returned dictionary has the following keys:
  `start`: The start offset of the match
 `end`: The end offset of the match
 `text`: The text that matched.
 `captures`: An array containing a string for each matched capturing group. The first item of the array contains the first matched capturing, not the whole match! This is empty unless the `pattern` was a regex with capturing groups.
    View example: Shape of the returned dictionary  
```
#let pat = regex("not (a|an) (apple|cat)")
#"I'm a doctor, not an apple.".match(pat) \
#"I am not a cat!".match(pat)

```
     View example: Different kinds of patterns  
```
#assert.eq("Is there a".match("for this?"), none)
#"The time of my life.".match(regex("[mit]+e"))

```
   self.match([str][regex]) -> [none][dictionary]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to search for.
 

### `matches`

Searches for the specified pattern in the string and returns an array of dictionaries with details about all matches. For details about the returned dictionaries, see [above].
   View example  
```
#"Day by Day.".matches("Day")

```
   self.matches([str][regex]) -> [array]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to search for.
 

### `replace`

Replace at most `count` occurrences of the given pattern with a replacement string or function (beginning from the start). If no count is given, all occurrences are replaced.
 self.replace([str][regex],[str][function],[count: ][int],) -> [str]  `pattern`   [str] or [regex]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to search for.
 `replacement`   [str] or [function]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The string to replace the matches with or a function that gets a dictionary for each match and can return individual replacement strings.
 

The dictionary passed to the function has the same shape as the dictionary returned by [`match`].
 `count`   [int]    

If given, only the first `count` matches of the pattern are placed.
 

### `trim`

Removes matches of a pattern from one or both sides of the string, once or repeatedly and returns the resulting string.
 self.trim([none][str][regex],[at: ][alignment],[repeat: ][bool],) -> [str]  `pattern`   [none] or [str] or [regex]   Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to search for. If `none`, trims white spaces.
 

 Default: `none` 
 `at`   [alignment]    

Can be `start` or `end` to only trim the start or end of the string. If omitted, both sides are trimmed.
 `repeat`   [bool]    

Whether to repeatedly removes matches of the pattern or just once. Defaults to `true`.
 

 Default: `true` 
 

### `split`

Splits a string at matches of a specified pattern and returns an array of the resulting parts.
 

When the empty string is used as a separator, it separates every character (i.e., Unicode code point) in the string, along with the beginning and end of the string. In practice, this means that the resulting list of parts will contain the empty string at the start and end of the list.
 self.split([none][str][regex]) -> [array]  `pattern`   [none] or [str] or [regex]   Positional  Question mark    Positional parameters are specified in order, without names.      

The pattern to split at. Defaults to whitespace.
 

 Default: `none` 
 

### `rev`

Reverse the string.
 self.rev() -> [str]  [Standard LibraryPrevious page] [SymbolNext page]