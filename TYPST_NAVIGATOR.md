---
typst_min_version: "0.12.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 1013
last_audit_date: ""
---

# TYPST NAVIGATOR — Entry Point

> Baca file ini PERTAMA. Gunakan tag-based routing di bawah untuk memuat chunk yang relevan.
> JANGAN baca semua chunks — hanya yang dibutuhkan oleh tags.

## Contextual Scoping (READ THIS FIRST)
Periksa di direktori mana Anda (LLM) sedang beroperasi:
- **JIKA ANDA BERADA DI LUAR REPO `typst-brain` (e.g. `~/Documents/MyProject`)**: File ini murni berfungsi sebagai **Read-Only Navigator**. Anda HANYA diizinkan untuk membaca `chunks/`, `fonts/`, `memory/`, dan `packages/`. JANGAN PERNAH mencoba menjalankan *script scraping* atau memodifikasi isi Brain dari luar.
- **JIKA ANDA BERADA DI DALAM REPO `typst-brain`**: Anda bertindak sebagai **Brain Administrator**. Anda diizinkan mengeksekusi `.agents/workflows/` untuk menambah package baru atau memperbarui dokumentasi inti Typst.

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
1. Buka `packages/<nama_package>/_index.md`.
2. Jika file tidak ada:
   - **Jika Anda di luar `typst-brain`**: Laporkan ke *user* bahwa *package* belum tersedia di Brain dan minta *user* untuk membuka jendela _chat_ baru di dalam folder `typst-brain` untuk melakukan _scraping_. Jangan *scrape* dari luar.
   - **Jika Anda di dalam `typst-brain`**: Anda **HARUS** melakukan *scraping* terlebih dahulu menggunakan panduan Agentic Workflow:
   - Baca `.agents/workflows/scrape-universe.md` untuk package Typst Universe standar.
   - Baca `.agents/workflows/scrape-github.md` jika Anda diberi link GitHub.
   - Baca `.agents/workflows/scrape-mdbook.md` jika Anda diberi link manual berformat buku.
3. Setelah package di-_scrape_, baca daftar *Chunks* yang tersedia di dalam *index*.
4. Gunakan `view_file` **hanya** untuk membuka 1 atau 2 chunk (misal `packages/touying/chunks/02-api-reference.md`) yang paling relevan dengan masalah saat ini. Jangan menebak path.

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
