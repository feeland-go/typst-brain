---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 655
last_audit_date: ""
---

# TYPST NAVIGATOR — Entry Point

> Baca file ini PERTAMA. Gunakan tag-based routing di bawah untuk memuat chunk yang relevan.
> JANGAN baca semua chunks — hanya yang dibutuhkan oleh tags.

## Quick Start
- **Draft standar** → Baca `core/quick-reference.md` saja
- **Butuh fitur spesifik** → Lihat tabel tags di bawah

## Tag-Based Routing

| Tag | Chunk yang Di-load | Trigger |
|-----|-------------------|---------|
| needs-basic | `core/quick-reference.md` | Selalu aktif untuk task .typ |
| needs-table | `chunks/03-table-figure.md` | "buat tabel", "data grid", "table" |
| needs-math | `chunks/04-math-symbols.md` | "equation", "formula", "integral" |
| needs-layout | `chunks/02-layout-page.md` | "multi-column", "grid layout", "sidebar" |
| needs-script | `chunks/01-syntax-scripting.md` | "custom function", "loop", "template logic" |
| needs-data | `chunks/07-data-loading.md` | "dari CSV", "import JSON", "data file" |
| needs-styling | `chunks/05-text-styling.md` | "highlight", "color", "decoration" |
| needs-introspect | `chunks/06-introspection.md` | "counter", "state", "query" |
| needs-package | `packages/_index.md` → `packages/{name}.md` | "gunakan {package}", "@preview/" |
| needs-template | `templates/_index.md` → `templates/{name}.md` | "template {name}" |
| needs-slides | `slides/slides-quickref.md` | "presentasi", "slide", "deck" |
| needs-font | CLI: `typst fonts --font-path $TYPST_BRAIN_HOME/fonts \| grep` | "font X", compile error font |
| needs-docs | CLI: `python3 $TYPST_BRAIN_HOME/scripts/search_docs.py "keyword"` | "dokumentasi", "cara menggunakan fungsi", "referensi resmi" |

## How to use needs-docs
Jika LLM membutuhkan dokumentasi detail tentang fungsi atau topik spesifik yang tidak ada di `core/quick-reference.md`:
1. Jalankan CLI tool: `python3 $TYPST_BRAIN_HOME/scripts/search_docs.py "nama_fungsi"`
2. Skrip akan mengembalikan path ke file markdown spesifik (contoh: `chunks/docs/math/frac.md`).
3. Baca **hanya file yang dikembalikan** tersebut. Jangan menebak path.

## Disambiguation Rules
- **"template"**: ada "@preview/" → needs-template. Ada "function"/"reusable" → needs-script. Ada "slide" → needs-slides. Default: needs-template.
- **Tags hanya aktif jika task = menulis/edit file .typ.** Diskusi umum tidak trigger loading.
- **>4 tags aktif**: sarankan pecah task menjadi sub-tasks.

## Token Budget
Jumlahkan token dari semua active tags. Default max: 3,000 tok (configurable di config.toml).
Jika over budget, prioritaskan: needs-basic > task-specific tag > secondary tags.

## Version Check
Jalankan `typst --version` dan bandingkan dengan typst_min_version/typst_max_version di setiap chunk.
Chunk yang incompatible: jangan load, tandai [OUTDATED].

## Compile Workflow
Semua task berakhir dengan:
```
bash $TYPST_BRAIN_HOME/scripts/compile.sh file.typ
```
Error? Baca stderr → fix → re-compile. Max 3 retry. Setelah itu eskalasi ke user.

## Jika Chunk Tidak Cukup
Lihat "See also" di footer setiap L2 chunk untuk chunk terkait.
