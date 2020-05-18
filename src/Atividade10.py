import cv2

imagem = cv2.imread("entrada.jpg")
recorte = imagem[100:200, 100:200]

cv2.imshow("Recortado", recorte)
cv2.waitKey(0)
cv2.imwrite("recorte.jpg", recorte)