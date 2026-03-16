from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    return "".join([page.extract_text() or "" for page in reader.pages])