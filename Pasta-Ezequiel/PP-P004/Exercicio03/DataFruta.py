
from lista_Nomes import ListaNomes
from lista_Datas import ListaDatas
from lista_Salarios import ListaSalarios
from lista_Idades import ListaIdades
from data import Data  


def mostrarNomesESalarios(lista_nomes, lista_salarios):
        print("Nomes e Salários:")
        for nome, salario in zip(lista_nomes, lista_salarios):
            print(f"{nome}: {salario}")
            
def calcularCustoFolhaPagamento(lista_salarios):
        print("Custo da Folha de Pagamento com 10% de Reajuste:")
        salarios_reajustados = map(lambda x: x * 1.1, lista_salarios)
        for salario in salarios_reajustados:
            print("{:.2f}".format(salario))
            
def ajustarDatasAnteriores2019(lista_datas):
        print("Datas Ajustadas para o Primeiro Dia do Mês (Anteriores a 2019):")
        datas_ajustadas = filter(lambda x: x.ano < 2019, lista_datas)
        for data in datas_ajustadas:
            data.dia = 1
            print(data)

def main():
    tipo_nome = type("String")
    tipo_data = type(Data)
    tipo_salario = type(float)
    tipo_idade = type(int)

    nomes = ListaNomes(tipo_nome)
    datas = ListaDatas(tipo_data)
    salarios = ListaSalarios(tipo_salario)
    idades = ListaIdades(tipo_idade)

    while True:
        print("\nSelecione uma opção:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nomes.entradaDeDados()
        elif opcao == "2":
            salarios.entradaDeDados()
        elif opcao == "3":
            datas.entradaDeDados()
        elif opcao == "4":
            idades.entradaDeDados()
        elif opcao == "5":
            mostrarNomesESalarios(nomes, salarios)
        elif opcao == "6":
            calcularCustoFolhaPagamento(salarios)
        elif opcao == "7":
            ajustarDatasAnteriores2019(datas)
        elif opcao == "8":
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
