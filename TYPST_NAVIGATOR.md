---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 716
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
| needs-docs | CLI: `python3 $TYPST_BRAIN_HOME/scripts/search_docs.py "keyword"` | "dokumentasi", "fungsi", "tabel", "rumus", "math", "layout", "scripting", "styling" |
| needs-template | `templates/_index.md` → `templates/{name}.md` | "template {name}" |
| needs-package | `packages/_index.md` → `packages/<name>/_index.md` | "gunakan {package}", "@preview/" |
| needs-slides | `slides/slides-quickref.md` | "presentasi", "slide", "deck" |
| needs-font | CLI: `typst fonts --font-path $TYPST_BRAIN_HOME/fonts \| grep` | "font X", compile error font |

## How to use needs-docs & needs-package
Jika LLM membutuhkan dokumentasi detail tentang fungsi bawaan Typst:
1. Jalankan CLI tool: `python3 $TYPST_BRAIN_HOME/scripts/search_docs.py "nama_fungsi"`

Jika LLM membutuhkan dokumentasi spesifik *package* pihak ketiga (misal Touying, Tablex):
1. Buka `packages/<nama_package>/_index.md`. Jika file tidak ada, scrape terlebih dahulu: `python3 $TYPST_BRAIN_HOME/scripts/scrape_package.py <nama_package>`.
2. Baca daftar *Chunks* yang tersedia di dalam *index* tersebut.
3. Gunakan `view_file` **hanya** untuk membuka 1 atau 2 chunk (misal `packages/touying/chunks/04-quick-start.md`) yang paling relevan dengan masalah saat ini. Jangan menebak path.

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
