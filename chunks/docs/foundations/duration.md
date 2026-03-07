---
url: https://typst.app/docs/reference/foundations/duration/
category: foundations
topic: duration
---

[  ] 
   
  [Reference] 
   
  [Foundations] 
   
  [Duration] 
  

#  duration  

Represents a positive or negative span of time.
 

##  Constructor   Question mark    If a type has a constructor, you can call it like a function to create a new value of the type.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i); 

Creates a new duration.
 

You can specify the [duration] using weeks, days, hours, minutes and seconds. You can also get a duration by subtracting two [datetimes].
   View example  
```
#duration(
  days: 3,
  hours: 12,
).hours()

```
   duration([seconds: ][int],[minutes: ][int],[hours: ][int],[days: ][int],[weeks: ][int],) -> [duration]  `seconds`   [int]    

The number of seconds.
 

 Default: `0` 
 `minutes`   [int]    

The number of minutes.
 

 Default: `0` 
 `hours`   [int]    

The number of hours.
 

 Default: `0` 
 `days`   [int]    

The number of days.
 

 Default: `0` 
 `weeks`   [int]    

The number of weeks.
 

 Default: `0` 
 

##  Definitions  Question mark    Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.    

### `seconds`

The duration expressed in seconds.
 

This function returns the total duration represented in seconds as a floating-point number rather than the second component of the duration.
 self.seconds() -> [float]  

### `minutes`

The duration expressed in minutes.
 

This function returns the total duration represented in minutes as a floating-point number rather than the second component of the duration.
 self.minutes() -> [float]  

### `hours`

The duration expressed in hours.
 

This function returns the total duration represented in hours as a floating-point number rather than the second component of the duration.
 self.hours() -> [float]  

### `days`

The duration expressed in days.
 

This function returns the total duration represented in days as a floating-point number rather than the second component of the duration.
 self.days() -> [float]  

### `weeks`

The duration expressed in weeks.
 

This function returns the total duration represented in weeks as a floating-point number rather than the second component of the duration.
 self.weeks() -> [float]  [DictionaryPrevious page] [EvaluateNext page]