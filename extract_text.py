import fitz  # PyMuPDF
import docx2txt

def extract_from_pdf(file_path):
    text = ""
    pdf = fitz.open(file_path)
    for page in pdf:
        text += page.get_text()
    return text

def extract_from_docx(file_path):
    return docx2txt.process(file_path)
