## Reference

### Basic types and functions

* `cellx`: Represents a table cell, and is initialized as follows:
#let cellx(content,
  x: auto, y: auto,
  rowspan: 1, colspan: 1,
  fill: auto, align: auto,
  inset: auto,
  fit-spans: auto
) = (
  tablex-dict-type: "cell",
  content: content,
  rowspan: rowspan,
  colspan: colspan,
  align: align,
  fill: fill,
  inset: inset,
  fit-spans: fit-spans,
  x: x,
  y: y,
)

where:

`tablex-dict-type` is the type marker

* `content` is the cell’s content (either `content` or a function with `(col, row) => content`)

* `rowspan` is how many rows this cell spans (default 1)

* `colspan` is how many columns this cell spans (default 1)

* `align` is this cell’s align override, such as “center” (default `auto` to follow the rest of the table)

* `fill` is this cell’s fill override, such as “blue” (default `auto` to follow the rest of the table)

* `inset` is this cell’s inset override, such as `5pt` (default `auto` to follow the rest of the table)

* `fit-spans` allows overriding the table-wide `fit-spans` setting for this specific cell (e.g. if this cell has a `colspan` greater than 1, `fit-spans: (x: true)` will cause it to not affect the sizes of `auto` columns).

* `x` is the cell’s column index (0…len-1) - `auto` indicates it wasn’t assigned yet

* `y` is the cell’s row index (0…len-1) - `auto` indicates it wasn’t assigned yet

* `hlinex`: represents a horizontal line:
#let hlinex(
  start: 0, end: auto, y: auto,
  stroke: auto,
  stop-pre-gutter: auto, gutter-restrict: none,
  stroke-expand: true,
  expand: none
) = (
  tablex-dict-type: "hline",
  start: start,
  end: end,
  y: y,
  stroke: stroke,
  stop-pre-gutter: stop-pre-gutter,
  gutter-restrict: gutter-restrict,
  stroke-expand: stroke-expand,
  expand: expand,
  parent: none,
)

where:

`tablex-dict-type` is the type marker

* `start` is the column index where the hline starts from (default `0`, a.k.a. the beginning)

* `end` is the last column the hline touches (default `auto`, a.k.a. all the way to the end)

Note that hlines will not be drawn over cells with `colspan` larger than 1, even if their spans (`start`-`end`) include that cell.

* `y` is the index of the row at the top of which the hline is drawn. (Defaults to `auto`, a.k.a. depends on where you placed the `hline` among the table items - it’s always on the top of the row below the current one.)

* `stroke` is the hline’s stroke override (defaults to `auto`, a.k.a. follow the rest of the table).

* `stop-pre-gutter`: When `true`, the hline will not be drawn over gutter (which is the default behavior of tables). Defaults to `auto` which is essentially `false` (draw over gutter).

* `gutter-restrict`: Either `top`, `bottom`, or `none`. Has no effect if `row-gutter` is set to `none`. Otherwise, defines if this `hline` should be drawn only on the top of the row gutter (`top`); on the bottom (`bottom`); or on both the top and the bottom (`none`, the default). Note that `top` and `bottom` are alignment values (not strings).

* `stroke-expand`: When `true`, the hline will be extended as necessary to cover the stroke of the vlines going through either end of the line. Defaults to `true`.

* `expand`: Optionally extend the hline by an arbitrary length. When `none`, it is not expanded. When a length (such as `5pt`), it is expanded by that length on both ends. When an array of two lengths (such as `(5pt, 10pt)`), it is expanded to the left by the first length (in this case, `5pt`) and to the right by the second (in this case, `10pt`). Defaults to `none`.

* `parent`: An internal attribute determined when splitting lines among cells. (It should always be `none` on user-facing interfaces.)

* `vlinex`: represents a vertical line:
#let vlinex(
  start: 0, end: auto, x: auto,
  stroke: auto,
  stop-pre-gutter: auto, gutter-restrict: none,
  stroke-expand: true,
  expand: none
) = (
  tablex-dict-type: "vline",
  start: start,
  end: end,
  x: x,
  stroke: stroke,
  stop-pre-gutter: stop-pre-gutter,
  gutter-restrict: gutter-restrict,
  stroke-expand: stroke-expand,
  expand: expand,
  parent: none,
)

where:

`tablex-dict-type` is the type marker

* `start` is the row index where the vline starts from (default `0`, a.k.a. the top)

* `end` is the last row the vline touches (default `auto`, a.k.a. all the way to the bottom)

Note that vlines will not be drawn over cells with `rowspan` larger than 1, even if their spans (`start`-`end`) include that cell.

* `x` is the index of the column to the left of which the vline is drawn. (Defaults to `auto`, a.k.a. depends on where you placed the `vline` among the table items.)

For a `vline` to be placed after all columns, its `x` value will be equal to the amount of columns (which isn’t a valid column index, but it’s what is used here).

* `stroke` is the vline’s stroke override (defaults to `auto`, a.k.a. follow the rest of the table).

* `stop-pre-gutter`: When `true`, the vline will not be drawn over gutter (which is the default behavior of tables). Defaults to `auto` which is essentially `false` (draw over gutter).

* `gutter-restrict`: Either `left`, `right`, or `none`. Has no effect if `column-gutter` is set to `none`. Otherwise, defines if this `vline` should be drawn only to the left of the column gutter (`left`); to the right (`right`); or on both the left and the right (`none`, the default). Note that `left` and `right` are alignment values (not strings).

* `stroke-expand`: When `true`, the vline will be extended as necessary to cover the stroke of the hlines going through either end of the line. Defaults to `true`.

* `expand`: Optionally extend the vline by an arbitrary length. When `none`, it is not expanded. When a length (such as `5pt`), it is expanded by that length on both ends. When an array of two lengths (such as `(5pt, 10pt)`), it is expanded towards the top by the first length (in this case, `5pt`) and towards the bottom by the second (in this case, `10pt`). Defaults to `none`.

* `parent`: An internal attribute determined when splitting lines among cells. (It should always be `none` on user-facing interfaces.)

* The `occupied` type is an internal type used to represent cell positions occupied by cells with `colspan` or `rowspan` greater than 1.

* Use `is-tablex-cell`, `is-tablex-hline`, `is-tablex-vline` and `is-tablex-occupied` to check if a particular object has the corresponding type marker.

* `colspanx` and `rowspanx` are shorthands for setting the `colspan` and `rowspan` attributes of `cellx`. They can also be nested (one given as an argument to the other) to combine their properties (e.g., `colspanx(2)(rowspanx(3)[a])`). They accept all other cell properties with named arguments. For example, `colspanx(2, align: center)[b]` is equivalent to `cellx(colspan: 2, align: center)[b]`.

### Gridx and Tablex

* `gridx` is equivalent to `tablex` with `auto-lines: false`; see below.

* `tablex:` The main function for creating a table with this library:
#let tablex(
  columns: auto, rows: auto,
  inset: 5pt,
  align: auto,
  fill: none,
  stroke: auto,
  column-gutter: auto, row-gutter: auto,
  gutter: none,
  repeat-header: false,
  header-rows: 1,
  header-hlines-have-priority: true,
  auto-lines: true,
  auto-hlines: auto,
  auto-vlines: auto,
  map-cells: none,
  map-hlines: none,
  map-vlines: none,
  map-rows: none,
  map-cols: none,
  ..items
) = {
// ...
}

Parameters:

`columns`: The sizes (widths) of each column. They work just like regular `table`’s columns, and can be:

an array of lengths (`1pt`, `2em`, `100%`, …), including fractional (`2fr`), to specify the width of each column

For instance, `columns: (2pt, 3em)` will give you two columns: one with a width of `2pt` and another with the width of `3em` (3 times the font size).

Note that percentages, such as `49%`, are considered fixed widths as they are always multiplied by the full page width (minus margins) for columns. Thus, a column with a size of `100%` would span your whole page (even if there are other columns).

* `auto` may be specified to automatically resize the column based on the largest width of its contents, if possible - this is the most common column width choice, as it just delegates the column sizing job to tablex!

For example, if your `auto`-sized column contains two cells with `Hello world!` and `Bye!` as contents, tablex will try to make the column large enough for `Hello world!` (the cell with largest potential width) to fit in a single line.

* However, note that often enough that’s not possible, as increasing the column’s size too much would result in the table going over the page’s margin - perhaps even beyond the document’s total width. Therefore, tablex will automatically reduce the size of your `auto` columns when they would otherwise cause the table to overrun the page’s normal width (i.e. the width between the page’s lateral margins).

Fixed width columns (such as `2pt`, `3em` or `49%`) are not subject to this size reduction; thus, if you specify all columns’ widths with fixed lengths, your table could become larger than the page’s width! (In such a case, `auto` columns would be reduced to a size of zero, as there would be no available space anymore!)

* when specifying fractional widths (`1fr`, `2fr`…) for columns, the available space (remaining page width, after calculating all other columns’ sizes) is divided between them, weighted on the fraction value of each column.

For example, with `(1fr, 2fr)`, the available space will be divided by 3 (1 + 2), and the first column will have 1/3 of the space, while the second will have 2/3.

`(1fr, 1fr)` would cause both columns to have equal length (1/2 and 1/2 of the available space).

* This is useful when you want some columns to just occupy all the remaining horizontal space in the page.

Note: If only one column has a fractional width (e.g. a single column with `1fr`), it will occupy the entire available space.

* Warning: fractional columns in tablex (much like in Typst’s default tables) will not work properly in pages with `auto` width (the columns will have width zero) - this is because those pages theoretically have infinite width (they can expand indefinitely), so having columns spanning the entire available width is then impossible!

* a single length like above, to indicate the width of a single column (equivalent to just placing it inside a unit array)

For instance, `columns: 2pt` is equivalent to `columns: (2pt,)`, which translates to a single column of width `2pt`.

* an integer (such as `4`), as a shorthand for `(auto,) * 4` (that many `auto` columns)

Useful if you just want to quickly set the amount of columns without worrying about their sizes (`columns: 4` will give you four `auto` columns).

* `rows`: The sizes (heights) of each row. They follow the exact same format as `columns`, except that the “available space” is infinite (auto rows can expand as much as is needed, as the table can add rows over multiple pages).

Note: For rows, percentages (such as `49%`) are fixed width lengths, like in `columns`; however, here, they are multiplied by the page’s full height (minus margins), and not width.

* Note: If more rows than specified are added, the height for the last row will be the one assigned to all extra rows. (If the last row is `auto`, the extra ones will also be `auto`, for example.)

Your table can have more rows than expected by simply having more cells than `(# columns)` multiplied by `(# rows)`. In this case, you will have an extra row for each `(# columns)` cells after the limit. In other words, the amount of columns is always fixed (determined by the amount of widths in the array given to `columns`), but the amount of rows can vary depending on your input of cells to the table.

* Adding a cell at an arbitrary `y` coordinate can also cause your table to have extra rows (enough rows to reach the cell at that coordinate).

* Warning: support for fractional sizes for rows is still rudimentary - they only work properly on the table’s first page; on the second page and onwards, they will not behave properly, differently from the default `#table`.

* `inset`: Inset/internal padding to give to each cell. Can be either a length (same inset from the top, bottom, left and right of the cell), or a dictionary (e.g. `(left: 5pt, right: 10pt, bottom: 2pt, top: 4pt)`, or even `(left: 5pt, rest: 10pt)` to apply the same value to the remaining sides). Defaults to `5pt` (the `#table` default).

* `align`: How to align text in the cells. Defaults to `auto`, which inherits alignment from the outer context. Must be either `auto`, an `alignment` (such as `left` or `top`), a `2d alignment` (such as `left + top`), an `array` of alignment/2d alignment (one for each column in the table - if there are more columns than alignment values, they will alternate); or a function `(column, row) => alignment/2d alignment` (to customize for each individual cell).

* `fill`: Color with which to fill cells’ backgrounds. Defaults to `none`, or no fill. Must be either a `color`, such as `blue`; an `array` of colors (one for each column in the table - if there are more columns than colors, they will alternate); or a function `(column, row) => color` (to customize for each individual cell).

* `stroke`: Indicates how to draw the table lines. Defaults to the current line styles in the document. For example: `5pt + red` to change the color and the thickness.

* `column-gutter`: optional separation (length) between columns (such as `5pt`). Defaults to `none` (disable). At the moment, looks a bit ugly if your table has a `hline` attempting to cross a `colspan`.

* `row-gutter`: optional separation (length) between rows. Defaults to `none` (disable). At the moment, looks a bit ugly if your table has a `vline` attempting to cross a `rowspan`.

* `gutter`: Sets a length to both `column-` and `row-gutter` at the same time (overridable by each).

* `repeat-header`: Controls header repetition. If set to `true`, the first row (or the amount of rows specified in `header-rows`), including its rowspans, is repeated across all pages this table spans. If set to `false` (default), the aforementioned header row is not repeated in any page. If set to an integer (such as `4`), repeats for that many pages after the first, then stops. If set to an array of integers (such as `(3, 4)`), repeats only on those pages relative to the table’s first page (page 1 here is where the table is, so adding `1` to said array has no effect).

* `header-rows`: minimum amount of rows for the repeatable
header. 1 by default. Automatically increases if
one of the cells is a rowspan that would go beyond the
given amount of rows. For example, if 3 is given,
then at least the first 3 rows will repeat.

* `header-hlines-have-priority`: if `true`, the horizontal
lines below the header being repeated take priority
over the rows they appear atop of on further pages.
If `false`, they draw their own horizontal lines.
Defaults to `true`.

For example, if your header has a blue hline under it, that blue hline will display on all pages it is repeated on if this option is `true`. If this option is `false`, the header will repeat, but the blue hline will not.

* `rtl`: if true, the table is horizontally flipped. That is, cells and lines are placed in the opposite order (starting from the right), and horizontal lines are flipped.
This is meant to simulate the behavior of default Typst tables when `set text(dir: rtl)` is used,
and is useful when writing in a language with a RTL (right-to-left) script.
Defaults to `false`.

* `auto-lines`: Shorthand to apply a boolean to both `auto-hlines` and `auto-vlines` at the same time (overridable by each). Defaults to `true`.

* `auto-hlines`: If `true`, draw a horizontal line on every line where you did not manually draw one; if `false`, no hlines other than the ones you specify (via `hlinex`) are drawn. Defaults to `auto` (follows `auto-lines`, which in turn defaults to `true`).

* `auto-vlines`: If `true`, draw a vertical line on every line where you did not manually draw one; if `false`, no vlines other than the ones you specify (via `vlinex`) are drawn. Defaults to `auto` (follows `auto-lines`, which in turn defaults to `true`).

* `map-cells`: A function which takes a single `cellx` and returns another `cellx`, or a `content` which is converted to `cellx` by `cellx[#content]`. You can customize the cell in pretty much any way using this function; just take care to avoid conflicting with already-placed cells if you move it.

* `map-hlines`: A function which takes each horizontal line object (`hlinex`) and returns another, optionally modifying its properties. You may also change its row position (`y`). Note that this is also applied to lines generated by `auto-hlines`.

* `map-vlines`: A function which takes each horizontal line object (`vlinex`) and returns another, optionally modifying its properties. You may also change its column position (`x`). Note that this is also applied to lines generated by `auto-vlines`.

* `map-rows`: A function mapping each row of cells to new values or modified properties.
Takes `(row_num, cell_array)` and returns
the modified `cell_array`. Note that, with your function, they
cannot be sent to another row. Also, please preserve the order of the cells. This is especially important given that cells may be `none` if they’re actually a position taken by another cell with colspan/rowspan. Make sure the `none` values are in the same indexes when the array is returned.

* `map-cols`: A function mapping each column of cells to new values or modified properties.
Takes `(col_num, cell_array)` and returns
the modified `cell_array`. Note that, with your function, they
cannot be sent to another column. Also, please preserve the order of the cells. This is especially important given that cells may be `none` if they’re actually a position taken by another cell with colspan/rowspan. Make sure the `none` values are in the same indexes when the array is returned.

* `fit-spans`: either a dictionary `(x: bool, y: bool)` or just `bool` (e.g. just `true` is converted to `(x: true, y: true)`). When given `(x: true)`, colspans won’t affect the sizes of `auto` columns. When given `(y: true)`, rowspans won’t affect the sizes of `auto` rows. By default, this is equal to `(x: false, y: false)` (equivalent to just `false`), which means that colspans will cause the last spanned `auto` column to expand (depending on the contents of the cell) and rowspans will cause the last spanned `auto` row to expand similarly.

This is usually used as `(x: true)` to prevent unexpected expansion of `auto` columns after using a colspan, which can happen when a colspan spans both a fractional-size column (e.g. `1fr`) and an `auto`-sized column. Can be applied to rows too through `(y: true)` or `(x: true, y: true)`, if needed, however.

* The point of this option is to have colspans and rowspans not affect the size of the table at all, and just “fit” within the columns and rows they span. Therefore, this option does not have any effect upon colspans and rowspans which don’t span columns or rows with automatic size.