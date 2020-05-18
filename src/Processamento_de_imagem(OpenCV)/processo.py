import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    (x, frame) = cap.read()
    if not x:
        break
    frame = frame[::2,::2]
    frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_sv = cv2.GaussianBlur(frame_pb, (3, 3), 0)
    (T, frame_bin1) = cv2.threshold(frame_sv, 160, 255, cv2.THRESH_BINARY)
    (T, frame_bin2) = cv2.threshold(frame_sv, 160, 255, cv2.THRESH_BINARY_INV)
    bordas = cv2.Canny(frame_bin1, 100, 300)

    pilha = np.vstack([
        np.hstack([frame_pb, frame_sv]),
        np.hstack([frame_bin1, bordas])
    ])
    cv2.imshow("Original", frame)
    cv2.imshow("Resultado", pilha)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break