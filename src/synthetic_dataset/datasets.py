import os
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image
import random

def generate_and_save_random_bar_code(num_folder=10, images_by_folder=10):
    for i in range(1, num_folder + 1):
        name_folder = f'barcode{i}'
        os.makedirs(name_folder, exist_ok=True)
        
        for j in range(images_by_folder):
            random_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            barcode = EAN13(random_number, writer=ImageWriter())
            
            image_path_without_extension = os.path.join(name_folder, random_number)
        
            barcode.save(image_path_without_extension)
            
            image_path_with_extension = f"{image_path_without_extension}.png"
            
            angle_rotation = random.randint(0, 360)
            
            image = Image.open(image_path_with_extension)
            rotated_image = image.rotate(angle_rotation, expand=True)  
            rotated_image.save(image_path_with_extension)

if __name__ == "__main__":
    generate_and_save_random_bar_code()
