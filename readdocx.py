from docx import Document
path = r"/Users/linux/Downloads/test.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)
