import os
from PyPDF2 import PdfFileWriter, PdfFileReader

#f will hold the filenames of all the PDF files in the directory 'pdffiles'.
f = []
for root, dirs, files in os.walk("pdffiles"):
    for filename in files:
        f.append(filename)

outputfile = PdfFileWriter()

"""
the outer for loop is used to access each and every pdf file that is in the directry using its name. 
The inner for loop saved all pages except the last one of all pdfs, to a new object, which is then 
saved as a new pdf file.
"""

for fname in f:
    inputfile = PdfFileReader("pdffiles/"+fname, 'rb')

    for num in range(inputfile.numPages - 1):
        page = inputfile.getPage(num)
        outputfile.addPage(page)
    
with open('mergedfile.pdf', 'wb') as outpdf:
    outputfile.write(outpdf)
