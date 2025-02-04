from PyPDF2 import PdfReader
import os

def extract_text_from_pdfs(pdf_dir):
    all_text = ""
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, file)
            reader = PdfReader(pdf_path)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            all_text += text + "\n\n"
    return all_text

# Extract text from PDFs in "data" directory
data_text = extract_text_from_pdfs("data")

# Save extracted text
with open("corpus.txt", "w", encoding="utf-8") as f:
    f.write(data_text)

print("Text extracted and saved in corpus.txt")
