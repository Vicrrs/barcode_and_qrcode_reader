import numpy as np
import cv2 as cv
# testes + testes1
img = cv.imread("/home/roza/PycharmProjects/PoC1/imgs/bar15.jpeg")
# 4 a 15 descobre a regiao do barcode
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gradX = cv.Sobel(gray, ddepth=cv.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv.Sobel(gray, ddepth=cv.CV_32F, dx=0, dy=1, ksize=-1)
gradient = cv.subtract(gradX, gradY)
gradient = cv.convertScaleAbs(gradient)
blurred = cv.blur(gradient, (9, 9))
(_, thresh) = cv.threshold(blurred, 225, 255, cv.THRESH_BINARY)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (21, 7))
closed = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
closed = cv.erode(closed, None, iterations=4)
closed = cv.dilate(closed, None, iterations=4)
(cnts, _) = cv.findContours(closed.copy(),
                            cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv.contourArea, reverse=True)[0]
c_ = max(cnts, key=cv.contourArea)
x, y, w, h = cv.boundingRect(c_)
# cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
crop_img = img[y:y+h, x:x+w]
# rect = cv.minAreaRect(c)
angle = cv.minAreaRect(c)[2]
# h, w, c = img.shape
center = (h//2, w//2)
# usando o complemento para o angulo
rotation_matrix = cv.getRotationMatrix2D(center, angle - 90, 1)
final_rotated = cv.warpAffine(crop_img, rotation_matrix, (w, h))
# box = np.int0(cv.boxPoints(rect))
# cv.drawContours(img, [box], -1, (0, 255, 0), 3)
# cv.imwrite('final.jpg', final_rotated)
cv.imshow("Image", final_rotated)
cv.waitKey(0)
