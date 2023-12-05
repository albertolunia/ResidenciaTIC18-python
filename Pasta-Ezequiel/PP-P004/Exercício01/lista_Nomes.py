# listanomes.py
from analise_Dados import AnaliseDados

class ListaNomes(AnaliseDados):
    @property
    def label(self):
        return "nome"

    def entradaDeDados(self):
        try:
            n = int(input(f"Quantos {self.label}s você deseja adicionar? "))
            for _ in range(n):
                nome = input(f"Digite um {self.label}: ")
                self._dados.append(nome)
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
