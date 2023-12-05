from abc import ABC, abstractmethod
import os

class Data:
    def __init__(self, dia = 1, mes = 1, ano = 2000):
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
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

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

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def getLista(self):
        return self.__lista

    def entradaDeDados(self):
        num_elementos = int(input("Quantos nomes você deseja adicionar? > "))
        for _ in range(num_elementos):
            elemento = input("Digite um nome: ")
            self.__lista.append(elemento)

    def mostraMediana(self):
        self.__lista.sort()
        meio = len(self.__lista) // 2
        return self.__lista[meio]   

    def mostraMenor(self):
        menor = min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = max(self.__lista)
        return maior

    def listarEmOrdem(self):
        print("Lista Ordenada:")
        self.__lista.sort()
        print(self.__lista)

    def __str__(self):
        return str(self.__lista)
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        num_datas = int(input("Quantas datas você deseja adicionar? > "))
        for _ in range(num_datas):
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
            print(end="\n")
            data = Data(dia, mes, ano)
            self.__lista.append(data)
    
    def mostraMediana(self):
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        meio = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[meio])    
     
    def mostraMenor(self):
        menor = min(self.__lista)
        return menor
    
    def mostraMaior(self):
        maior = max(self.__lista)
        return maior

    def listarEmOrdem(self):
        print("Lista Ordenada:")
        self.__lista.sort(key=lambda x: (x.ano, x.mes, x.dia))
        for item in self.__lista:
            print(item)

    def modificarDiaAntes2019(self):
        print("Alterando datas anteriores a 2019:")
        self.__lista = list(map(lambda data: Data(1, data.mes, data.ano) if data.ano < 2019 else data, self.__lista))
        for data in self.__lista:
            print(data)
    
    def __str__(self):
        return str(self.__lista)

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def getLista(self):
        return self.__lista

    def entradaDeDados(self):
        num_salarios = int(input("Quantos salários você deseja adicionar? > "))
        for _ in range(num_salarios):
            salario = float(input("Digite um salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        mediana = len(sorted_lista) // 2
        if len(sorted_lista) % 2 == 0:
            mediana = (sorted_lista[mediana - 1] + sorted_lista[mediana]) / 2
        else:
            mediana = sorted_lista[mediana]
        print("Mediana:", mediana)

    def mostraMenor(self):
        menor = min(self.__lista)
        return menor

    def mostraMaior(self):
        maior = max(self.__lista)
        return maior
    
    def listarEmOrdem(self):
        print("Lista Ordenada:")
        self.__lista.sort()
        print(self.__lista)

    def reajustarSalarios(self):
        print("Reajustando salários em 10%:")
        self.__lista = list(map(lambda salario: salario * 1.1, self.__lista))
        for salario in self.__lista:
            print("Salario: {:.2f}".format(salario))
    
    def __str__(self):
        return str(self.__lista)

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        num_idades = int(input("Quantas idades você deseja adicionar? > "))
        for _ in range(num_idades):
            idade = int(input("Digite uma idade: "))
            self.__lista.append(idade)
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        sorted_lista = sorted(self.__lista)
        mediana = len(sorted_lista) // 2
        if len(sorted_lista) % 2 == 0:
            mediana = (sorted_lista[mediana - 1] + sorted_lista[mediana]) / 2
        else:
            mediana = sorted_lista[mediana]
        print("Mediana:", mediana)   
    
    def mostraMenor(self):
        menor = min(self.__lista)
        return menor
    
    def mostraMaior(self):
        maior = max(self.__lista)
        return maior
    
    def listarEmOrdem(self):
        print("Lista Ordenada:")
        self.__lista.sort()
        print(self.__lista)

    def __str__(self):
        return str(self.__lista)

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        limparTerminal()
        print("Menu:")
        print("1. Incluir um nome")
        print("2. Incluir um salario")
        print("3. Incluir uma data")
        print("4. Incluir uma idade")
        print("5. Listar os salarios de cada pessoa")
        print("6. Calcular salario com reajuste de 10%")
        print("7. Modificar datas anteriores a 2019")
        print("0. Sair do programa")
        escolha = input("Digite uma opcao (0-7): ")

        if escolha == "0":
            print("Encerrando o programa.")
            break
        elif escolha == "1":
            limparTerminal()
            nomes.entradaDeDados()
            input("Pressione Enter para continuar...")
        elif escolha == "2":
            limparTerminal()
            salarios.entradaDeDados()
            input("Pressione Enter para continuar...")
        elif escolha == "3":
            limparTerminal()
            datas.entradaDeDados()
            input("Pressione Enter para continuar...")
        elif escolha == "4":
            limparTerminal()
            idades.entradaDeDados()
            input("Pressione Enter para continuar...")
        elif escolha == "5":
            limparTerminal()
            if(len(nomes.getLista()) == 0 or len(salarios.getLista()) == 0):
                print("Nenhum nome ou salario encontrado.")
            else:
                if(len(nomes.getLista()) == len(salarios.getLista())):
                    for nome, salario in zip(nomes.getLista(), salarios.getLista()):
                        print(f"{nome} tem salário de {salario}")
                else:
                    print("As listas de nomes e salarios devem ter a mesma quantidade.")
            input("Pressione Enter para continuar...")
        elif escolha == "6":
            limparTerminal()
            salarios.reajustarSalarios()
            input("Pressione Enter para continuar...")
        elif escolha == "7":
            limparTerminal()
            datas.modificarDiaAntes2019()
            input("Pressione Enter para continuar...")
        else:
            print("Opção invalida. Tente novamente.")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
