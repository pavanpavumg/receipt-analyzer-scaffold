import pytesseract
import re
from pdf2image import convert_from_path
import cv2
from dateutil import parser as dateparser

def extract_text_from_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return pytesseract.image_to_string(thresh)

def parse_text(text):
    vendor = re.search(r'(?i)(?:vendor|store):?\s*(.+)', text)
    amount = re.search(r'\$?\s?([\d,]+\.?\d*)', text)  # Allow for missing $ sign
    date_match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4})', text)

    parsed_date = "1970-01-01"
    if date_match:
        try:
            parsed_date = dateparser.parse(date_match.group(1)).date().isoformat()
        except Exception:
            pass

    return {
        'vendor': vendor.group(1).strip() if vendor else "Unknown",
        'amount': float(amount.group(1).replace(",", "")) if amount else 0.0,
        'date': parsed_date
    }