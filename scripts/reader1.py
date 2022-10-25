# Importando biblioteca
import cv2
from pyzbar.pyzbar import decode

# Faça um método para decodificar o código de barras


def BarcodeReader(image):

    # leia a imagem no array numpy usando cv2
    img = cv2.imread(image)

    # Decodifique a imagem do código de barras
    detectedBarcodes = decode(img)

    # Se não for detectado, imprima a mensagem
    if not detectedBarcodes:
        print("Código de barras não detectado ou seu código de barras está em branco/corrompido!")
    else:

        # Percorra todos os códigos de barras detectados na imagem
        for barcode in detectedBarcodes:

            # Localize a posição do código de barras na imagem
            (x, y, w, h) = barcode.rect

            # Coloque o retângulo na imagem usando
            # cv2 para destacar o código de barras
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                # Imprima os dados do código de barras
                print(barcode.data)
                print(barcode.type)

    # Exibir a imagem
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Pegue a imagem do usuário
    image = "Img.jpg"
    BarcodeReader(image)
