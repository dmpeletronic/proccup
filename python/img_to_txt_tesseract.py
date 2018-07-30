import sys as sys
import pytesseract as ocr 
from PIL import Image

path=sys.argv[1]
print "File from path ", path

img = Image.open(path)

phrase = ocr.image_to_string(img, lang='por')
print(phrase)


