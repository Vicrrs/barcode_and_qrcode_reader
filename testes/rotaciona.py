# import the necessary packages
import numpy as np
import imutils
import cv2
# construir o argumento analisar e analisar os argumentos
image = cv2.imread("/home/roza/PycharmProjects/PoC1/imgs/bar15.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 20, 100)
# encontra contornos no mapa de arestas
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# garante que pelo menos um contorno foi encontrado
if len(cnts) > 0:
	# pegue o contorno maior e desenhe uma máscara para a pílula
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
	# calcula sua caixa delimitadora de pílula e, em seguida, extrai o ROI,
    # e aplique a máscara
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = image[y:y + h, x:x + w]
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,
		mask=maskROI)
	for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate_bound(imageROI, angle)
		cv2.imshow("Rotated (Correct)", rotated)
		cv2.waitKey(0)