# importando as bibliotecas
import cv2
import imutils
import numpy as np
from pyzbar import pyzbar
from pyzbar.pyzbar import decode


# Função que carrega o decodificador do pyzbar
def decodes(img):
    # decodifica todos os códigos de barras de uma imagem
    decoded_objects = pyzbar.decode(img)
    if not decoded_objects:
        return None, None, None
    for obj in decoded_objects:
        # desenha o código de barras
        print("código de barras detectado:", obj)
        img = draw_barcode(obj, img)
        # imprimir tipo e dados de código de barras
        print("Tipo:", obj.type)
        print("Dados:", obj.data.decode('utf-8'), '\n')
        type_barcode = obj.type
        data_barcode = obj.data.decode('utf-8')

    return img, type_barcode, data_barcode


# Função para desenhar a bbox
def draw_barcode(decoded, img):
    img = cv2.rectangle(img, (decoded.rect.left, decoded.rect.top),
                        (decoded.rect.left + decoded.rect.width,
                         decoded.rect.top + decoded.rect.height),
                        color=(0, 255, 0),
                        thickness=5)
    return img


# Função para rotacionar a imagem
def rotate(img):
    rot = imutils.rotate(img, angle=-1)
    return rot


def read_barcode(img):
    # carrega a imagem para o opencv
    img_copy = img.copy()
    img_ = None
    # decodifica detectar códigos de barras e obter a imagem que é desenhada
    i = 0
    while img_ is None and i < 180:
        img_, type_barcode, data_barcode = decodes(img_copy)
        img_copy = rotate(img_copy)
    return img_, type_barcode, data_barcode


def show_img(img):
    cv2.imshow('Janela', img)
    cv2.waitKey(0)


def cam_decoder(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)

        cv2.putText(frame, string, (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        # print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        return barcodeData, barcodeType


def camera():
    cap = cv2.VideoCapture(0)
    while True:
        global frame
        ret, frame = cap.read()
        cam_decoder(frame)
        cv2.imshow('Image', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break


if __name__ == "__main__":
    # Passar o caminho da imagem que deseja testar
    # img = cv2.imread(
    #     "/home/icts-0891/Documentos/Projeto/imgs/bar15.jpeg")

    # img_code, type_barcode, data_barcode = read_barcode(img)

    # show_img(img_code)

    camera()
