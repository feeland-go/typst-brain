---
url: https://typst.app/docs/reference/pdf/
category: pdf
topic: index
---


# PDF (pdf)

PDF files focus on accurately describing documents visually, but also have facilities for annotating their structure. This hybrid approach makes them a good fit for document exchange: They render exactly the same on every device, but also support extraction of a document's content and structure (at least to an extent). Unlike PNG files, PDFs are not bound to a specific resolution. Hence, you can view them at any size without incurring a loss of quality.

## Overview

Reference PDF PDF PDF files focus on accurately describing documents visually, but also have facilities for annotating their structure. This hybrid approach makes them a good fit for document exchange: They render exactly the same on every device, but also support extraction of a document's content and structure (at least to an extent). Unlike PNG files, PDFs are not bound to a specific resolution. Hence, you can view them at any size without incurring a loss of quality. Exporting as PDF Command Line PDF is Typst's default export format. Running the compile or watch subcommand without specifying a format will create a PDF. When exporting to PDF, you have the following configuration options: Which PDF standards Typst should enforce conformance with by specifying --pdf-standard followed by one or multiple comma-separated standards. Valid standards are 1.4, 1.5, 1.6, 1.7, 2.0, a-1b, a-1a, a-2b, a-2u, a-2a, a-3b, a-3u, a-3a, a-4, a-4f, a-4e, and ua-1. By default, Typst outputs PDF-1.7-compliant files. You can disable PDF tagging completely with --no-pdf-tags. By default, Typst will always write Tagged PDF to provide a baseline level of accessibility. Using this flag, you can turn tags off. This will make your file inaccessible and prevent conformance with accessible conformance levels of PDF/A and all parts of PDF/UA. Which pages to export by specifying --pages followed by a comma-separated list of numbers or dash-separated number ranges. Ranges can be half-open. Example: 2,3,7-9,11-. Web App Click the quick download button at the top right to export a PDF with default settings. For further configuration, click "File" > "Export as" > "PDF" or click the downwards-facing arrow next to the quick download button and select "Export as PDF". When exporting to PDF, you have the following configuration options: Which PDF standards Typst should enforce conformance with. By default, Typst outputs PDF-1.7-compliant files. You can choose the PDF version freely between 1.4 and 2.0. ...