
from abc import ABC, abstractmethod

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

    def entradaDeDados(self):
        
        qtd_elementos = int(input("Digite a quantidade de elementos que irão existir na lista de nomes: "))
        for i in range(qtd_elementos):
            nome = input("Digite o nome para ser adicionado a lista: ")
            self.__lista.append(nome)
        
    def mostraMediana(self):
        
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        if (len(sorted_lista) % 2 == 0):
            print(f"Mediana: {sorted_lista[meio-1]}")
        else:
            print(f"Mediana: {sorted_lista[meio]}")
       
    def mostraMenor(self):
        print(f"Menor: {min(self.__lista)}")
        
    def mostraMaior(self):
        print(f"Maior: {max(self.__lista)}") 
       
    def listarEmOrdem(self):
        print(f"Lista ordenada: {sorted(self.__lista)}")
        
    def mostraNomeESalario(self, lista_salario):
        print("\nNomes e salarios:")
        for nome, salario in zip(self.__lista, lista_salario):
            print(f"Nome: {nome}, Salário: {salario}")

    def __str__(self):
        return f'Objeto da classe ListaNomes com lista: {self.__lista}'
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        qtd_elementos = int(input("Digite a quantidade de elementos que irão existir na lista de datas: "))
        for i in range(qtd_elementos):
            print(f"\nData {i + 1}:")
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
            data = Data(dia, mes, ano)
            self.__lista.append(data)
    
    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        if (len(sorted_lista) % 2 == 0):
            print(f"Mediana: {sorted_lista[meio-1]}")
        else:
            print(f"Mediana: {sorted_lista[meio]}")
        
    def mostraMenor(self):
        print(f"Menor: {min(self.__lista)}")
        
    def mostraMaior(self):
        print(f"Maior: {max(self.__lista)}")
        
       
    def listarEmOrdem(self):
        print(f"Lista ordenada: ", end="")
        sorted_lista = sorted(self.__lista)
        for i in sorted_lista:
            print(f"[{i}]", end=" ")
    
    def modificaDatas(self):
        self.__lista = filter(lambda data: data.ano < 2019, self.__lista)
        print("\nDatas modificadas:")
        for data in self.__lista:
            data.dia = 1
            print(data)
    def __str__(self):
        return f'\nObjeto da classe ListaDatas com lista: {self.__lista}'

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        
    
    def getLista(self):
        return self.__lista

    def entradaDeDados(self):
        qtd_elementos = int(input("Digite a quantidade de elementos que irão existir na lista de salarios: "))
        for i in range(qtd_elementos):
            salario = float(input("Digite o salario para ser adicionado a lista: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        if (len(sorted_lista) % 2 == 0):
            print(f"Mediana: {(sorted_lista[meio - 1] + sorted_lista[meio]) / 2}")
        else:
            print(f"Mediana: {sorted_lista[meio]}")
        
    def mostraMenor(self):
        print(f"Menor: {min(self.__lista)}")
       
    def mostraMaior(self):
        print(f"Maior: {max(self.__lista)}") 
       
    def listarEmOrdem(self):
        print(f"Lista ordenada: {sorted(self.__lista)}")
        
    def calculaFolhaReajuste(self):
        salarios_reajustados = list(map(lambda salario: salario * (1 + 10 / 100), self.__lista))
        custo_total = sum(salarios_reajustados)
        print("\nCusto total da folha de pagamento após reajuste de 10%: R$", custo_total)
    def __str__(self):
        return f'Objeto da classe ListaSalarios com lista: {self.__lista}'

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        qtd_elementos = int(input("Digite a quantidade de elementos que irão existir na lista de idades: "))
        for i in range(qtd_elementos):
            idade = int(input("Digite a idade para ser adicionada a lista: "))
            self.__lista.append(idade)
       
    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        if (len(sorted_lista) % 2 == 0):
            print(f"Mediana: {(sorted_lista[meio - 1] + sorted_lista[meio]) / 2}")
        else:
            print(f"Mediana: {sorted_lista[meio]}")
       
    def mostraMenor(self):
        print(f"Menor: {min(self.__lista)}")
      
    def mostraMaior(self):
        print(f"Maior: {max(self.__lista)}") 
       
    def listarEmOrdem(self):
        print(f"Lista ordenada: {sorted(self.__lista)}")
        
    def __str__(self):
        return f'Objeto da classe ListaIdades com lista: {self.__lista}'

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    # listaListas = [nomes, datas, salarios, idades]

    # for lista in listaListas:
    #     lista.entradaDeDados()
    #     lista.mostraMediana()
    #     lista.mostraMenor()
    #     lista.mostraMaior()
    #     lista.listarEmOrdem()
    #     print(lista)
    #     print("___________________")

    # nomes.mostraNomeESalario(salarios.getLista())
    # print("___________________")
    # salarios.calculaFolhaReajuste()
    # print("___________________")
    # datas.modificaDatas()
    # print("___________________")
    
    # print("\nFim do teste!!!")

    while True:
        print("\n=== Menu de opções ===")
        print ("1. Incluir um nome na lista de nomes.")
        print ("2. Incluir um salário na lista de salários.")
        print ("3. Incluir uma data na lista de datas.")
        print ("4. Incluir uma idade na lista de idades.")
        print ("5. Percorrer as listas de nomes e salários.")
        print ("6. Calcular o valor da folha com um reajuste de 10%.")
        print ("7. Modificar o dia das datas anteriores a 2019.")
        print ("8. Sair.")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nomes.entradaDeDados()
        elif opcao == "2":
            salarios.entradaDeDados()
        elif opcao == "3":
            datas.entradaDeDados()
        elif opcao == "4":
            idades.entradaDeDados()
        elif opcao == "5":
            nomes.mostraNomesESalarios()
        elif opcao == "6":
            salarios.calcularCustoFolha()
        elif opcao == "7":
            datas.modificarDatas()
        elif opcao == "8":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()
