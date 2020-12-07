#!/usr/bin/env python

import mammoth
from sys import argv


def convert(docfile, htmlfile):
    f = open(docfile, 'rb')
    b = open(htmlfile, 'wb')
    document = mammoth.convert_to_html(f)
    b.write(document.value.encode('utf8'))
    f.close()
    b.close()


doc = argv[1]
html = argv[2]
convert(doc, html)

