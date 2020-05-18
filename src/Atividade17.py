import cv2
import numpy as np

imgre = cv2.imread('entrada.jpg')
img = imgre[::2,::2]

(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
cv2.waitKey(0)
cv2.imwrite("ponte.jpg",img)
