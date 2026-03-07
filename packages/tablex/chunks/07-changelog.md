## Changelog

### v0.0.9

NOTE: Please use Typst’s built-in tables instead of tablex (starting with Typst 0.11.0).
Most of tablex’s features were implemented in Typst’s tables by the author of tablex.

* Added compatibility with Typst v0.12.0 (https://github.com/PgBiel/typst-tablex/issues/135)

* Added library usage notice to README

* Tablex is now dual-licensed under MIT/Apache-2.0 (https://github.com/PgBiel/typst-tablex/issues/134)

### v0.0.8

* Added `fit-spans` option to `tablex` and `cellx` (https://github.com/PgBiel/typst-tablex/pull/111)

Accepts `(x: bool, y: bool)`. When set to `(x: true)`, colspans won’t affect the sizes of `auto` columns. When set to `(y: true)`, rowspans won’t affect the sizes of `auto` rows.

* Defaults to `false`, equivalent to `(x: false, y: false)`, that is, colspans and rowspans affect the sizes of `auto` tracks (columns and rows) by default (expanding the last spanned track if the colspan/rowspan is too large).

* Useful when you want merged cells (or a specific merged cell) to “fit” within their spanned columns and rows. May help when adding a colspan or rowspan causes an `auto`-sized track to inadvertently expand.

* `auto` column sizing received multiple improvements and bug fixes. Tables should now have more natural column widths. (https://github.com/PgBiel/typst-tablex/pull/109, https://github.com/PgBiel/typst-tablex/pull/116)

Fixes some problems with overflowing cells (https://github.com/PgBiel/typst-tablex/issues/48, https://github.com/PgBiel/typst-tablex/issues/75)

* Fixes `auto` columns being needlessly expanded in some cases (https://github.com/PgBiel/typst-tablex/issues/56, https://github.com/PgBiel/typst-tablex/issues/78)

For similar problems not fixed by this, please use the new `fit-spans` option as needed, or use fixed-size columns instead.

* Several performance optimizations and other internal code improvements were made (https://github.com/PgBiel/typst-tablex/pull/113, https://github.com/PgBiel/typst-tablex/pull/114, https://github.com/PgBiel/typst-tablex/pull/115).

Documents with lots of `tablex` tables might now become up to 20% faster to cold compile. Give it a shot!

* Fixed extra fixed-height rows appearing to have `auto` height (https://github.com/PgBiel/typst-tablex/pull/108).

* Fixed rows without any visible cells being drawn with zero height (https://github.com/PgBiel/typst-tablex/pull/107).

Fixes some rowspans causing cells to overlap (https://github.com/PgBiel/typst-tablex/issues/82, https://github.com/PgBiel/typst-tablex/issues/105).

### v0.0.7

I have begun work on bringing many tablex improvements to built-in Typst tables! In that regard, you can now sponsor my work on tablex and improving Typst tables via GitHub Sponsors! Consider taking a look :)

* Allow gradients and patterns in fills (https://github.com/PgBiel/typst-tablex/pull/87)

* Fixed a critical bug where `line` in tablex cells would misbehave (https://github.com/PgBiel/typst-tablex/issues/80)

CeTZ and drawing in general should now work properly within tablex cells (see https://github.com/johannes-wolf/cetz/issues/345).

* Also fixes a problem with nested tables (https://github.com/PgBiel/typst-tablex/issues/34)

* Fixed negative line expansion within a single cell (https://github.com/PgBiel/typst-tablex/pull/84)

Negative line expansion across multiple cells isn’t yet supported.

* Thanks GitHub user @dixslyf for the great work on fixing and testing this!

* Made internal length calculation procedures more robust (https://github.com/PgBiel/typst-tablex/issues/92, https://github.com/PgBiel/typst-tablex/issues/94)

Fixes a potential incompatibility with (currently unreleased) Typst 0.11.0

* Added missing support for boolean types in Typst 0.8.0+ (https://github.com/PgBiel/typst-tablex/issues/73)

* Added some keywords to tablex’s `typst.toml` for better discoverability (https://github.com/PgBiel/typst-tablex/issues/91)

### v0.0.6

* Added support for RTL tables with `rtl: true` (https://github.com/PgBiel/typst-tablex/issues/58).

Default Typst tables are automatically flipped horizontally when using `set text(dir: rtl)`, however we can’t detect that setting from tablex at this moment (it isn’t currently possible to fetch set rules in Typst).

* Therefore, as a way around that, you can now specify `#tablex(rtl: true, ...)` to flip your table horizontally if you’re writing a document in RTL (right-to-left) script. (You can use e.g. `#let old-tablex = tablex` followed by `#let tablex(..args) = old-tablex(rtl: true, ..args)` to not have to repeat the `rtl` parameter every time.)

* Added support for `box`’s dictionary inset syntax on tablex (https://github.com/PgBiel/typst-tablex/issues/54).

For instance, you can now do `#tablex(inset: (left: 5pt, top: 10pt, rest: 2pt), ...)`.

* Fixed errors when using floating point strokes or other more complex strokes (https://github.com/PgBiel/typst-tablex/issues/55).

* Added full compatibility with the new Typst 0.8.0 type system (https://github.com/PgBiel/typst-tablex/issues/69).

* Added info about `#rotate` problems to “Known Issues” in the README (https://github.com/PgBiel/typst-tablex/pull/60).

* Improved docs for tablex options `columns` and `rows` (https://github.com/PgBiel/typst-tablex/issues/53).

### v0.0.5

* ⚠️ Minimum Typst version raised to v0.2.0

* Improved calculation of page/container dimensions by using the `layout()` function.

Fixes tables with fractional columns not displaying properly in blocks with `auto` width (https://github.com/PgBiel/typst-tablex/issues/44; https://github.com/PgBiel/typst-tablex/issues/39)

* Fixes some nested tables overflowing the page width (https://github.com/PgBiel/typst-tablex/issues/41)

* Fixes bad interaction between tables with fractional columns and nested tables (https://github.com/PgBiel/typst-tablex/issues/28)

* Fixes table rotation messing up table size calculation (https://github.com/PgBiel/typst-tablex/issues/52)

* Probably fixes other issues not listed here as well.

* Added some guards for infinite lengths and `auto`-sized pages (https://github.com/PgBiel/typst-tablex/issues/47).

* Fixed tablex crashes/improper behavior with `em` strokes and other types of strokes (https://github.com/PgBiel/typst-tablex/issues/49).

* Added the tablex version number as a comment in the source file (as requested in https://github.com/PgBiel/typst-tablex/issues/25).

### v0.0.4

* Added `typst.toml` to support Typst v0.6.0’s soon-to-be-released package manager (see https://github.com/PgBiel/typst-tablex/issues/22).

* Fixed a division by zero regression from v0.0.3 (https://github.com/PgBiel/typst-tablex/issues/19).

* Fixed a bug where cells placed in arbitrary positions could force an extra empty row to appear (https://github.com/PgBiel/typst-tablex/issues/16).

* Fixed `hlinex(gutter-restrict: top)` causing the hline to just disappear (https://github.com/PgBiel/typst-tablex/issues/20).

* Fixed certain `gutter-restrict` lines disappearing when there’s no gutter (https://github.com/PgBiel/typst-tablex/issues/21).

* Fixed row gutter lines not properly splitting across pages (https://github.com/PgBiel/typst-tablex/issues/23).

### v0.0.3

* Added support for Typst v0.4.0 and v0.5.0.

The tablex options `fill:` and `align:` now accept arrays of values for each column (https://github.com/PgBiel/typst-tablex/issues/13).

For example, `fill: (red, blue)` would fill the first column with red, the second column with blue, and any further columns would alternate between the two fill colors.

* Fixed the calculation of the size of `auto` rows and columns when a rowspan or colspan was used (https://github.com/PgBiel/typst-tablex/issues/11).

* Fixed the calculation of the size of the last `auto` column when it was too long (https://github.com/PgBiel/typst-tablex/issues/6).

### v0.0.2

* Added support for Typst v0.3.0.

* Fixed strokes - now lines will expand to not look weird when strokes are larger.

You can disable this behavior by setting `stroke-expand: false` on your lines.

* You can now arbitrarily change your lines’ sizes at either end with the option `expand: (length, length)`; e.g. `expand: (5pt, 10pt)` will increase your horizontal line 5pt to the left and 10pt to the right (or, for a vertical line, 5pt to the top and 10pt to the bottom).

Support for negative expand lengths is limited (so far, only reduces length in the first cell the line spans).

* Added some gutter fixes (not all gutter issues were fixed yet).

### v0.0.1

Initial release.

* Added types `tablex`, `cellx`, `hlinex`, `vlinex`

* Added type aliases `gridx`, `rowspanx`, `colspanx`