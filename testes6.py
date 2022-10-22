import cv2
import numpy as np

img = cv2.imread("/home/roza/PycharmProjects/PoC1/imgs/bar15.jpeg")

# Convertendo a imagem para cor cinza e aplicando a detecção de bordas por Canny
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bordas = cv2.Canny(cinza, 70, 255)

# Detecção das linhas probabilisticas

lines = cv2.HoughLinesP(bordas, 1, np.pi / 180, 20, 255)

# Detecção de linha do Hough, laço for para percorrer toda imagem

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Imagem", img)
cv2.waitKey(0)
cv2.destroyAllWindows()