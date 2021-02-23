import PyPDF2
import sys


inputs = sys.argv[1:]

def pdfCombiner(pdfList):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfList:
        #print(pdf)
        merger.append(pdf)
    merger.write('./changed/super.pdf')


pdfCombiner(inputs)