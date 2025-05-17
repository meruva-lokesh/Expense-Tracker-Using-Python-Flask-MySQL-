import os
import cv2
import pytesseract

# Ensure Tesseract path is set correctly for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """Preprocess image for better OCR results."""
    img = cv2.imread(image_path)
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh

def extract_text(image_path):
    """Extract text from image using pytesseract OCR."""
    image = preprocess_image(image_path)
    if image is None:
        return ""
    temp_path = "temp_for_ocr.png"
    cv2.imwrite(temp_path, image)
    text = pytesseract.image_to_string(temp_path)
    os.remove(temp_path)
    return text

def parse_receipt(text):
    """Parse the OCR'd text to find items, amounts, and date."""
    import re
    lines = text.split('\n')
    items = []
    amount = 0.0
    date = ''
    price_re = re.compile(r'(\d+\.\d{2})')
    date_re = re.compile(r'(\d{2,4}[-/]\d{2}[-/]\d{2,4})')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        price_match = price_re.search(line)
        if price_match:
            items.append(line)
            value = float(price_match.group())
            if value > amount:
                amount = value
        date_match = date_re.search(line)
        if date_match:
            date = date_match.group()
    return {
        "items": items,
        "total": amount,
        "date": date
    }