# importing required modules
import PyPDF2
import pyperclip

import os

# specify the folder path
folder_path = 'Ready for Authentication'

# loop through all files in the folder
for filename in os.listdir(folder_path):
	try:
		if os.path.isfile(os.path.join(folder_path, filename)):
			pdfFileObj = open(filename, 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
			print(pdfReader.numPages)
				
			pageObj = pdfReader.getPage(0)
		#	pyperclip.copy(pageObj)
			print(pageObj.extractText())
			ok = input("is it ok?")
			pdfFileObj.close()

	except FileNotFoundError:
		pass