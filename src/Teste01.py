import cv2;

imagem = cv2.imread('entrada.jpg')

print('largura em pixels: ', end='')
print(imagem.shape[1]) #Largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #Altura da imagem
print('Qtd de canais: ', end='')
print(imagem.shape[2])

#Mostra a imagem e faz esperar pressionar uma tecla respectivamente
cv2.imshow("Teste", imagem)
cv2.waitKey(0)

#Salva a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)