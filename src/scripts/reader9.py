# importando as bibliotecas
from pyzbar import pyzbar
import cv2
from imutils import rotate_bound
import time


# Função que carrega o decodificador do pyzbar
def decode(img):
    # decodifica todos os códigos de barras de uma imagem
    decoded_objects = pyzbar.decode(img)
    if not decoded_objects:
        return None, None, None
    for obj in decoded_objects:
        # desenha o código de barras
        print("código de barras detectado:", obj)
        img = draw_barcode(obj, img)
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


def read_barcode(img):
    # carrega a imagem para o opencv
    img_copy = img.copy()
    img_ = None
    step = 5
    i = 1
    # decodifica detectar códigos de barras e obter a imagem que é desenhada
    while img_ is None and i < 180:
        img_, type_barcode, data_barcode = decode(img_copy)
        if data_barcode:
            break
        img_copy = rotate_bound(img_copy, i)
        i += step
    return img_, type_barcode, data_barcode

# Funcao para exibir a imagem na janela
def show_img(img):
    cv2.imshow('Janela', img)
    cv2.waitKey(0)


def cam_decode(frame):
    # decodificando barcode e qrcode
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        # Desenhando bbox azul como contorno
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # definindo cor e fonte da lentra
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6),
                    font, 0.7, (255, 0, 0), 1)
    return frame


def camera():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    # Laço para mostrar a imagem e fechar a aba
    while ret:
        ret, frame = camera.read()
        frame = cam_decode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()



