import cv2
import numpy as np


img = cv2.imread('ponte.jpg')
img = img[::2,::2] # Diminui a imagem
suave = np.vstack([
 np.hstack([img,
 cv2.GaussianBlur(img, ( 3, 3), 0)]),
 np.hstack([cv2.GaussianBlur(img, ( 5, 5), 0),
 cv2.GaussianBlur(img, ( 7, 7), 0)]),
 np.hstack([cv2.GaussianBlur(img, ( 9, 9), 0),
 cv2.GaussianBlur(img, (11, 11), 0)]),
 ])
cv2.imshow("Imagem original e suavisadas pelo filtro Gaussiano", suave)
cv2.waitKey(0)
