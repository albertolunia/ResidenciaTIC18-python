
from lista_Nomes import ListaNomes
from lista_Datas import ListaDatas
from lista_Salarios import ListaSalarios
from lista_Idades import ListaIdades
from data import Data  

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
