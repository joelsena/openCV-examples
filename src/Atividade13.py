import cv2
import numpy as np

imagem = cv2.imread("entrada.jpg")

#captura largura e altura (0, 1) img.shape[ vai do 0 até 1] =>
(alt, lar) = imagem.shape[:2]
centro = (alt//2, lar//2) # acha o centro

m = cv2.getRotationMatrix2D(centro, 30, 1.0) #30 graus
imgRotacionada = cv2.warpAffine(imagem, m, (lar, alt))

cv2.imshow("Rotacionada", imgRotacionada)
cv2.waitKey(0)