
import pdfplumber
import os


pdf_directory = r'C:\Users\Kyle\Desktop\python_work\Epic\check'
files = []

for filename in os.listdir(pdf_directory):
	if filename.endswith(".pdf"):
		files.append(os.path.join(pdf_directory, filename))
print(files)

for file in files:
	with pdfplumber.open(file) as pdf:
		page = pdf.pages[0]
		text = page.extract_text()
		name = text.split("\n")[2]
		pdf.close()
	os.rename(f"{file}", fr"{pdf_directory}\{name}.pdf")






#
#
#
