# listadatas.py
from analise_Dados import AnaliseDados
from data import Data

class ListaDatas(AnaliseDados):
    @property
    def label(self):
        return "data"

    def entradaDeDados(self):
        try:
            n = int(input(f"Quantas {self.label}s você deseja adicionar? "))
            for _ in range(n):
                while True:
                    try:
                        data_str = input("Digite a data (formato: dd/mm/aaaa): ")
                        dia, mes, ano = map(int, data_str.split('/'))
                        data = Data(dia, mes, ano)
                        break  # Exit the loop if the input is valid
                    except (ValueError, IndexError) as e:
                        print(f"Erro: {e}")
                self._dados.append(data)
        except ValueError:
            print("Erro: Insira um número válido.")

    def mostraMenor(self):
        print(f"Menor {self.label}: {min(self._dados)}")

    def mostraMaior(self):
        print(f"Maior {self.label}: {max(self._dados)}")

    def calcularMediana(self):
        sorted_dados = sorted(self._dados)
        mid = len(sorted_dados) // 2
        if len(sorted_dados) % 2 == 0:
            median_values = sorted_dados[mid - 1:mid + 1]
            median = sum(median_values) / 2
        else:
            median = sorted_dados[mid]
        return median

    def listarEmOrdem(self):
        print("Lista de Datas em Ordem:")
        for data in sorted(self._dados):
            print(data)