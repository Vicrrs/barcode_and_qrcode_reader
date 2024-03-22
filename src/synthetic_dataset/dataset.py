from barcode import EAN13
from barcode.writer import ImageWriter
import random

def generate_and_save_random_bar_code():
    random_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    create_barcode = EAN13(random_number, writer=ImageWriter())
    name_file = f'{random_number}'
    create_barcode.save(name_file)
    print(f"Image Barcode '{name_file}' generate!")
    
generate_and_save_random_bar_code()
