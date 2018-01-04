import PyPDF2

pdfFileObj = open('annual-report-2016.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

text = []
for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(0)
    text.append(pageObj.extractText())