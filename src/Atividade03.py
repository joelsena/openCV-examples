import cv2

imagem = cv2.imread('entrada.jpg')
#imagem.shape[0] representa a altura da imagem
#imagem.shape[1] representa a largura da imagem

for y in range(0, imagem.shape[0], 10):
    for x in range(0, imagem.shape[1], 10):
        imagem[y: y+5, x: x+5] = (255, 0, 0)

cv2.imshow('isso', imagem)
cv2.waitKey(0)