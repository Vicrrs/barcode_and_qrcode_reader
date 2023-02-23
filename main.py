from scripts.reader9 import read_barcode, show_img, camera
import cv2

# Pass the path of the image you want to test
img = cv2.imread(
    r"C:\Users\rozas\PycharmProjects\barcode_and_qrcode_reader\DataSet\imgs\barcodes\barcode20\b5.jpg")


img_code, type_barcode, data_barcode = read_barcode(img)


show_img(img_code)

# camera()
