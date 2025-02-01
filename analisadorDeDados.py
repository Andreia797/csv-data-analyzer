import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(file_path):
    data = pd.read_csv(file_path)
    print("\nResumo dos Dados:")
    print(data.describe())

    column = input("\nDigite o nome da coluna para gerar o gráfico: ")
    if column in data.columns:
        data[column].hist()
        plt.title(f"Distribuição de {column}")
        plt.xlabel(column)
        plt.ylabel("Frequência")
        plt.show()
    else:
        print("Coluna não encontrada.")

def main():
    print("Analisador de Dados CSV")
    file_path = input("Digite o caminho do arquivo CSV: ")
    analyze_data(file_path)

if __name__ == "__main__":
    main()
