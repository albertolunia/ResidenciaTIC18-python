from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC):
    def __init__(self, tipoDeDados):
        self._tipoDeDados = tipoDeDados
        self._dados = []

    @property
    @abstractmethod
    def label(self):
        pass

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def calcularMediana(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self._tipoDeDados}) - Dados: {self._dados}"

    def __len__(self):
        return len(self._dados)

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

class ListaDatas(AnaliseDados):
    @property
    def label(self):
        return "data"

    def entradaDeDados(self):
        try:
            n = int(input(f"Quantas {self.label}s você deseja adicionar? "))
            for _ in range(n):
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                data = Data(dia, mes, ano)
                self._dados.append(data)
        except ValueError as e:
            print(f"Erro: {e}")

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

class ListaSalarios(AnaliseDados):
    @property
    def label(self):
        return "salário"

    def entradaDeDados(self):
        try:
            n = int(input(f"Quantos {self.label}s você deseja adicionar? "))
            for _ in range(n):
                salario = float(input(f"Digite um {self.label}: "))
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

class ListaIdades(AnaliseDados):
    @property
    def label(self):
        return "idade"

    def entradaDeDados(self):
        try:
            n = int(input(f"Quantas {self.label}s você deseja adicionar? "))
            for _ in range(n):
                idade = int(input(f"Digite uma {self.label}: "))
                self._dados.append(idade)
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

def main():
    tipo_nome = type("String")
    tipo_data = type(Data)
    tipo_salario = type(float)
    tipo_idade = type(int)

    nomes = ListaNomes(tipo_nome)
    datas = ListaDatas(tipo_data)
    salarios = ListaSalarios(tipo_salario)
    idades = ListaIdades(tipo_idade)

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        print(lista)
        print(f"Mediana: {lista.calcularMediana()}")
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

if __name__ == "__main__":
    main()

