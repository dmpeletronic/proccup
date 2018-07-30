import sys as sys
import pytesseract as ocr 
import cv2 as cv
import numpy as np

from PIL import Image


path=sys.argv[1]
print "File from path ", path

# Preparando a imagem
img = Image.open(path).convert('RGB')

# Convertendo em array editavel numpy [x, y, CANALS]
npimagem = np.asarray(img).astype(np.uint8)  

# diminuicao dos ruidos antes da binarizacao
npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

# atribuicao em escala de cinza
im = cv.cvtColor(npimagem, cv.COLOR_RGB2GRAY) 

# aplicacao da truncagem binaria para a intensidade
# pixels de intensidade de cor abaixo de 127 serao convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serao convertidos para 255 (BRANCO)
# A atrubicao do THRESH_OTSU incrementa uma analise inteligente dos nivels de truncagem
ret, thresh = cv.threshold(im, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

# reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
binimg= Image.fromarray(thresh) 

phrase = ocr.image_to_string(binimg, lang='por')

print(phrase)


