import cv2

#Carrega arquivo e converte para tons de cinza
i = cv2.imread('rostos2.jpg')
iPB = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)

#Criação do detector de faces
df = cv2.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

#Executa a detecção
faces = df.detectMultiScale(image=iPB, scaleFactor=1.05, minNeighbors=3, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)

#Desenha retangulos amarelos na iamgem original (colorida)
for (x, y, w, h) in faces:
 cv2.rectangle(i, (x, y), (x + w, y + h), (0, 255, 255), 3)

#Exibe imagem. Título da janela exibe número de faces
cv2.imshow(str(len(faces))+' face(s) encontrada(s).', i)
cv2.waitKey(0)


