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

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass


class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        n = int(input("Quantos nomes você deseja adicionar? "))
        for _ in range(n):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        sorted_nomes = sorted(self.__lista)
        mid = len(sorted_nomes) // 2
        print(f"Mediana: {sorted_nomes[mid]}")

    def mostraMenor(self):
        print(f"Menor nome: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior nome: {max(self.__lista)}")

    def __str__(self):
        return ", ".join(self.__lista)


class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        n = int(input("Quantas datas você deseja adicionar? "))
        for _ in range(n):
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano: "))
            data = Data(dia, mes, ano)
            self.__lista.append(data)

    def mostraMediana(self):
        sorted_datas = sorted(self.__lista)
        mid = len(sorted_datas) // 2
        print(f"Mediana: {sorted_datas[mid]}")

    def mostraMenor(self):
        print(f"Menor data: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior data: {max(self.__lista)}")

    def __str__(self):
        return ", ".join(str(data) for data in self.__lista)


class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        n = int(input("Quantos salários você deseja adicionar? "))
        for _ in range(n):
            salario = float(input("Digite um salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        sorted_salarios = sorted(self.__lista)
        mid = len(sorted_salarios) // 2
        print(f"Mediana: {sorted_salarios[mid]}")

    def mostraMenor(self):
        print(f"Menor salário: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior salário: {max(self.__lista)}")

    def __str__(self):
        return ", ".join(str(salario) for salario in self.__lista)


class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        n = int(input("Quantas idades você deseja adicionar? "))
        for _ in range(n):
            idade = int(input("Digite uma idade: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        sorted_idades = sorted(self.__lista)
        mid = len(sorted_idades) // 2
        print(f"Mediana: {sorted_idades[mid]}")

    def mostraMenor(self):
        print(f"Menor idade: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior idade: {max(self.__lista)}")

    def __str__(self):
        return ", ".join(str(idade) for idade in self.__lista)


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

   


if __name__ == "__main__":
    main()
