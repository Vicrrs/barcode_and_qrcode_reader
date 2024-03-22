# barcode_checker.py
import os
import csv
import cv2
from reader import read_barcode

def check_barcodes_and_save_to_csv(root_directory):
    csv_headers = ["Image", "Decoded Value", "Expected Value", "Verification Result"]
    csv_file_path = os.path.join(root_directory, 'barcode_results.csv')

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)

        for folder_name in os.listdir(root_directory):
            folder_path = os.path.join(root_directory, folder_name)
            if os.path.isdir(folder_path):
                for image_name in os.listdir(folder_path):
                    if image_name.endswith('.png'):
                        image_path = os.path.join(folder_path, image_name)
                        image = cv2.imread(image_path)
                        if image is None:
                            print(f"Erro ao ler a imagem: {image_path}")
                            continue

                        _, _, decoded_value = read_barcode(image)

                        decoded_value_without_checksum = decoded_value[:-1] if decoded_value else None
                        expected_value = os.path.splitext(image_name)[0]
                        result = 'Correto' if decoded_value_without_checksum == expected_value else 'Incorreto'
                        writer.writerow([image_name, decoded_value_without_checksum, expected_value, result])


root_directory = 'C:\\Users\\rozas\\Documents\\Projetos_GITHUB\\barcode_and_qrcode_reader\\imgs\\synthetic_barcodes'
check_barcodes_and_save_to_csv(root_directory)
