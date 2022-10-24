import cv2

img = cv2.imread("imgs/bar15.jpeg")

imgr = cv2. rotate(img, rotateCode=2)

h, w, c = img.shape
center = (h//2, w//2)
# usando o complemento para o angulo
rotation_matrix = cv2.getRotationMatrix2D(center, -36, 1)
final_rotated = cv2.warpAffine(img, rotation_matrix,(w,h))


cv2.imshow("rotacionada", final_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()