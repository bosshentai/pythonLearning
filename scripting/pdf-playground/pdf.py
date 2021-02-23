import PyPDF2

# read binary mode 
with open('./files/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(page.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./changed/tilt.pdf','wb') as newFile:
        writer.write(newFile)
