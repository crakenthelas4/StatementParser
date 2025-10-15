# src/parsers/__init__.py
from .hdfc_parser import HDFCParser
from .sbi_parser import SBIParser
from .icici_parser import ICICIParser
from .axis_parser import AxisParser
from .citi_parser import CitiParser

# mapping for detection (used in main)
PARSERS = {
     "HDFC": HDFCParser,
    "SBI": SBIParser,
    "ICICI": ICICIParser,
    "Axis": AxisParser,
    "Citi": CitiParser
}
