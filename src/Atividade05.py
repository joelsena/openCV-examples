import cv2

imagem = cv2.imread("saida.jpg")

for y in range(imagem.shape[0]):
    for x in range(imagem.shape[1]):
        imagem[y, x] = (0,(x*y)%256,0)

cv2.imshow("Uhuu", imagem)
cv2.waitKey(0)