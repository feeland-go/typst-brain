## Known Issues

* Filled cells will partially overlap with horizontal lines above them (see https://github.com/PgBiel/typst-tablex/issues/4).

To be fixed in a future rework of the table drawing process.

* Table lines don’t play very well with column and row gutter when a colspan or rowspan is used. They may be missing or be cut off by gutters.

* Repeatable table headers might not behave properly depending on the size of your document or other factors (https://github.com/PgBiel/typst-tablex/issues/43).

* Using tablex (especially when using repeatable header rows) may cause a warning, “layout did not converge within 5 attempts”, to appear on recent Typst versions (https://github.com/PgBiel/typst-tablex/issues/38). This warning is due to how tablex works internally and is not your fault (in principle), so don’t worry too much about it (unless you’re sure it’s not tablex that is causing this).

* Rows with fractional height (such as `2fr`) have zero height if the table spans more than one page. This is because fractional row heights are calculated on the available height of the first page of the table, which is something that the default `#table` can circumvent using internal code. This won’t be fixed for now. (Columns with fractional width work fine, provided all pages the table is in have the same width, and the page width isn’t `auto` (which forces fractional columns to be 0pt, even in the default `#table`).)

* Rotation (via Typst’s `#rotate`) of text only affects the visual appearance of the text on the page, but does not change its dimensions as they factor into the layout.
This leads to certain visual issues, such as rotated text potentially overflowing the cell height without being hyphenated or, inversely, being hyphenated even though there is enough space vertically (https://github.com/PgBiel/typst-tablex/issues/59).
This is a known issue with Typst (perhaps, in the future, `#rotate` may get a setting to affect layout).
As a workaround for the text hyphenation problem, the content can be boxed (and thus grouped together) with `#box` (e.g., `rowspanx(7, box(rotate(-90deg, [*donothyphenatethis*])))`), or hyphenation can be prevented by setting `#text(hyphenate: false, ...)` (e.g., `colspanx(2, text(hyphenate: false, rotate(-90deg, [*donothyphenatethis*])))`), as also discussed in https://github.com/PgBiel/typst-tablex/issues/59;
another alternative is to use `#place`, e.g. aligning to `center + horizon`: `cellx(place(center + horizon, rotate(-90deg, [*donothyphenatethis*])))`, which probably allows the most control over the in-cell layout, since it simply draws the rotated content without having it occupy any space (letting you define that by yourself, e.g. using `box(width: 1em, height: 2em, place(...))`).

Alternatively, you may attempt to use the solution proposed at https://github.com/typst/typst/issues/528#issuecomment-1494318510 to define a `rotatex` function which produces a rotated element with the appropriate sizes, such that tablex may recognize its size accordingly and avoid visual glitches.

* `tablex` can potentially be slower and/or take longer to compile than the default `table` (especially when the table spans a lot of pages). Please use the latest Typst version to reduce this problem (each version has been bringing further improvements in this sense). Still, we are looking for ways to better optimize the library (see more discussion at https://github.com/PgBiel/typst-tablex/issues/5 - feel free to give some input!). However, re-compilation is usually fine thanks to Typst’s built-in memoization.

* The internals of the library still aren’t very well documented; I plan on adding more info about this eventually.

* Please open a GitHub issue for anything weird you come across (make sure others haven’t reported it first).