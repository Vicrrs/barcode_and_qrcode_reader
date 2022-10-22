# importando as bibliotecas
from pyzbar import pyzbar
import cv2 as cv
import imutils
import numpy as np


def decode(img):
    # decodifica todos os códigos de barras de uma imagem
    decoded_objects = pyzbar.decode(img)
    if not decoded_objects:
        return None
    for obj in decoded_objects:
        # desenha o código de barras
        print("código de barras detectado:", obj)
        img = draw_barcode(obj, img)
        # imprimir tipo e dados de código de barras
        print("Tipo:", obj.type)
        print("Dados:", obj.data, '\n')

    return img


def draw_barcode(decoded, img):

    img = cv.rectangle(img, (decoded.rect.left, decoded.rect.top),
                       (decoded.rect.left + decoded.rect.width,
                        decoded.rect.top + decoded.rect.height),
                       color=(0, 255, 0),
                       thickness=5)
    return img


def rotate(img):
    rot = imutils.rotate(img, angle=-1)
    return rot


def show_img(img):
    # carrega a imagem para o opencv
    img_copy = img.copy()
    img_ = None
    # decodifica detectar códigos de barras e obter a imagem que é desenhada
    i = 0
    while img_ is None and i < 180:
        img_ = decode(img_copy)
        img_copy = rotate(img_copy)
    # img = decode(img)
    # mostra a imagem
    cv.imshow("Resultado", img_)
    cv.waitKey(0)
    return img


if __name__ == "__main__":

    img = cv.imread("/home/roza/PycharmProjects/PoC1/imgs/bar15.jpeg")
    show_img(img)
    # vid = cv.VideoCapture(0)
    # ret, frame = vid.read()
    # while ret:
    #     show_img(frame)
    #     ret, frame = vid.read()
    #     if cv.waitKey(0) & 0xFF == ord('q'):
    #         break
    # vid.release()
    # cv.destroyAllWindows()
