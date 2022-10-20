# importando as bibliotecas
from pyzbar import pyzbar
import cv2 as cv
from glob import glob
import time


def decode(img):
    # decodifica todos os códigos de barras de uma imagem
    decoded_objects = pyzbar.decode(img)
    for obj in decoded_objects:
        # desenha o código de barras
        print("código de barras detectado:", obj)
        img = draw_barcode(obj, img)
        # imprimir tipo e dados de código de barras
        print("Tipo:", obj.type)
        print("Dados:", obj.data, '\n')

    return img


def draw_barcode(decoded, img):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv.line(img, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    # é só descomentar acima e comentar abaixo se quiser desenhar um polígono e não um retângulo
    img = cv.rectangle(img, (decoded.rect.left, decoded.rect.top),
                       (decoded.rect.left + decoded.rect.width,
                        decoded.rect.top + decoded.rect.height),
                       color=(0, 255, 0),
                       thickness=5)
    return img


def show_img(img):
    barcodes = glob(img)
    for barcode_file in barcodes:
        # carrega a imagem para o opencv
        img = cv.imread(barcode_file)
        # decodifica detectar códigos de barras e obter a imagem que é desenhada
        img = decode(img)
        # mostra a imagem
        cv.imshow("Resultado", img)
        cv.waitKey(0)
    return img


if __name__ == "__main__":

    # Starts measuring time
    t_start = time.time()

    # Colocar caminho relativo da imagem
    show_img("/home/User/Folder/imgs/image")

    # Tempo total decorrido (em ms)
    elapsed_time = 1000 * (time.time() - t_start)

    print(f"\tTempo médio: {elapsed_time/2:.1f} ms")
