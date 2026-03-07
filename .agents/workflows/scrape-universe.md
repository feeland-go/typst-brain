---
description: How to scrape and chunk standard Typst Universe packages
---

# Scrape Typst Universe Package Workflow

This workflow uses the LLM to intelligently split and index standard Typst Universe packages, rather than relying on brittle Python regex `##` splitting.

## Parameters
- `<package_name>`: The name of the Typst package on the universe (e.g., `touying`, `tablex`).

## Tools Needed
- Python script: `scripts/universe_scraper/fetch_package.py`

## Instructions for the LLM

// turbo-all
1. **Fetch Raw Data**: Execute the Python scraper to download the package's README, auto-install it to the local cache, and extract basic metadata (version, github link).
   ```bash
   python3 scripts/universe_scraper/fetch_package.py <package_name>
   ```

2. **Analyze the Raw Content**:
   The Python script will dump the raw Markdown README and metadata into `/tmp/raw_universe_dump/<package_name>/`. Use `view_file` to read the `README.md` and `metadata.json`.

3. **Curate and Chunk (CRITICAL)**:
   Do NOT just split blindly by `##`. Read the README and logically separate it into distinct files. 
   Create meaningful markdown chunks inside `packages/<package_name>/chunks/`. Name them sequentially (e.g., `01-overview.md`, `02-api-reference.md`).
   If the README is very short, 1 or 2 chunks is perfectly fine.

4. **Generate the Index**:
   Create the `packages/<package_name>/_index.md` entry point. It MUST contain:
   - Package Name, Version, and Date (use `metadata.json`)
   - Import statement (`#import "@preview/<package_name>:<version>": *`)
   - The Official Typst Universe URL and Repository URL (from `metadata.json`)
   - A `## Documentation Chunks` section listing all the chunks you just created.

5. **Clean Up**:
   Remove the temporary dump.
   ```bash
   rm -rf /tmp/raw_universe_dump/<package_name>
   ```
