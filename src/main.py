# src/main.py
import sys
import os
import json
from src.utils.pdf_utils import extract_text_from_pdf
from src.parsers import PARSERS
from src.parsers.hdfc_parser import HDFCParser

# -----------------------------
# Improved bank detection heuristics
# -----------------------------
def detect_bank(text: str):
    text_lower = text.lower()
    scores = {
        "hdfc": 0,
        "sbi": 0,
        "icici": 0,
        "axis": 0,
        "citi": 0
    }

    # HDFC keywords
    for kw in ["hdfc bank", "hdfc credit card", "hdfc"]:
        if kw in text_lower:
            scores["hdfc"] += 1

    # SBI keywords
    for kw in ["state bank of india", "sbi credit card", "sbi card"]:
        if kw in text_lower:
            scores["sbi"] += 1

    # ICICI keywords
    for kw in ["icici bank", "icici credit card", "icici"]:
        if kw in text_lower:
            scores["icici"] += 1

    # Axis keywords
    for kw in ["axis bank", "axis credit card", "axis"]:
        if kw in text_lower:
            scores["axis"] += 1

    # Citi keywords
    for kw in ["citibank", "citi credit card", "citi"]:
        if kw in text_lower:
            scores["citi"] += 1

    # Pick bank with max score
    bank_key = max(scores, key=lambda k: scores[k])
    if scores[bank_key] == 0:
        return None
    return bank_key

def get_parser_for(bank_key: str):
    cls = PARSERS.get(bank_key)
    return cls

def detect_bank_with_logo(text: str):
    first_page = text[:300].lower()
    bank = detect_bank(first_page)
    return bank


# -----------------------------
# Main parsing function
# -----------------------------
def parse_file(path: str, output_dir: str = "output"):
    # Extract text from PDF
    text = extract_text_from_pdf(path)

    # Detect bank
    bank_key = detect_bank(text)
    print(f"[INFO] detected bank: {bank_key}")

    # Choose parser class
    if not bank_key:
        print("[WARN] Bank not detected automatically. Using HDFC parser as default.")
        parser_cls = HDFCParser
    else:
        parser_cls = get_parser_for(bank_key)
        if parser_cls is None:
            print(f"[WARN] Parser class for {bank_key} not found. Using HDFC parser as fallback.")
            parser_cls = HDFCParser

    # Instantiate parser
    parser = parser_cls(path)

    # Parse PDF
    try:
        result = parser.parse()
    except NotImplementedError as e:
        print("[ERROR]", e)
        return None

    # Save JSON output
    os.makedirs(output_dir, exist_ok=True)
    base = os.path.basename(path)
    json_name = os.path.splitext(base)[0] + ".json"
    out_path = os.path.join(output_dir, json_name)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[OK] Parsed output saved to {out_path}")
    return out_path

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <path-to-pdf> [output-dir]")
        sys.exit(1)
    pdf_path = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else "output"
    parse_file(pdf_path, outdir)
