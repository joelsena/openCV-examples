import cv2
import numpy as np
import mahotas

def escrever(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)

imgCol = cv2.imread("dados2.jpg")
#imgCol = imgCol[::2, ::2]
imgCin = cv2.cvtColor(imgCol, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(imgCin, (7, 7), 0)

T = mahotas.thresholding.otsu(suave)
bin = suave.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(suave)

bordas = cv2.Canny(bin, 70, 150)

(objetos, lx) = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

escrever(imgCol, "Original", (255, 255, 255))
escrever(imgCin, "Cinza")
escrever(suave, "Suave")
escrever(bordas, "Canny")

imagens = np.vstack((
    np.hstack([imgCin, suave]),
    np.hstack([bin, bordas])
))
cv2.imshow("Dados presentes: "+ str(len(objetos)), imagens)
cv2.waitKey(0)

draw = imgCol.copy()
draw = cv2.drawContours(draw, objetos,-1, (255, 0, 0), 2)

escrever(draw,"Foram encontrados "+str(len(objetos)) + " dados")

cv2.imshow("Resultado", draw)
cv2.waitKey(0)