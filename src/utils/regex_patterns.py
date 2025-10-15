# src/utils/regex_patterns.py
# central place for patterns (add/adjust as you test real statements)
import regex as re

# Common patterns (loose and forgiving)
CARD_LAST4 = re.compile(r'(?:Card(?:\s+No| Number| #)?\s*(?:Ending)?\s*[:\-]?\s*)(\d{4})', re.IGNORECASE)
CARD_LAST4_ALT = re.compile(r'(\d{4})\s*\)\s*$', re.MULTILINE)

NAME_PATTERN = re.compile(r'(?:Cardholder|Card Holder|Customer|Account Name|Name)\s*[:\-]?\s*([A-Z][A-Za-z \.]{2,60})', re.IGNORECASE)
TOTAL_DUE = re.compile(r'(?:Total\s+Due|Amount\s+Due|Minimum\s+Due|Amount\s+Payable)\s*[:\-]?\s*₹?\s*([0-9,]+\.\d{2}|[0-9,]+)', re.IGNORECASE)
DUE_DATE = re.compile(r'(?:Due Date|Payment Due Date|Last Date for Payment)\s*[:\-]?\s*([A-Za-z0-9,\s\-\/]+)', re.IGNORECASE)
TOTAL_SPENT = re.compile(r'(?:Total\s+Spent|Total\s+Purchases|Total\s+Amount)\s*[:\-]?\s*₹?\s*([0-9,]+\.\d{2}|[0-9,]+)', re.IGNORECASE)

# Transaction table detection (very heuristic; used later for advanced extraction)
TRAN_TABLE_HEADER = re.compile(r'(Date|Transaction Date).*(Description|Merchant).*(Amount)', re.IGNORECASE | re.DOTALL)
