# importando as bibliotecas
from pyzbar import pyzbar
import cv2
import imutils


# Função que carrega o decodificador do pyzbar
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


def show_img(img):
    # carrega a imagem para o opencv
    img_copy = img.copy()
    img_ = None
    # decodifica detectar códigos de barras e obter a imagem que é desenhada
    i = 0
    while img_ is None and i < 180:
        img_ = decode(img_copy)
        img_copy = rotate(img_copy)
    # mostra a imagem
    cv2.imshow("Resultado", img_)
    cv2.waitKey(0)
    return img


if __name__ == "__main__":
    # Passar o caminho da imagem que deseja testar
    img = cv2.imread("C:\\Users\\rozas\\OneDrive\\Documentos\\GitHub\\PoC_refactor\\imgs\\bar15.jpeg")
    show_img(img)
    # se quiser usar a camera descomente abaixo
    # tempo de espera pra rotação
    # vid = cv.VideoCapture(0)
    # ret, frame = vid.read()
    # while ret:
    #     show_img(frame)
    #     ret, frame = vid.read()
    #     if cv.waitKey(0) & 0xFF == ord('q'):
    #         break
    # vid.release()
    # cv.destroyAllWindows()
