## 0.1.0 Roadmap

* [ ] General

[X] More docs

* [ ] Code cleanup

* [ ] Table drawing rework

* [ ] `#table` parity

[X] `columns:`, `rows:`

[X] Basic support

* [X] Accept a single size to mean a single column

* [X] Adjust `auto` columns and rows

* [X] Accept integers to mean multiple `auto`

* [X] Basic unit conversion (em -> pt, etc.)

* [X] Ratio unit conversion (100% -> page width…)

* [X] Fractional unit conversion based on available space (1fr, 2fr -> 1/3, 2/3)

* [X] Shrink `auto` columns based on available space

* [X] `fill`

[X] Basic support (`color` for general fill)

* [X] Accept a function (`(column, row) => color`)

* [X] Accept an array of colors (one for each column)

* [X] `align`

[X] Basic support (`alignment` and `2d alignment` apply to all cells)

* [X] Accept a function (`(column, row) => alignment/2d alignment`)

* [X] Accept an array of alignment values (one for each column)

* [X] `inset`

* [ ] `gutter`

[X] Basic support

[X] `column-gutter`

* [X] `row-gutter`

* [ ] Hline, vline adaptations

[X] `stop-pre-gutter`: Makes the hline/vline not transpose gutter boundaries

* [X] `gutter-restrict`: Makes the hline/vline not draw on both sides of a gutter boundary, and instead pick one (top/bottom; left/right)

* [ ] Properly work with gutters after colspanxs/rowspanxs

* [X] `stroke`

[X] Basic support (change all lines, vline or hline, without override)

* [X] `none` for no stroke

* [X] Default to lines on every row and column

* [ ] New features for `#tablex`

[X] Basic types (`cellx`, `hlinex`, `vlinex`)

* [X] `hlinex`, `vlinex`

[X] Auto-positioning when placed among cells

* [X] Arbitrary positioning

* [X] Allow customizing `stroke`

* [X] `colspanx`, `rowspanx`

[X] Interrupt `hlinex` and `vlinex` with `end: auto`

* [X] Support simultaneous col/rowspan with `cellx(colspanx:, rowspanx:)`

* [X] Support nesting colspan/rowspan (`colspanx(rowspanx())`)

* [X] Support cell attributes (e.g. `colspanx(2, align: left)[a]`)

* [X] Reliably detect conflicts

* [ ] Repeating headers

[X] Basic support (first row group repeats on every page)

* [ ] Work with different page sizes

* [X] `repeat-header`: Control header repetition

[X] `true`: Repeat on all pages

* [X] integer: Repeat for the next ‘n’ pages

* [X] array of integers: Repeat on those (relative) pages

* [X] `false` (default): Do not repeat

* [X] `header-rows`: Indicate what to consider as a “header”

[X] integer: At least first ‘n’ rows are a header (plus whatever rowspanxs show up there)

[X] Defaults to 1

* [X] `none` or `0`: no header (disables header repetition regardless of `repeat-header`)

* [X] `cellx`

[X] Auto-positioning based on order and columns

* [X] Place empty cells when there are too many

* [X] Allow arbitrary positioning with `cellx(x:, y:)`

* [X] Allow `align` override

* [X] Allow `fill` override

* [X] Allow `inset` override

[X] Works properly only with `auto` cols/rows

* [X] Dynamic content (maybe shortcut for `map-cells` on a single cell)

* [X] Auto-lines

[X] `auto-hlines` - `true` to place on all lines without hlines, `false` otherwise

* [X] `auto-vlines` - similar

* [X] `auto-lines` - controls both simultaneously (defaults to `true`)

* [X] Iteration attributes

[X] `map-cells` - Customize every single cell

* [X] `map-hlines` - Customize each horizontal line

* [X] `map-vlines` - Customize each vertical line

* [X] `map-rows` - Customize entire rows of cells

* [X] `map-cols` - Customize entire columns of cells