## Important notice regarding Tablex usage

Summary: Please use built-in Typst tables instead of tablex. Most of tablex’s features were implemented in Typst 0.11.0, see the docs.

However, keep an eye for future tablex updates as there might be some interesting goodies ahead, including CeTZ support!

Details:

A large amount of tablex’s features have successfully been upstreamed by this package’s author to Typst’s built-in `table` and `grid` elements (see the new Tables Guide, at https://typst.app/docs/guides/table-guide/, and the `table` element’s reference, at https://typst.app/docs/reference/model/table/, for more information).

This effort was tracked in the following Typst issue: https://github.com/typst/typst/issues/3001

This means that, starting with Typst 0.11.0, many advanced table features can now be used with Typst grids and tables without tablex! This includes:

* Per-cell customization (through `table.cell(inset: ..., align: ..., fill: ...)[body]`, and `#show table.cell: it => ...` instead of `map-cells`);

* Merging cells (colspans and rowspans, through `table.cell(colspan: 2, rowspan: 2)[body]`);

* Line customization (you can control the `stroke` parameter of `table.cell` to control the lines around it, and you can use `table.hline` and `table.vline` which work similarly to their tablex counterparts - the equivalent of `map-hlines` and `map-vlines` is `table(stroke: (x, y) => (left: ..., right: ..., top: ..., bottom: ...))`);

* Repeatable table headers (through `table.header(... cells ...)`);

* The features above are available within `grid` as well by replacing `table` with `grid` where applicable (e.g. `grid.cell` instead of `table.cell`).

Additionally, built-in Typst tables have support for features which weren’t previously available within tablex, such as repeatable table footers (through `table.footer` and `grid.footer`).

Therefore, for the vast majority of use cases, you will no longer need to use this library.

There are a few observations:

* Tablex will still receive updates over time with extra features. In the next version (tablex 0.1.0), there will be support for CeTZ integration, which will allow you to easily annotate your tables using CeTZ (e.g. draw arrows between cells). If you’re interested in such features, then tablex might still be useful for you in the future!

* Not all tablex features are present in built-in tables, at least yet. Therefore, if you happen to use the features listed below, you might still have to use tablex depending on your use case. It is expected, however, that built-in tables will eventually have support for most of the missing features in future Typst releases. Here’s a non-exhaustive list of them:

Built-in tables do not yet have the ability to expand table lines by some arbitrary length.

* The tablex `fit-spans` option, through which colspans and rowspans don’t cause `auto`-sized columns and/or rows to expand, is not yet supported in built-in tables.

* Built-in repeatable table headers currently always repeat in all pages, whereas you can define in which pages a tablex header should be repeated.

* Regarding sponsorships: Any future sponsorships to the tablex author, @PgBiel, who was also responsible for upstreaming the various tablex features to built-in tables, will go not only towards extended maintenance of tablex, but also towards other general contributions to the Typst ecosystem and his other open-source contributions! More information here: https://github.com/sponsors/PgBiel/

If there any questions, feel free to open a thread in the `Discussions` page of this repository, or ping the author on Discord. Thanks to everyone who supported me throughout tablex’s development and the upstreaming process. I hope you enjoy the new update, and have fun with tables! 😄

And make sure to keep an eye for future tablex updates. 😉