from barcode import EAN13
from barcode.writer import ImageWriter


numero_aleatorio = '123456789012'  

codigo_de_barras = EAN13(numero_aleatorio, writer=ImageWriter())

caminho_da_imagem = 'codigo_de_barras_ean1312.png'

codigo_de_barras.save(caminho_da_imagem)

print("Imagem do código de barras salva como:", caminho_da_imagem)
