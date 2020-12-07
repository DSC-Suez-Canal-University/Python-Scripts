import mammoth
from sys import argv


def convert(docfile, htmlfile):
    f = open(docfile, 'rb')
    b = open(htmlfile, 'wb')
    document = mammoth.convert_to_html(f)
    f.close()
    return document
