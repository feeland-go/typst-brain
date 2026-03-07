---
url: https://typst.app/docs/reference/pdf/header-cell/
category: pdf
topic: header-cell
---

[  ] 
   
  [Reference] 
   
  [PDF] 
   
  [Header Cell] 
  

# `header-cell`

Explicitly defines a cell as a header cell.
 

Header cells help users of Assistive Technology (AT) understand and navigate complex tables. When your table is correctly marked up with header cells, AT can announce the relevant header information on-demand when entering a cell.
 

By default, Typst will automatically mark all cells within [`table.header`] as header cells. They will apply to the columns below them. You can use that function's [`level`] parameter to make header cells labelled by other header cells.
 

The `pdf.header-cell` function allows you to indicate that a cell is a header cell in the following additional situations:
  You have a header column in which each cell applies to its row. In that case, you pass `"row"` as an argument to the [`scope` parameter] to indicate that the header cell applies to the row.
 You have a cell in [`table.header`], for example at the very start, that labels both its row and column. In that case, you pass `"both"` as an argument to the [`scope`] parameter.
 You have a header cell in a row not containing other header cells. In that case, you can use this function to mark it as a header cell.
  

The API of this feature is temporary. Hence, calling this function requires enabling the `a11y-extras` feature flag at the moment. In a future Typst release, this functionality may move out of the `pdf` module so that tables in other export targets can contain the same information.
 
```
#show table.cell.where(x: 0): set text(weight: "medium")
#show table.cell.where(y: 0): set text(weight: "bold")

#table(
  columns: 3,
  align: (start, end, end),

  table.header(
    // Top-left cell: Labels both the nutrient rows
    // and the serving size columns.
    pdf.header-cell(scope: "both")[Nutrient],
    [Per 100g],
    [Per Serving],
  ),

  // First column cells are row headers
  pdf.header-cell(scope: "row")[Calories],
  [250 kcal], [375 kcal],
  pdf.header-cell(scope: "row")[Protein],
  [8g], [12g],
  pdf.header-cell(scope: "row")[Fat],
  [12g], [18g],
  pdf.header-cell(scope: "row")[Carbs],
  [30g], [45g],
)

```

## Parameters  Question mark    Parameters are the inputs to a function. They are specified in parentheses after the function name.   const f="ontransitionend"in window,u=window.matchMedia("(prefers-reduced-motion: reduce)").matches,v=window.matchMedia("(hover: hover)");let w=v.matches;v.addEventListener("change",i=>{w=i.matches});function p(i){const n=i.querySelector("svg"),e=i.querySelector("div[role='tooltip']");if(!n||!e)return;let o=!1;const d=n.getElementsByTagName("title")[0];let m=d.textContent,c=0;const r=256,a=()=>{const t=window.innerWidth,l=n.getBoundingClientRect();l.left+r/2>t?(e.style.left=`${t-r-l.left-32}px`,e.classList.add("mobile")):l.left-r/2<0?(e.style.left=`${-l.left+32}px`,e.classList.add("mobile")):(e.style.left="-120px",e.classList.remove("mobile")),o=!0,d.innerHTML="",e.style.display="block",window.requestAnimationFrame(()=>{e.style.opacity="1",e.style.pointerEvents="auto",e.removeAttribute("aria-hidden")}),c=Date.now()},s=()=>{d&&(d.innerHTML=m??""),o=!1;const t=()=>{e.style.display="none",e.style.pointerEvents="none",e.setAttribute("aria-hidden","true")};f&&!u?e.addEventListener("transitionend",t,{once:!0}):t(),window.requestAnimationFrame(()=>{f&&!u&&(e.style.opacity="0")})};n.addEventListener("click",()=>{w||(o&&Date.now()-c>100?s():a())}),n.addEventListener("mouseenter",t=>{t.preventDefault(),a()}),n.addEventListener("mousemove",t=>{o&&t.preventDefault()}),n.addEventListener("focus",a),n.addEventListener("blur",s),n.addEventListener("mouseleave",s),window.addEventListener("click",t=>{o&&!i.contains(t.target)&&s()}),window.addEventListener("mouseleave",s),window.addEventListener("keydown",t=>{o&&t.key==="Escape"&&s()})}for(const i of document.querySelectorAll("div.tooltip-context"))p(i);  pdf.header-cell([level: ][int],[scope: ][str],[content],) -> [content]  

### `level`   [int]    

The nesting level of this header cell.
 

 Default: `1` 
 

### `scope`   [str]    

What track of the table this header cell applies to.
 VariantDetails`"both"`

The header cell refers to both the row and the column.
`"column"`

The header cell refers to the column.
`"row"`

The header cell refers to the row.
 

 Default: `"column"` 
 

### `cell`   [content]  Required  Positional  Question mark    Positional parameters are specified in order, without names.      

The table cell.
 

This can be content or a call to [`table.cell`].
 [Data CellPrevious page] [Table SummaryNext page]