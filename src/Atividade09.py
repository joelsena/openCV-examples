import cv2
import numpy as np

imagem = cv2.imread("entrada.jpg")

fonte= cv2.FONT_HERSHEY_SIMPLEX

#Aparentemente nos métodos do openCV as coordenadas da imagem são dados como (Coluna, Linha) e não (Linha, Coluna) como eh nas matrizes
cv2.putText(imagem, 'DaleeCV', (600,450), fonte, 2, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow("Texto", imagem)
cv2.waitKey(0)