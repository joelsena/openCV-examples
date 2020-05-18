import cv2

imagem = cv2.imread("entrada.jpg")

#Cria um retangulo azul por toda a largura da imagem
imagem[30:50, : ] = (255,0,0)

#Cria um quadrado vermelho
imagem[100:150, 50:100] = (0,0,255)

#Cria um retangulo amarelo por toda a altura da imagem
imagem[ : , 200:220] = (0, 255, 255)


cv2.imshow("Slicing", imagem)
cv2.waitKey(0)
