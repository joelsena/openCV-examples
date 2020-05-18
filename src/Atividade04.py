import cv2

imagem = cv2.imread('entrada.jpg')

for y in range(imagem.shape[0]):
    for x in range(imagem.shape[1]):
        imagem[y, x] = (x%256, y%256, x%256)

cv2.imshow('Imagem alterada de acordo com as suas linhas e colunas', imagem)
cv2.waitKey(0)