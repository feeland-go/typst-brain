# Typst Brain 🧠

A centralized, LLM-optimized knowledge repository for Typst. This project is built specifically to allow Artificial Intelligence to write, compile, and debug complex Typst documents using a consistent source of truth.

## Features

- **Agentic Data Scrapers:** Autonomous LLM-curated workflows to ingest standard Typst Universe packages, mdBook tutorials, and raw GitHub repositories into highly optimized markdown chunks.
- **Navigator Protocol:** The `TYPST_NAVIGATOR.md` acts as a routing table. Drop this file into any other generic Typst project, and the AI will know exactly how to fetch Typst functions and package documentations from this brain.
- **Pre-Processed Knowledge:** Over 150+ core Typst library functions statically extracted and ready for instant RAG (Retrieval-Augmented Generation).

## Directory Structure

```text
typst-brain/
├── .agents/workflows/   # LLM Instructions for the Agentic Scraper Workflows
├── TYPST_NAVIGATOR.md   # The Universal Routing Protocol (Symlink this to your projects)
├── chunks/docs/         # The official Typst Reference Manual, broken into precise functions
├── core/                # Core Typst abstractions (patterns, snippets, quick-reference)
├── packages/            # LLM-curated markdown documentations of 3rd-party packages
└── scripts/             # Python backend tools (fetchers, CLI searches, compilers)
```

## How to use the Scrapers (Agentic Data Ingestion)

Typst Brain does not rely on fragile Python Regex. Instead, it uses **Agentic Workflows**. If you want the AI to ingest a new package, tell the AI to execute one of the following workflows:

1. **For Typst Universe Packages:**
   `Read .agents/workflows/scrape-universe.md to scrape package <name>`
2. **For GitHub Hosted Packages:**
   `Read .agents/workflows/scrape-github.md to scrape <repo_url>`
3. **For mdBook Manuals:**
   `Read .agents/workflows/scrape-mdbook.md to scrape book at <url>`

## How to use with other Projects

To grant an LLM in another directory access to the Typst Brain:
1. Ensure the `$TYPST_BRAIN_HOME` environment variable points to this repository.
2. Copy or symlink `TYPST_NAVIGATOR.md` into the root of your target project.
3. The AI will automatically read `TYPST_NAVIGATOR.md` and know how to use the tools inside this repository.

## Progress Tracking
See `PROGRESS.md` for the historical development and milestone logs.
