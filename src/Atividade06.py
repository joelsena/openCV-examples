import cv2

imagem = cv2.imread("entrada.jpg")

for y in range(0,imagem.shape[0], 10):
    for x in range(0, imagem.shape[1],10):
        imagem[y: y+3, x: x+3] = (0,255,255)

cv2.imshow("Pontinhos", imagem)
cv2.waitKey(0)