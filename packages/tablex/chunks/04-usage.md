## Usage

NOTE: Please use built-in tables instead of this library (see notice above). The rest of the README is kept for reference purposes only.

To use this library through the Typst package manager (for Typst v0.6.0+), write for example `#import "@preview/tablex:0.0.9": tablex, cellx` at the top of your Typst file (you may also add whichever other functions you use from the library to that import list!).

For older Typst versions, download the file `tablex.typ` from the latest release (or directly from the main branch, for the ‘bleeding edge’) at the tablex repository (https://github.com/PgBiel/typst-tablex) and place it on the same folder as your own Typst file. Then, at the top of your file, write for example `#import "tablex.typ": tablex, cellx` (plus whichever other functions you use from the library).

This library should be compatible with Typst versions between v0.2.0 and v0.12.0 (inclusive).
Using the latest Typst version is always recommended in order to make use of the latest optimizations and features available.

Here’s an example of what `tablex` can do:

Here’s the code for that table:

#import "@preview/tablex:0.0.9": tablex, rowspanx, colspanx

#tablex(
  columns: 4,
  align: center + horizon,
  auto-vlines: false,

  // indicate the first two rows are the header
  // (in case we need to eventually
  // enable repeating the header across pages)
  header-rows: 2,

  // color the last column's cells
  // based on the written number
  map-cells: cell => {
    if cell.x == 3 and cell.y > 1 {
      cell.content = {
        let value = int(cell.content.text)
        let text-color = if value  new_hline` and `map-vlines: v => new_vline`. This includes any automatically generated lines. For example:

#import "@preview/tablex:0.0.9": tablex, colspanx, rowspanx

#tablex(
  columns: 3,
  map-hlines: h => (..h, stroke: blue),
  map-vlines: v => (..v, stroke: green + 2pt),
  colspanx(2)[a], (),  [b],
  [c], rowspanx(2)[d], [ed],
  [f], (),             [g]
)

### Customize every single cell

Cells can be customized entirely. Instead of specifying content (e.g. `[text]`) as a table item, you can specify `cellx(property: a, property: b, ...)[text]`, which allows you to customize properties, such as:

* `colspan: 2` (same as using `colspanx(2, ...)[...]`)

* `rowspan: 3` (same as using `rowspanx(3, ...)[...]`)

* `align: center` (override whole-table alignment for this cell)

* `fill: blue` (fill just this cell with that color)

* `inset: 0pt` (override inset/internal padding for this cell - note that this can look off unless you use auto columns and rows)

* `x: 5` (arbitrarily place the cell at the given column, beginning at 0 - may error if conflicts occur)

* `y: 6` (arbitrarily place the cell at the given row, beginning at 0 - may error if conflicts occur)

Additionally, instead of specifying content to the cell, you can specify a function `(column, row) => content`, allowing each cell to be aware of where it’s positioned. (Note that positions are recorded in the cell’s `.x` and `.y` attributes, and start as `auto` unless you specify otherwise.)

For example:

#import "@preview/tablex:0.0.9": tablex, cellx, colspanx, rowspanx

#tablex(
  columns: 3,
  fill: red,
  align: right,
  colspanx(2)[a], (),  [beeee],
  [c], rowspanx(2)[d], cellx(fill: blue, align: left)[e],
  [f], (),             [g],

  // place this cell at the first column, seventh row
  cellx(colspan: 3, align: center, x: 0, y: 6)[hi I'm down here]
)

#### Bulk customization of cells

To customize multiple cells at once, you have a few options:

* `map-cells: cell => cell` (given a cell, returns a new cell). You can use this to customize the cell’s attributes, but also  to change its positions (however, avoid doing that as it can easily generate conflicts). You can access the cell’s position with `cell.x` and `cell.y`. All other attributes are also accessible and changeable (see the `Reference` further below for a list). Return something like `(..cell, fill: blue)`, for example, to ensure the other properties (including the cell type marker) are kept. (Calling `cellx` here is not necessary. If overriding the cell’s content, use `content: [whatever]`). This is useful if you want to, for example, customize a cell’s fill color based on its contents, or add some content to every cell, or something similar.

* `map-rows: (row_index, cells) => cells` (given a row index and all cells in it, return a new array of cells). Allows customizing entire rows, but note that the cells in the `cells` parameter can be `none` if they’re some position occupied by a colspan or rowspan of another cell. Ensure you return the cells in the order you were given, including the `none`s, for best results. Also, you cannot move cells here to another row. You can change the cells’ columns (by changing their `x` property), but that will certainly generate conflicts if any col/rowspans are involved (in general, you cannot bulk-change col/rowspans without `map-cells`).

* `map-cols: (col_index, cells) => cells` (given a column index and all cells in it, return a new array of cells). Similar to `map-rows`, but for customizing columns. You cannot change the column of any cell here. (To do that, `map-cells` is required.) You can, however, change its row (with `y`, but do that sparingly), and, of course, all other properties.

Note: Execution order is `map-cells` => `map-rows` => `map-cols`.

Example:

#import "@preview/tablex:0.0.9": tablex, colspanx, rowspanx

#tablex(
  columns: 4,
  auto-vlines: true,

  // make all cells italicized
  map-cells: cell => {
    (..cell, content: emph(cell.content))
  },

  // add some arbitrary content to entire rows
  map-rows: (row, cells) => cells.map(c =>
    if c == none {
      c  // keeping 'none' is important
    } else {
      (..c, content: [#c.content\ *R#row*])
    }
  ),

  // color cells based on their columns
  // (using 'fill: (column, row) => color' also works
  // for this particular purpose)
  map-cols: (col, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if col  (blue, red, green).at(calc.rem(row + col - 1, 3)),
  map-cols: (col, cells) => {
    let last = cells.last()
    last.content = [
      #cells.slice(0, cells.len() - 1).fold(0, (acc, c) => if c != none { acc + eval(c.content.text) } else { acc })
    ]
    last.fill = aqua
    cells.last() = last
    cells
  },
  [0], [5], [10],
  [1], [6], [11],
  [2], [7], [12],
  [3], [8], [13],
  [4], [9], [14],
  [s], [s], [s]
)