from src.reader import read_barcode, show_img, camera
import cv2

# Caminho para a imagem a ser testada
image_path = "caminho_para_sua_imagem.jpg"
img = cv2.imread(image_path)

# Leitura e exibição do código de barras
img_code, type_barcode, data_barcode = read_barcode(img)
if img_code is not None:
    show_img(img_code)
else:
    print("Nenhum código de barras encontrado.")

# Para iniciar a leitura de código de barras através da câmera, descomente a linha abaixo
# camera()
