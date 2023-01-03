# Barcode and Qrcode reader

## Esta PoC (prova de conceito) mostra possiveis soluções para leitores de Qr code e código de barras.


### Explicação do código em português

---

Neste repositório você irá encontrar um código python que consegue fazer a leitura de códigos de barras e Qrcodes em diferentes posições. Sendo na horizontal, vertical ou Diagonal. Usando uma função do imutils para rotacionar a imagem até ele conseguir ler. O código que consegue fazer a leitura é o scripts/reader5.py. Os outros readers vieram de uma série de tentativas para essa versão final.

### Explanation of the code in English

---

In this repository you will find a python code that can read barcodes and qrcodes in different positions. Horizontally, vertically or diagonally. Using an imutils function to rotate the image until it can read it. The code that can read is scripts/reader5.py. The other readers came from a series of trials for this final version.



## Clonando repositório
Supondo que esteja no Linux, instale o gh:

```bash
sudo apt update
sudo apt install gh
```

Depois clone o repositório:


```bash
gh repo clone Vicrrs/barcode_and_qrcode_reader
```
Rode no terminal o código abaixo para baixar as bibliotecas necessárias para o porojeto funcionar!

```bash
pip install -r requirements.txt
```
Caso apareça um erro pedindo instalação do pyzbar, rode:
```bash
pip install pyzbar
pip install pyzbar[scripts]
```

Para rodar o programa selecione o `reader9.py`, passando como parâmetro o caminho relativo da imagem em `show_img("/home/User/PoC1/imgs/imagem")`, os outros asquivos `reader.py` mostram a evolução do algoritmo até chegar na solução solicitada.
A mesma é capaz, agora, de ler qrcode e barcodes em várias posições, verrtical, diagonal e horizontal.

## Esquema do Repositório

* `barcodes_types:` Imagens de tipos diferentes de Barcodes.

* `imgs:` Pasta na qual se encontra as imagens utilizadas para teste do script.

* `scripts:` Pasta na qual se encontra o código que faz a leitura de código de barras e Qr code.

* `testes:` Pasta na qual se encontra algoritmos que foram testados para embasar a solução final.

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

O script desenvolvido (`reader9.py`) se mostra eficaz tanto para leitura de Qrcode quanto para códigos de barras de determindas classes. O mesmo consegue rotacionar as imagens, quando não se encontrama na horizonta, para fazer a leitura. 
