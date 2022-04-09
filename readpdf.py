import pdfplumber
with pdfplumber.open("/Users/linux/Downloads/test.pdf") as pdf:
	first_page = pdf.pages[0] #指定页码
	text = first_page.extract_text()#提取文本
	print(text)
