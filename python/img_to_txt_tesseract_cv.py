import sys as sys
import pytesseract as ocr 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

from PIL import Image


def showimg(img, texto):
	cv.imshow(texto, img)
	#cv.waitKey(0)
   #plt.imshow(img),plt.title(texto)
   #plt.xticks([]), plt.yticks([])
   #plt.show()

def img_to_text(img):
  # Write the image to disk
  filename = "{}.png".format(os.getpid())
  cv.imwrite(filename, img)
  phrase = ocr.image_to_string(Image.open(filename), lang='por')
  os.remove(filename)	
  print(phrase)
  return phrase



path=sys.argv[1]
print "File from path ", path

# Preparando a imagem
img = cv.imread(path)#Image.open(path).convert('RGB')
showimg(img, "original")
img_to_text(img)


# atribuicao em escala de cinza
grayscale = cv.cvtColor(img, cv.COLOR_RGB2GRAY) 
showimg(grayscale, "gray")
img_to_text(grayscale)

#Suavizando
filtro = cv.medianBlur(grayscale,3)
showimg(filtro, "filtro")
img_to_text(filtro)

# aplicacao da truncagem binaria para a intensidade
# pixels de intensidade de cor abaixo de 127 serao convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serao convertidos para 255 (BRANCO)
# A atrubicao do THRESH_OTSU incrementa uma analise inteligente dos nivels de truncagem
ret, thresh = cv.threshold(filtro, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
showimg(thresh, "binaria")

cv.waitKey(0)
cv.destroyAllWindows()