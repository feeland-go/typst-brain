---
url: https://typst.app/docs/reference/foundations/int/
category: foundations
topic: int
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Integer] 
  

#  int  

A whole number.
 

The number can be negative, zero, or positive. As Typst uses 64 bits to store integers, integers cannot be smaller than `-9223372036854775808` or larger than `9223372036854775807`. Integer literals are always positive, so a negative integer such as `-1` is semantically the negation `-` of the positive literal `1`. A positive integer greater than the maximum value and a negative integer less than or equal to the minimum value cannot be represented as an integer literal, and are instead parsed as a `float`. The minimum integer value can still be obtained through integer arithmetic.
 

The number can also be specified as hexadecimal, octal, or binary by starting it with a zero followed by either `x`, `o`, or `b`.
 

You can convert a value to an integer with this type's constructor.
 

## Example 
```
#(1 + 2) \
#(2 - 5) \
#(3 + 4 < 8)

#0xff \
#0o10 \
#0b1001

```
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Converts a value to an integer. Raises an error if there is an attempt to produce an integer larger than the maximum 64-bit signed integer or smaller than the minimum 64-bit signed integer.
  Booleans are converted to `0` or `1`.
 Floats and decimals are rounded to the next 64-bit integer towards zero.
 Strings are parsed in base 10.
    View example  
```
#int(false) \
#int(true) \
#int(2.7) \
#int(decimal("3.8")) \
#(int("27") + int("4"))

```
   int([bool][int][float][str][decimal]) -> [int]  `value`   [bool] or [int] or [float] or [str] or [decimal]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The value that should be converted to an integer.
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `signum`

Calculates the sign of an integer.
  If the number is positive, returns `1`.
 If the number is negative, returns `-1`.
 If the number is zero, returns `0`.
    View example  
```
#(5).signum() \
#(-5).signum() \
#(0).signum()

```
   self.signum() -> [int]  

### `bit-not`

Calculates the bitwise NOT of an integer.
 

For the purposes of this function, the operand is treated as a signed integer of 64 bits.
   View example  
```
#4.bit-not() \
#(-1).bit-not()

```
   self.bit-not() -> [int]  

### `bit-and`

Calculates the bitwise AND between two integers.
 

For the purposes of this function, the operands are treated as signed integers of 64 bits.
   View example  
```
#128.bit-and(192)

```
   self.bit-and([int]) -> [int]  `rhs`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The right-hand operand of the bitwise AND.
 

### `bit-or`

Calculates the bitwise OR between two integers.
 

For the purposes of this function, the operands are treated as signed integers of 64 bits.
   View example  
```
#64.bit-or(32)

```
   self.bit-or([int]) -> [int]  `rhs`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The right-hand operand of the bitwise OR.
 

### `bit-xor`

Calculates the bitwise XOR between two integers.
 

For the purposes of this function, the operands are treated as signed integers of 64 bits.
   View example  
```
#64.bit-xor(96)

```
   self.bit-xor([int]) -> [int]  `rhs`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The right-hand operand of the bitwise XOR.
 

### `bit-lshift`

Shifts the operand's bits to the left by the specified amount.
 

For the purposes of this function, the operand is treated as a signed integer of 64 bits. An error will occur if the result is too large to fit in a 64-bit integer.
   View example  
```
#33.bit-lshift(2) \
#(-1).bit-lshift(3)

```
   self.bit-lshift([int]) -> [int]  `shift`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The amount of bits to shift. Must not be negative.
 

### `bit-rshift`

Shifts the operand's bits to the right by the specified amount. Performs an arithmetic shift by default (extends the sign bit to the left, such that negative numbers stay negative), but that can be changed by the `logical` parameter.
 

For the purposes of this function, the operand is treated as a signed integer of 64 bits.
   View example  
```
#64.bit-rshift(2) \
#(-8).bit-rshift(2) \
#(-8).bit-rshift(2, logical: true)

```
   self.bit-rshift([int],[logical: ][bool],) -> [int]  `shift`   [int]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The amount of bits to shift. Must not be negative.
 

Shifts larger than 63 are allowed and will cause the return value to saturate. For non-negative numbers, the return value saturates at `0`, while, for negative numbers, it saturates at `-1` if `logical` is set to `false`, or `0` if it is `true`. This behavior is consistent with just applying this operation multiple times. Therefore, the shift will always succeed.
 `logical`   [bool]    

Toggles whether a logical (unsigned) right shift should be performed instead of arithmetic right shift. If this is `true`, negative operands will not preserve their sign bit, and bits which appear to the left after the shift will be `0`. This parameter has no effect on non-negative operands.
 

 Default: `false` 
 

### `from-bytes`

Converts bytes to an integer.
   View example  
```
#int.from-bytes(bytes((0, 0, 0, 0, 0, 0, 0, 1))) \
#int.from-bytes(bytes((1, 0, 0, 0, 0, 0, 0, 0)), endian: "big")

```
   int.from-bytes([bytes],[endian: ][str],[signed: ][bool],) -> [int]  `bytes`   [bytes]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The bytes that should be converted to an integer.
 

Must be of length at most 8 so that the result fits into a 64-bit signed integer.
 `endian`   [str]    

The endianness of the conversion.
 VariantDetails`"big"`

Big-endian byte order: The highest-value byte is at the beginning of the bytes.
`"little"`

Little-endian byte order: The lowest-value byte is at the beginning of the bytes.
 

 Default: `"little"` 
 `signed`   [bool]    

Whether the bytes should be treated as a signed integer. If this is `true` and the most significant bit is set, the resulting number will negative.
 

 Default: `true` 
 

### `to-bytes`

Converts an integer to bytes.
   View example  
```
#array(10000.to-bytes(endian: "big")) \
#array(10000.to-bytes(size: 4))

```
   self.to-bytes([endian: ][str],[size: ][int],) -> [bytes]  `endian`   [str]    

The endianness of the conversion.
 VariantDetails`"big"`

Big-endian byte order: The highest-value byte is at the beginning of the bytes.
`"little"`

Little-endian byte order: The lowest-value byte is at the beginning of the bytes.
 

 Default: `"little"` 
 `size`   [int]    

The size in bytes of the resulting bytes (must be at least zero). If the integer is too large to fit in the specified size, the conversion will truncate the remaining bytes based on the endianness. To keep the same resulting value, if the endianness is big-endian, the truncation will happen at the rightmost bytes. Otherwise, if the endianness is little-endian, the truncation will happen at the leftmost bytes.
 

Be aware that if the integer is negative and the size is not enough to make the number fit, when passing the resulting bytes to `int.from-bytes`, the resulting number might be positive, as the most significant bit might not be set to 1.
 

 Default: `8` 
 [FunctionPrevious page] [LabelNext page]