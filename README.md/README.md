# SmartCreditParser

SmartCreditParser is a CLI tool that extracts key fields from credit-card statement PDFs (multi-bank).  
This repo contains a modular parser architecture so you can add support for more banks easily.

## Features
- Extracts 5 key fields per statement: `cardholder_name`, `card_last_4`, `total_due`, `due_date`, `total_spent`
- Bank autodetection (keyword-based)
- Saves parsed output as JSON (and optional CSV for transactions)
- Modular parser classes — add a parser per bank in `src/parsers/`

## Project structure
SmartCreditParser/
├── src/
│ ├── parsers/
│ │ ├── base_parser.py
│ │ ├── hdfc_parser.py
│ │ └── <other_parsers>.py
│ ├── utils/
│ │ ├── pdf_utils.py
│ │ └── regex_patterns.py
│ └── main.py
├── samples/
│ ├── hdfc_sample.pdf
│ └── ...
├── output/
├── README.md
└── requirements.txt


---

# 2 — Line-by-line explanation + exact commands

### A — Create the project & README
1. Create folder and files (example on Windows/macOS/Linux terminal):
```bash
mkdir SmartCreditParser
cd SmartCreditParser
# create README.md and other folders
mkdir -p src/parsers src/utils samples output
touch README.md requirements.txt

# SmartCreditParser

## Overview
SmartCreditParser extracts key information from credit card statements in PDF format for multiple banks (HDFC, SBI, ICICI, Axis, Kotak).

## Features
- Extracts cardholder name, card last 4 digits, total spent, total due, due date, and transactions.
- Multi-bank support with easy-to-add parsers.
- Outputs clean JSON for integration with other applications.

## Installation
```bash
git clone <repo-url>
cd SmartCreditParser
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

 

# 3 - license 

---

## 3️⃣ Optional: Add **extract_text.py** for debugging
```python
# extract_text.py
from src.utils.pdf_utils import extract_text_from_pdf

pdf_path = "samples/hdfc_sample.pdf"
text = extract_text_from_pdf(pdf_path)
print(text)


