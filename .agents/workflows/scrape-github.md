---
description: How to scrape and chunk a raw GitHub repository format for Typst Brain
---

# Scrape GitHub Repository Workflow

This workflow replaces the legacy deterministic Python HTML scrapers with an Agentic LLM-curated approach, as requested by the user. The goal is to fetch raw repository data and then use the LLM's intelligence to map, chunk, and index the documentation.

## Parameters
- `<package_name>`: The name of the Typst package (e.g., `touying`).
- `<version>`: The version of the package (e.g., `0.1.0` or `main`).
- `<github_url>`: The URL of the GitHub repository (e.g., `https://github.com/touying-typ/touying`).

## Tools Needed
- Python script: `scripts/github_scraper/pull_repo.py`

## Instructions for the LLM

// turbo-all
1. **Fetch Raw Data**: Execute the Python scraper to download the raw repository into a temporary directory.
   ```bash
   python3 scripts/github_scraper/pull_repo.py <github_url> /tmp/raw_github_dump/<package_name>
   ```

2. **Analyze the Repository Structure**:
   Use the `list_dir` and `view_file` tools to explore the downloaded repository in `/tmp/raw_github_dump/<package_name>`. Look specifically for:
   - `README.md`
   - Any `docs/` or `examples/` folders
   - Interesting `.typ` files that demonstrate usage.

3. **Curate and Chunk**:
   Instead of using regex, you (the LLM) are responsible for splitting and summarizing the documentation. Create meaningful markdown chunks (maximum 10 chunks to save tokens) inside `packages/<package_name>/chunks/`. Name them sequentially (e.g., `01-overview.md`, `02-configuration.md`).

4. **Generate the Index**:
   Create the `packages/<package_name>/_index.md` entry point. It MUST contain:
   - Package Name, Version, and Date
   - Import statement (`#import "@preview/<package_name>:<version>": *`)
   - The original GitHub Repository URL
   - A `## Documentation Chunks` section listing all the chunks you just created.

5. **Clean Up**:
   Remove the temporary dump.
   ```bash
   rm -rf /tmp/raw_github_dump/<package_name>
   ```
