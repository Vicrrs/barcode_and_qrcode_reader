import csv
import os
import matplotlib.pyplot as plt

def check_barcode_reader_quality(csv_file_path):
    total_count = 0
    correct_count = 0
    incorrect_count = 0

    if not os.path.exists(csv_file_path):
        print("Arquivo CSV não encontrado.")
        return

    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Verificar as chaves (nomes das colunas) para evitar KeyError
        if 'Verification Result' not in reader.fieldnames:
            print(f"Colunas disponíveis no CSV: {reader.fieldnames}")
            print("A coluna 'Verification Result' não foi encontrada.")
            return
        
        for row in reader:
            total_count += 1
            if row['Verification Result'] == 'Correto':
                correct_count += 1
            else:
                incorrect_count += 1

    accuracy = (correct_count / total_count) * 100 if total_count > 0 else 0

    print(f"Total de códigos de barras processados: {total_count}")
    print(f"Quantidade de leituras corretas: {correct_count}")
    print(f"Quantidade de leituras incorretas: {incorrect_count}")
    print(f"Acurácia do leitor: {accuracy:.2f}%")
    
    # mostrar a qualidade do leitor
    labels = ['Correct', 'Incorrect']
    values = [correct_count, incorrect_count]

    fig, ax = plt.subplots()
    bars = plt.bar(labels, values, color=['green', 'red'])
    # texto de contagem nas barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, yval, ha='center', va='bottom')

    # resultado do print no gráfico
    textstr = f'Total: {total_count}\nCorrect: {correct_count}\nIncorrect: {incorrect_count}\nAccuracy: {accuracy:.2f}%'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.95, 0.95, textstr, transform=ax.transAxes, fontsize=14,verticalalignment='top', horizontalalignment='right', bbox=props)

    plt.title('Barcode Reader Accuracy')
    plt.xlabel('Result Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

csv_file_path = 'C:\\Users\\rozas\\Documents\\Projetos_GITHUB\\barcode_and_qrcode_reader\\imgs\\synthetic_barcodes\\barcode_results.csv'
check_barcode_reader_quality(csv_file_path)
