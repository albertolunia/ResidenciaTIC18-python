
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
        print("\n"+lista.__class__.__name__+":")
        print(f"Mediana: {lista.calcularMediana()}")
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

        
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
            
if __name__ == "__main__":
    main()
    datas = ListaDatas(Data)
    datas.entradaDeDados()
    ajustarDatasAnteriores2019(datas)
  
    salarios = ListaSalarios(float)
    salarios.entradaDeDados()
    calcularCustoFolhaPagamento(salarios)
    

    nomes = ListaNomes(str)
    nomes.entradaDeDados()
    salarios = ListaSalarios(float)
    salarios.entradaDeDados()
    mostrarNomesESalarios(nomes, salarios)

   