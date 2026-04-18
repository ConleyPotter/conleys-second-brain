---
type: tool-analysis
domain: general
tags: [second-brain, tools, pdf, markdown, ingestion, python, open-source]
created: 2026-04-18
updated: 2026-04-18
sources:
  - "microsoftmarkitdown Python tool for converting PDF files and office documents to Markdown.md"
---

# MarkItDown

**Related:** [[llm-wiki-pattern]], [[second-brain-article]], [[tech-stack]]

*Source: [microsoft/markitdown](https://github.com/microsoft/markitdown) GitHub README — Microsoft open-source project*

---

## What It Is

MarkItDown is a lightweight Python utility from Microsoft for converting documents and files into Markdown, specifically for LLM pipelines. It is comparable to textract but with a focus on preserving document structure (headings, lists, tables, links) as Markdown rather than plain text. Output is LLM-optimized, not human-display-optimized.

**Why Markdown for LLMs:** Mainstream LLMs are trained on massive volumes of Markdown text and "speak" it natively. Markdown is near-plain-text but preserves structure, and is highly token-efficient. This makes it the right target format for any document being fed into an LLM pipeline.

---

## How Conley Uses It

MarkItDown is the **ingest bridge** for this second brain: it converts PDFs, Word docs, and other office formats into Markdown before they land in `raw-sources/`. The resumes ingested on 2026-04-18 are an example — originally PDF or DOCX files, converted to `.md` via markitdown before being dropped into the vault for LLM processing.

This solves the otherwise-manual step of getting non-text documents into the wiki ingest workflow. See [[llm-wiki-pattern]] for the three-layer architecture this feeds into.

---

## Supported Formats

- PDF
- Word (DOCX)
- PowerPoint (PPTX)
- Excel (XLSX, XLS)
- Images — EXIF metadata extraction + optional OCR via LLM vision
- Audio — EXIF metadata + speech-to-text transcription
- HTML
- Text-based formats: CSV, JSON, XML
- ZIP (iterates over contents)
- YouTube URLs (fetches transcription)
- EPubs

---

## Installation

```bash
pip install 'markitdown[all]'
```

Or install specific format support only:

```bash
pip install 'markitdown[pdf,docx,pptx]'
```

Requires Python 3.10+.

---

## Basic Usage

**CLI:**
```bash
markitdown path-to-file.pdf > output.md
markitdown path-to-file.pdf -o output.md
```

**Python API:**
```python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

---

## Extensions and Integrations

### MCP Server (markitdown-mcp)
A Model Context Protocol server is available, enabling direct integration with Claude Desktop and other MCP-compatible LLM applications. Converts documents directly within the Claude context window without a separate CLI step.

### markitdown-ocr Plugin
Adds OCR support for embedded images in PDF, DOCX, PPTX, and XLSX files. Uses the same `llm_client` / `llm_model` pattern as image description — pass an OpenAI-compatible client and model to extract text from images via LLM vision. No new binary dependencies required.

```python
from markitdown import MarkItDown
from openai import OpenAI

md = MarkItDown(
    enable_plugins=True,
    llm_client=OpenAI(),
    llm_model="gpt-4o",
)
result = md.convert("scan.pdf")
```

### Azure Document Intelligence
Enterprise-grade OCR and layout analysis via Azure's Document Intelligence service:
```bash
markitdown file.pdf -o output.md -d -e "<document_intelligence_endpoint>"
```

---

## Notable Breaking Changes (0.0.1 → 0.1.0)

- Optional feature groups introduced — install `[all]` for backward-compatible behavior
- `convert_stream()` now requires a binary file-like object (previously accepted text streams)
- `DocumentConverter` interface changed from file paths to file-like streams

---

## Relationship to Other Tools

- **vs. textract:** textract extracts raw text; markitdown preserves document structure as Markdown. Better for LLM pipelines where headings, tables, and lists carry semantic meaning.
- **vs. manual copy-paste:** Eliminates the conversion step entirely — any PDF in the workflow becomes a `.md` file automatically.
- **vs. Adobe/Acrobat PDF export:** Those tools optimize for human reading; markitdown optimizes for LLM token efficiency and structural fidelity.

---

## Limitations

- Output is LLM-optimized, not human-display-optimized. Complex layouts (multi-column PDFs, scanned documents without OCR) may have reduced fidelity.
- OCR on scanned documents requires the `markitdown-ocr` plugin and an LLM API key.
- Audio transcription quality depends on the underlying ASR model.
