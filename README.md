# PDF Generation POC Repository

## Overview
This repository serves as a Proof of Concept (POC) for PDF generation. It demonstrates and tests the functionality of several key packages that will be utilized in the revamped PDF generation project.

## Tech Stack
- **Languages**: Python, HTML, CSS, Markdown  
- **Packages**:
  - `durable-rules`
  - `Jinja2`
  - `weasyprint`
  - `markdown`

## Explanation of Components
- **Jinja2**: Acts as a template engine to dynamically inject parameters into the HTML templates.
- **markdown**: Converts Markdown-formatted content into HTML.
- **weasyprint**: Transforms the generated HTML content into a PDF document.
- **durable-rules**: Defines a ruleset to dynamically generate parameters for the data used in the templates.

## Usage
For more details about the implementation and usage, please refer to the `main.py` file.
