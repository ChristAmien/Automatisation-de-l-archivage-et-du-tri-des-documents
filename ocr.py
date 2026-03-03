import pytesseract
import PyPDF2
from PIL import Image
import os

# Configuration de Tesseract
try:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
except:
    pass  # Tesseract peut être dans PATH

def extract_text_from_image(image_path):
    """Extrait le texte d'une image"""
    try:
        image = Image.open(image_path)
        texte = pytesseract.image_to_string(image, lang="fra")
        return texte.strip() if texte else ""
    except Exception as e:
        print(f"Erreur OCR image: {e}")
        return ""

def extract_text_from_pdf(pdf_path):
    """Extrait le texte d'un PDF"""
    try:
        texte = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                texte += page.extract_text() + "\n"
        return texte.strip()
    except Exception as e:
        print(f"Erreur PDF: {e}")
        return ""

def extract_text(filepath):
    """Extrait le texte d'un fichier (image ou PDF)"""
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext in ['.pdf']:
        return extract_text_from_pdf(filepath)
    elif ext in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']:
        return extract_text_from_image(filepath)
    else:
        return ""