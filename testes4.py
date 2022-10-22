import cv2
import imutils

image = cv2.imread("imgs/bar15.jpeg")
 
rot = imutils.rotate(image, angle=-36)
cv2.imshow("Rotated", rot)
cv2.waitKey(0)