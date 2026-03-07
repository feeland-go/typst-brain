---
url: https://typst.app/docs/reference/foundations/dictionary/
category: foundations
topic: dictionary
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Dictionary] 
  

#  dictionary  

A map from string keys to values.
 

You can construct a dictionary by enclosing comma-separated `key: value` pairs in parentheses. The values do not have to be of the same type. Since empty parentheses already yield an empty array, you have to use the special `(:)` syntax to create an empty dictionary.
 

A dictionary is conceptually similar to an [array], but it is indexed by strings instead of integers. You can access and create dictionary entries with the `.at()` method. If you know the key statically, you can alternatively use [field access notation] (`.key`) to access the value. To check whether a key is present in the dictionary, use the `in` keyword.
 

You can iterate over the pairs in a dictionary using a [for loop]. This will iterate in the order the pairs were inserted / declared initially.
 

Dictionaries can be added with the `+` operator and [joined together]. They can also be [spread] into a function call or another dictionary[1] with the `..spread` operator. In each case, if a key appears multiple times, the last value will override the others.
 

## Example 
```
#let dict = (
  name: "Typst",
  born: 2019,
)

#dict.name \
#(dict.launch = 20)
#dict.len() \
#dict.keys() \
#dict.values() \
#dict.at("born") \
#dict.insert("city", "Berlin")
#("name" in dict)

```
 1 

When spreading into a dictionary, if all items between the parentheses are spread, you have to use the special `(:..spread)` syntax. Otherwise, it will spread into an array.
  

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value into a dictionary.
 

Note that this function is only intended for conversion of a dictionary-like value to a dictionary, not for creation of a dictionary from individual pairs. Use the dictionary syntax `(key: value)` instead.
   View example  
```
#dictionary(sys).at("version")

```
   dictionary([module]) -> [dictionary]  `value`   [module]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that should be converted to a dictionary.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `len`

The number of pairs in the dictionary.
 self.len() -> [int]  

### `at`

Returns the value associated with the specified key in the dictionary. May be used on the left-hand side of an assignment if the key is already present in the dictionary. Returns the default value if the key is not part of the dictionary or fails with an error if no default value was specified.
 self.at([str],[default: ]any,) -> any  `key`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The key at which to retrieve the item.
 `default`   any    

A default value to return if the key is not part of the dictionary.
 

### `insert`

Inserts a new pair into the dictionary. If the dictionary already contains this key, the value is updated.
 

To insert multiple pairs at once, you can just alternatively another dictionary with the `+=` operator.
 self.insert([str],any,)  `key`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The key of the pair that should be inserted.
 `value`   any  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value of the pair that should be inserted.
 

### `remove`

Removes a pair from the dictionary by key and return the value.
 self.remove([str],[default: ]any,) -> any  `key`   [str]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The key of the pair to remove.
 `default`   any    

A default value to return if the key does not exist.
 

### `keys`

Returns the keys of the dictionary as an array in insertion order.
 self.keys() -> [array]  

### `values`

Returns the values of the dictionary as an array in insertion order.
 self.values() -> [array]  

### `pairs`

Returns the keys and values of the dictionary as an array of pairs. Each pair is represented as an array of length two.
 self.pairs() -> [array]  [DecimalPrevious page] [DurationNext page]