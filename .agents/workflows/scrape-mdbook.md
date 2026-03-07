---
description: How to scrape and chunk an external mdBook documentation site for Typst Brain
---

# Scrape mdBook Workflow

This workflow delegates the summarization and formatting of large, multi-page mdBook tutorials (like the Polylux or Typst Book) to the LLM. 

## Parameters
- `<package_name>`: The name of the Typst package (e.g., `polylux`).
- `<base_url>`: The root URL of the mdBook (e.g., `https://polylux.dev/book/`).

## Tools Needed
- Python script: `scripts/mdbook_scraper/fetch_book.py`

## Instructions for the LLM

// turbo-all
1. **Fetch Raw Data**: Execute the Python scraper to recursively download all HTML pages of the mdBook and convert them into raw Markdown inside a temporary directory.
   ```bash
   python3 scripts/mdbook_scraper/fetch_book.py <package_name> <base_url>
   ```

2. **Analyze the Raw Dump**:
   Use `list_dir` and `view_file` to read the downloaded markdown files in `/tmp/raw_mdbook_dump/<package_name>`. 
   *Note: mdBooks often have dozens of tiny pages. Your job is to condense them.*

3. **Curate and Chunk**:
   Merge related tiny pages into single, comprehensive markdown chunks. Do NOT just copy the source files 1:1. 
   Create a maximum of 10-15 Markdown chunks inside `packages/<package_name>/chunks/`. Name them sequentially (e.g., `01-getting-started.md`, `02-advanced-usage.md`).

4. **Generate the Index**:
   Create the `packages/<package_name>/_index.md` entry point. It MUST contain:
   - Package Name and Date
   - Import statement (`#import "@preview/<package_name>:<version>": *` - guess version if not found)
   - The original book URL
   - A `## Documentation Chunks` section listing all the chunks you just created.

5. **Clean Up**:
   Remove the temporary dump.
   ```bash
   rm -rf /tmp/raw_mdbook_dump/<package_name>
   ```
