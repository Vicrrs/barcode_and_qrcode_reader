# Importações necessárias
from pyzbar import pyzbar
import cv2
from imutils import rotate_bound

# Decodifica códigos de barras e QR codes na imagem
def decode(image):
    decoded_objects = pyzbar.decode(image)
    if not decoded_objects:
        return None, None, None
    for obj in decoded_objects:
        # Desenha o retângulo ao redor do código decodificado
        image = cv2.rectangle(image, (obj.rect.left, obj.rect.top),
                              (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
                              color=(0, 255, 0), thickness=5)
        type_barcode = obj.type
        data_barcode = obj.data.decode('utf-8')
        print(f"Código de barras detectado: {obj}")
    return image, type_barcode, data_barcode

# Lê o código de barras da imagem, tentando diferentes rotações
def read_barcode(image):
    img_copy = image.copy()
    step = 5
    for angle in range(0, 180, step):
        img_rotated, type_barcode, data_barcode = decode(img_copy)
        if data_barcode:
            return img_rotated, type_barcode, data_barcode
        img_copy = rotate_bound(image, angle)
    return None, None, None

# Exibe a imagem na janela
def show_img(image):
    cv2.imshow('Resultado', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Decodifica e anota barcodes em tempo real da câmera
def cam_decode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 0.7, (255, 0, 0), 1)
    return frame

# Inicializa a câmera e decodifica barcodes em tempo real
def camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Falha ao capturar imagem da câmera.")
            break
        frame = cam_decode(frame)
        cv2.imshow('Leitor de Código de Barras e QR Code', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
            break
    cap.release()
    cv2.destroyAllWindows()
