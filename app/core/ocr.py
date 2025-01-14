from pytesseract import image_to_string
from PIL import Image

def extract_text(file):
    try:
        image = Image.open(file)
        text = image_to_string(image)
        return text
    except Exception as e:
        raise ValueError("Failed to extract text from image")
