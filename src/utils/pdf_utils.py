# src/utils/pdf_utils.py
import pdfplumber
from typing import List

def extract_text_from_pdf(path: str) -> str:
    """
    Extracts text from all pages and returns a single string.
    Uses pdfplumber which handles many PDF layouts well.
    """
    text_pages: List[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            # get_text may return None for some pages; safe fallback
            page_text = page.extract_text() or ""
            text_pages.append(page_text)
    full_text = "\n".join(text_pages)
    return full_text

def preview_first_n_lines(text: str, n: int = 40) -> str:
    lines = text.splitlines()
    return "\n".join(lines[:n])
