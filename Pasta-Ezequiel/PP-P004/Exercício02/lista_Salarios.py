
from analise_Dados import AnaliseDados

class ListaSalarios(AnaliseDados):
    @property
    def label(self):
        return "salário"

    def entradaDeDados(self):
        try:
            n = int(input(f"Quantos {self.label}s você deseja adicionar? "))
            for _ in range(n):
                while True:
                    try:
                        salario = float(input(f"Digite um {self.label}: "))
                        if salario < 0:
                            raise ValueError("O salário não pode ser negativo.")
                        break  
                    except ValueError as e:
                        print(f"Erro: {e}")
                self._dados.append(salario)
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
        print("Lista de Salários em Ordem:")
        for salario in sorted(self._dados):
            print(salario)