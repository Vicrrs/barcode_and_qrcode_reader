# Barcode and Qrcode reader

## Esta PoC (prova de conceito) mostra possiveis soluções para leitores de Qr code e código de barras.


### Explicação do código em português

---

Neste repositório você irá encontrar um código python que consegue fazer a leitura de códigos de barras e Qrcodes em diferentes posições. Sendo na horizontal, vertical ou Diagonal. Usando uma função do imutils para rotacionar a imagem até ele conseguir ler. O código que consegue fazer a leitura é o scripts/reader5.py. Os outros readers vieram de uma série de tentativas para essa versão final.

### Explanation of the code in English

---

In this repository you will find a python code that can read barcodes and qrcodes in different positions. Horizontally, vertically or diagonally. Using an imutils function to rotate the image until it can read it. The code that can read is scripts/reader5.py. The other readers came from a series of trials for this final version.



## Clonando repositório


Clone o repositório:

```bash
git clone https://github.com/Vicrrs/barcode_and_qrcode_reader.git
```
Rode no terminal o código abaixo para baixar as bibliotecas necessárias para o porojeto funcionar!

```bash
docker build -t barcode-reader .
```

Para rodar o programa selecione o `reader.py`, passando como parâmetro o caminho relativo da imagem em `show_img("/home/User/PoC1/imgs/imagem")`, os outros asquivos `reader.py` mostram a evolução do algoritmo até chegar na solução solicitada.
A mesma é capaz, agora, de ler qrcode e barcodes em várias posições, verrtical, diagonal e horizontal.

## Esquema do Repositório

* `imgs:` Pasta na qual se encontra as imagens utilizadas para teste do script.

* `barcodes_types:` Imagens de tipos diferentes de Barcodes.

* `synthetic_barcodes`: Imagens geradas sinteticamente com dados randomicos de codigo de barras

* `src`: Códigos e testes feitos!

## Códigos/Scripts utilizados

* `reader.py`: É a solução adotada para ler barcodes em diferentes posições, rotaciona a imagem até ser feita a leitura do barcode!

* `datasets.py`: Gerando imagens randomicas de barcodes em diferentes rotações!

* `barcode_checker.py`: Comparando nome das imagens com a leitura do codigo de barras da imagem e gerando um csv com o resultado da leitura!

* `barcode_quality_checker.py`: Gerando um gráfico para visualizar o resultado da leitura!


## Tipos de código de Barras
Ao todo foram utilizados 6 tipos de códigos de barras:

* `Code 128`
* `Databar`
* `EAN`
* `25 Itercalado`
* `ITF-14`
* `UPC`

Na qual o algoritmo mostrou leituras promissoras para o `Code 128`,  `Databar`,  `EAN`,  `25 Itercalado`. E mostrou ineficaz para `ITF-14`  e  `UPC`. Por conta de não ter base de dados no pyzbar para esses dois tipos de códigos de barras! Problema pode ser contornado fazendo treinamento a partir de ma base de dados própria.

## Conclusão

O script desenvolvido (`reader.py`) se mostra eficaz tanto para leitura de Qrcode quanto para códigos de barras de determindas classes. O mesmo consegue rotacionar as imagens, quando não se encontrama na horizonta, para fazer a leitura. 
