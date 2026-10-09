# Kasanga Market Dues Revenue Leakage Detector

This repository contains a local government market dues revenue leakage detection project designed for Kasanga Market.

## Included documents
- docs/project-report.md
- docs/project-report.pdf
- docs/software-requirements-specification.md
- docs/software-requirements-specification.pdf
- docs/er-diagram-explanation.md
- docs/er-diagram-explanation.pdf

## Prototype application
- prototype/app.py
- prototype/templates/index.html

## How to run the prototype

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies
   ```bash
   pip install flask
   ```
3. Run the app
   ```bash
   cd prototype
   python app.py
   ```
4. Open in browser
   ```text
   http://localhost:5000
   ```

## Project purpose
The system helps local government officers track trade dues, identify unpaid or underpaid balances, detect duplicate or missing payments, and highlight revenue leakage in Kasanga Market.

## Business value
- Reduces revenue loss
- Improves transparency
- Supports decision making
- Encourages better tax and market collection practice
- Creates a product that can later be offered to local councils
