---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
last_audit_date: ""
---

# TYPST NAVIGATOR

> Baca PERTAMA. Tag-based routing. JANGAN baca semua.

## Quick Start
- **Draft** → `core/quick-reference.md`
- **Fitur** → Lihat tabel

## Tag-Based Routing

| Tag | Chunk | Trigger |
|-----|-------|---------|
| needs-basic | `core/quick-reference.md` | Selalu aktif |
| needs-table | `chunks/03-table-figure.md` | "tabel", "grid" |
| needs-math | `chunks/04-math-symbols.md` | "equation" |
| needs-layout | `chunks/02-layout-page.md` | "column", "grid" |
| needs-script | `chunks/01-syntax-scripting.md` | "function" |
| needs-data | `chunks/07-data-loading.md` | "CSV", "JSON" |
| needs-styling | `chunks/05-text-styling.md` | "color" |
| needs-introspect | `chunks/06-introspection.md` | "counter" |
| needs-package | `packages/_index.md` | "@preview/" |
| needs-template | `templates/_index.md` | "template" |
| needs-slides | `slides/slides-quickref.md` | "slide" |
| needs-font | CLI: `typst fonts` | "font" |

## Disambiguation
- "template": @preview/ → needs-template. function → needs-script.
- Tags aktif hanya untuk task .typ.
- >4 tags → pecah sub-tasks.

## Token Budget
Max 3,000 tok. Prioritas: needs-basic > task-specific.

## Version Check
`typst --version` vs chunk. Incompatible → [OUTDATED].

## Compile Workflow
```
bash $TYPST_BRAIN_HOME/scripts/compile.sh file.typ
```
Error → fix → re-compile. Max 3 retry.

## Chunk Tidak Cukup
Lihat "See also" di footer L2 chunk.
