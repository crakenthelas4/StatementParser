# save as extract_text.py in project root
import pdfplumber

pdf_path = r"C:\Users\hamiz\OneDrive\Desktop\SmartCreditParser\samples\hdfc_sample.pdf"

with pdfplumber.open(pdf_path) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"

print(text[:1000])  # print first 1000 chars for inspection
