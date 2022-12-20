import cv2
import imutils

image = cv2.imread("C:\\Users\\rozas\\PycharmProjects\\barcode_and_qrcode_reader\\DataSet\\barcodes\\barcode10\\b3.jpg")

Rotating = imutils.rotate(image, angle=70)

cv2.imshow("Rotating", Rotating)

cv2.waitKey(0)
