import cv2
import numpy as np

imagem = cv2.imread("entrada.jpg")

vermelho = (0,0,255)
verde = (0,255,0)
azul = (255,0,0)

#Nesses métodos a regra vai ser (Coluna, Linha)
cv2.line(imagem, (0,0), (100,200), verde)
cv2.line(imagem, (300,200), (150,150), vermelho, 5)
cv2.rectangle(imagem, (600,20), (820,120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)

(x, y) = (imagem.shape[1] //2, imagem.shape[0] // 2)

for raio in range(0, 175, 15):
    cv2.circle(imagem, (x,y), raio, vermelho,5)



cv2.imshow("Desenhando sobre imagem", imagem)
cv2.waitKey(0)

