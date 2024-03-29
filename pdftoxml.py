from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import XMLConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import BytesIO
import sys

input = BytesIO()
with open(argv[1], 'rb') as f:
    input.write(f.read())

    laparams = LAParams(all_texts=True)
    rsrcmgr = PDFResourceManager()
    for page in PDFPage.get_pages(input):
        output = BytesIO()
        device = XMLConverter(rsrcmgr, output, laparams=laparams)
        interupt = PDFPageInterpreter(rsrcmgr, device)
        interupt.process_page(page)
        
        output.getvalue()
        device.close()
        output.close()
    input.close()
