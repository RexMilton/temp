import os
# from docx import Document
from PyPDF2 import PdfReader
# import docx2txt  # Make sure to install docx2txt: pip install docx2txt
extracts=[]
# def read_text_from_docx(file_path):
#     try:
#         doc = Document(file_path)
#         text = ""
#         for para in doc.paragraphs:
#             text += para.text + "\n"
#         return text
#     except Exception as e:
#         print(f"Error reading DOCX file '{file_path}': {e}")
#         return None

def read_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()
            return text
    except Exception as e:
        print(f"Error reading PDF file '{file_path}': {e}")
        return None

# def read_text_from_doc(file_path):
#     try:
#         text = docx2txt.process(file_path)
#         return text
#     except Exception as e:
#         print(f"Error reading DOC file '{file_path}': {e}")
#         return None

def read_text_from_file(file_path):
    # Determine the file type based on the extension
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".pdf":
        return read_text_from_pdf(file_path)
    else:
        print(f"Unsupported file type for '{file_path}'")
        return None


