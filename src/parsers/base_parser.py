# src/parsers/base_parser.py
from typing import Dict, Any
from src.utils.pdf_utils import extract_text_from_pdf
from src.utils import regex_patterns as patterns

class BaseParser:
    """
    Base parser class. Each bank parser should inherit and implement parse() method.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.text = extract_text_from_pdf(pdf_path)

    def parse(self) -> Dict[str, Any]:
        """
        Parse the PDF and return a dict with keys of interest.
        Implement in subclass.
        """
        raise NotImplementedError

    # small helpers
    def find_first(self, regex_list, default=None):
        for r in regex_list:
            m = r.search(self.text)
            if m:
                return m.group(1).strip()
        return default
