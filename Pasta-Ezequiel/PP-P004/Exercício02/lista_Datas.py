# listadatas.py
from analise_Dados import AnaliseDados
from data import Data
from datetime import datetime, timedelta

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
       sorted_dados = sorted(self._dados, key=lambda x: (x.ano, x.mes, x.dia))
       mid = len(sorted_dados) // 2
       if len(sorted_dados) % 2 == 0:
         d1 = datetime(sorted_dados[mid - 1].ano, sorted_dados[mid - 1].mes, sorted_dados[mid - 1].dia)
         d2 = datetime(sorted_dados[mid].ano, sorted_dados[mid].mes, sorted_dados[mid].dia)
         t1 = d1.timestamp()
         t2 = d2.timestamp()
         t_avg = (t1 + t2) / 2
         d_avg = datetime.fromtimestamp(t_avg)
         median = Data(d_avg.day, d_avg.month, d_avg.year)
       else:
         median = sorted_dados[mid]
       return median
    
    def listarEmOrdem(self):
        print(f"Lista de {self.label}s em Ordem:")
        for data in sorted(self._dados, key=lambda x: (x.ano, x.mes, x.dia)):
            print(data)