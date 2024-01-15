#pdfminer.six
from io import StringIO
from pdfminer.high_level import extract_text, extract_text_to_fp
from pdfminer.layout import LAParams
import sys
import time

file = argv[1]
pdf_file_path = argv[1]

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
