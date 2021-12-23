import sys
import pypandoc

filename = sys.argv[1]
output = pypandoc.convert(filename, 'rst')