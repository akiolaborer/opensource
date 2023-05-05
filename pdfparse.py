#pdfminer.six

"""
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextLine, LTChar
pdf_file_path = "./20220631mxt_gakushi_000004157.pdf"
for page_layout in extract_pages(pdf_file_path):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                if isinstance(text_line , LTTextLine):
                    for character in text_line:
                        if isinstance(character, LTChar):
                            print(character.fontname)
                            print(character.size)

"""

"""
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
pdf_file_path = "./20220631mxt_gakushi_000004157.pdf"

for page_layout in extract_pages(pdf_file_path):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(element.get_text())

"""

"""
from pdfminer.high_level import extract_pages
pdf_file_path = "./20220631mxt_gakushi_000004157.pdf"
for page_layout in extract_pages(pdf_file_path):
    for element in page_layout:
        print(element)

"""

"""
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

pdf_file_path = "./20220631mxt_gakushi_000004157.pdf"

current_page = 5
last_page = 48
output_string = StringIO()
with open(pdf_file_path, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
    print(output_string.getvalue())
"""

from io import StringIO
from pdfminer.high_level import extract_text, extract_text_to_fp
from pdfminer.layout import LAParams
import time

file="./000648237"
pdf_file_path = file + ".pdf"
text_file_path = file + ".txt"
html_file_path = file + ".html"
xml_file_path = file +  ".xml"

start = time.process_time()
text = extract_text(pdf_file_path)
print(text)

output_string = StringIO()
with open(pdf_file_path, 'rb') as fin:
    #read text
    extract_text_to_fp(fin, output_string)
    #convert to html
    #extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='html', codec=None)
    #convert to xml
    #extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='xml', codec=None)
with open(text_file_path, 'w', encoding="utf-8") as fin:
            fin.write(output_string.getvalue())
end = time.process_time()
print(output_string.getvalue().strip())
print("start, end=", '{0}, {1}'.format(start, end)) 
print("elapsed=", '{0}'.format(end - start))

#pdfminer3x(old) 
"""
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO

pdf_file_path = "20220631mxt_gakushi_000004157"

with open(pdf_file_path , "rb") as pdf_file: #ファイルオブジェクトを受け取り、変数「pdf_file」に代入。
    output = StringIO() #コンソールに出力されたテキストを取得するため、IOクラス「StringIO」使用
    resource_manager = PDFResourceManager()
    "python.pythonPath": "C:\\Users\\coff-\\anaconda3\\envs\\python310\\python.exe",

    laparams = LAParams() #レイアウトの変更がなければデフォルトのままで 
    text_converter = TextConverter(resource_manager, output, laparams=laparams)
    page_interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for i_page in PDFPage.get_pages(pdf_file): #1ベージずづ処理 
        page_interpreter.process_page(i_page)

    output_text = output.getvalue()
    output.close()
    text_converter.close()

print(output_text)
"""

#pdfminer2x(too old)
""""
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument
from pdfminer.pdfparser import PDFPage
from pdfminer.pdfparser import PDFException
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# Open a PDF file.
fp = open("20220631mxt_gakushi_000004157.pdf", 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
document = PDFDocument()
parser.set_document(document) # set document to parser

# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
password="" # pdfを開くときのパスワード
document.set_parser(parser) # set parser to document
document.initialize(password)

# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFException

# Process each page contained in the document.
for page in document.get_pages():
    print(page)
"""