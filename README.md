# PoC Refactor
Esta PoC (prova de conceito) mostra possiveis soluções para leitores de Qr code e código de barras.
## Clonando repositório
Supondo que esteja no Linux, instale o gh:

```bash
sudo apt update
sudo apt install gh
```

Depois clone o repositório:


```bash
gh repo clone Vicrrs/PoC_refactor
```
Rode no terminal o código abaixo para baixar as bibliotecas necessárias para o porojeto funcionar!

```bash
pip install -r requirements.txt
```

Para rodar o programa selecione o `reader1.py`, passando como parâmetro o caminho relativo da imagem em `show_img("/home/User/PoC1/imgs/imagem")`

## Esquema do Repositório

* `barcodes_types:` Imagens de tipos diferentes de Barcodes.

* `imgs:` pasta na qual se encontra as imagens utilizadas para teste do script.

* `scripts:` Pasta na qual se encontra o código que faz a leitura de código de barras e Qr code.

## Tipos de código de Barras
Ao todo foram utilizados 6 tipos de códigos de barras:

* `Code 128`
* `Databar`
* `EAN`
* `25 Itercalado`
* `ITF-14`
* `UPC`

Na qual o algoritmo mostrou leituras promissoras para o `Code 128`,  `Databar`,  `EAN`,  `25 Itercalado`. E mostrou ineficaz para `ITF-14`  e  `UPC`. Por conta de não ter base de dados no pyzbar para esses dois tipos de códigos de barras! Problema pode ser contornado fazendo treinamento a partir de ma base de dados própria.

## Taxa de acerto

A taxa de acerto para o banco de imagens (imgs) foram feitas para as imagens de código de barras com início "bar" e para as imagens de qr code com início "qr". O algoritmo reader1.py mostrou uma taxa de acerto de 75% para os barcodes e 85% para Qr codes.

```bash
Taxa_de_Acerto = (Acertos/Quantidade)*100
```
## Conclusão

O script desenvolvido (`reader1.py`) se mostra eficaz tanto para leitura de Qrcode quanto para códigos de barras de determindas classes. Problema que pode ser contornado criando uma base de dados e fazendo treinamento para reconhecimento das classes defeituosas!
