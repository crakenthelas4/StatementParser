# Credit Card Statement Parser

This project extracts and summarizes important financial details from PDF-based credit card statements.  
It supports multiple credit card issuers (HDFC, ICICI, SBI, Axis, Citi) and outputs structured data in JSON or CSV format.

## Features
- Extracts 5 key data points:
  1. Cardholder Name
  2. Last 4 digits of the card
  3. Billing Period
  4. Total Amount Due
  5. Payment Due Date
- Handles varying PDF layouts and formats.
- Outputs results to JSON or CSV.
- Simple Streamlit interface for quick visualization.

## Tech Stack
- **Python 3.9+**
- **Libraries:** `pdfplumber`, `pandas`, `streamlit`, `re`
- **File Output:** JSON & CSV

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/Credit-Card-Statement-Parser.git
cd Credit-Card-Statement-Parser
