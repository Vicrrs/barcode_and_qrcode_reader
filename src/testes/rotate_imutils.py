import imutils
import cv2

img = cv2.imread('C:\\Users\\rozas\\PycharmProjects\\barcode_and_qrcode_reader\\testes\\barcodeteste.jpg')

rotate_image = imutils.rotate_bound(img, 32)
window_name='Rotate Image by Angle in Python'

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()