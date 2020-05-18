import cv2

imagem = cv2.imread("entrada.jpg")

#Redimensionando
imre = imagem[::2, ::2]
cv2.imshow("Original", imre)

flip_horizontal = imre[::-1,:] #Comando equivalente abaixo
#flip_horizontal = cv2.flip(img, 1)

cv2.imshow("Flip Horizontal", flip_horizontal)

flip_vertical = imre[:, ::-1]
#flip_vertical = cv2.flip(imagem, 0)

cv2.imshow("Flip Vertical", flip_vertical)

flip_hv = flip_horizontal[:, ::-1]
#flip_hv = cv2.flip(flip_horizontal, 0)

cv2.imshow("Flip vertical do horizontal", flip_hv)

cv2.waitKey(0)


