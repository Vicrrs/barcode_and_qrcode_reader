# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# constrói a análise do argumento e analisa os argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the image file")
args = vars(ap.parse_args())
# carregar a imagem do disco
image = cv2.imread(args["image"])
# loop over the rotation angles
# for angle in np.arange(0, 360, 15):
#     rotated = imutils.rotate(image, angle)
#     cv2.imshow("Rotated (Problematic)", rotated)
#     cv2.waitKey(0)
# loop sobre os ângulos de rotação novamente, desta vez garantindo
# nenhuma parte da imagem é cortada
for angle in np.arange(0, 360, 15):
    rotated = imutils.rotate_bound(image, angle)
    cv2.imshow("Rotated (Correct)", rotated)
    cv2.waitKey(0)
