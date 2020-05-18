import cv2
import numpy as np

imagem = cv2.imread("entrada.jpg")

cv2.imshow("Original", imagem)

largura = imagem.shape[1]
altura = imagem.shape[0]
proporcao = float(altura/largura)
largura_nova = 320
altura_nova = int(largura_nova*proporcao)
tamanho_novo = (largura_nova, altura_nova)

imgRe = cv2.resize(imagem, tamanho_novo, interpolation= cv2.INTER_AREA)

cv2.imshow("Redimensionado", imgRe)
cv2.waitKey(0)

#Ou

imgRedimensionada = imagem[::2,::2]
cv2.imshow("Metade", imgRedimensionada)
cv2.waitKey(0)
