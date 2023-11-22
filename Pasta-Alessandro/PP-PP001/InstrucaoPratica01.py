import math
import sys

""" 
Exercício 2 ->  Manipulação de variáveis de tipo inteiro, explorando as características
e os limites.
"""
print('>>> Exercicio 2')
print('Operadores Aritmeticos Basicos')

#Adição
a = 5
b = 3
result = a + b
print(result)

#Subtração
a = 5
b = 3
result = a - b
print(result)

#Multiplicação
a = 5
b = 3
result = a * b
print(result)

#Divisão
a = 5
b = 3
result = a / b  # Em Python 3, a divisão de inteiros resulta em um número de ponto flutuante.
print(result)

#Divisão inteira
a = 5
b = 3
result = a // b  # Retorna a parte inteira da divisão.
print(result)

#Resto da divisão
a = 5
b = 3
result = a % b
print(result)

#Potência
a = 2
b = 3
result = a ** b  # 2 elevado à potência de 3.
print(result)


print('Operadores Aritmeticos Compostos')
#Adição e Atribuição: +=
a = 5
a += 3  # Equivalente a: a = a + 3
print(a)

#Subtração e Atribuição: -=
a = 5
a -= 3  # Equivalente a: a = a - 3
print(a)

#Multiplicação e Atribuição: *=
a = 5
a *= 3  # Equivalente a: a = a * 3
print(a)

#Divisão e Atribuição: /=
a = 5
a /= 3  # Equivalente a: a = a / 3
print(a)

#Divisão Inteira e Atribuição: //=
a = 5
a //= 3  # Equivalente a: a = a // 3
print(a)

#Resto da Divisão e Atribuição: %=
a = 5
a %= 3  # Equivalente a: a = a % 3
print(a)

#Potência e Atribuição: **=
a = 2
a **= 3  # Equivalente a: a = a ** 3
print(a)

""" 
Diferenças e Novidades em Relação a C/C++

Divisão de Inteiros:
Em Python 3, a divisão de dois inteiros resulta em um número de ponto flutuante, 
a menos que o operador // seja usado para realizar a divisão inteira.

Sem Overflow:
Python lida automaticamente com overflow de inteiros, permitindo que você realize 
operações aritméticas sem se preocupar com estouro de tamanho de variável.

Dinamicamente Tipado:
Python é dinamicamente tipado, o que significa que você não precisa declarar o tipo 
de variável antes de usá-la. Isso contrasta com C/C++, onde você precisa declarar o tipo explicitamente.

Operadores Compostos:
Python oferece operadores compostos (como +=, -=, etc.), que são uma maneira concisa 
de realizar uma operação e atribuir o resultado à mesma variável.

"""

# Calcular o fatorial de 30 em Python
fatorial_30 = math.factorial(30)

print(f"Fatorial de 30 em Python: {fatorial_30}")

print('Variaveis imutaveis')
# Atribuição de valor a uma variável inteira
numero = 5
numero = numero + 3
print(numero)

# Atribuição de valor a uma variável de ponto flutuante
numero_real = 3.14
numero_real = numero_real * 2
print(numero_real)

#Verificando os metodos disponiveis para variaveis inteiras
x = 10
print(dir(x))

print('=====================================')


""" 
Exercício 3 ->  Manipulação de variáveis de tipo string e explorando o uso de print.
"""
print('>>> Exercicio 3')
print('Manipulacao de strings')
# Modificar o comportamento do print para imprimir caractere e código numérico na mesma linha
for i in range(10):
    print(f"Caractere: {chr(ord('0') + i)}, Codigo Numerico: {ord('0') + i}")
print()


# Modificar o comportamento do print para imprimir caractere, código numérico, octal e hexadecimal
for i in range(10):
    print(f"Caractere: {i}, Código Numérico: {i}, Octal: {oct(i)}, Hexadecimal: {hex(i)}")
print()

print("Digite um valor:")
i = input()
print(f"'{i}': {ord(i)} : {oct(ord(i))} : {hex(ord(i))}")

print()

print(">>> Mostrando caracteres especiais")
print(f"Valor de 'ç' na tabela ascii: {ord('ç')}")
print(f"Valor de 'ã' na tabela ascii: {ord('ã')}")

print("Digite um valor:")
i = input()
print(f"'{i}': {ord(i)} : {oct(ord(i))} : {hex(ord(i))}")

print('=====================================')

""" 
Exercício 4 ->   Manipulação de variáveis de tipo string e explorando os métodos da
classe.

"""
print('>>> Exercicio 4')
print(' Manipulação de variáveis de tipo string e explorando os métodos da classe.')

nome = "Alessandro Conceição Santos"
nome, sobrenome = nome.split(' ')[0:2]
print(nome)
print(sobrenome)

if nome[0] < sobrenome[0]:
    print(f"Nome antecede Sobrenome")
else:
    print(f"Sobrenome antecede Nome")

print(f"Quantidade de caracteres em nome: {len(nome)}")
print(f"Quantidade de caracteres em sobrenome: {len(sobrenome)}")

nome = nome.upper()
if nome == nome[::-1]:
    print("O nome é um palíndromo")
else:
    print("O nome não é um palíndromo")

print('=====================================')
""" 
Exercício 5->   Manipulação de variáveis de ponto flutuante, explorando as
características e os limites.
"""
print('>>> Exercicio 5')
print(' Manipulação de variáveis de ponto flutuante, explorando as características e os limites.')

# Operadores aritméticos em Python
a = 10.5
b = 3.7

print(f"Adição: {a + b}") 
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão: {a / b}")
print(f"Divisão inteira: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potência: {a ** b}")

# Operadores aritméticos compostos
a += b
print(f"A += B: {a}")

a -= b
print(f"A -= B: {a}")

a *= b
print(f"A *= B: {a}")

a /= b
print(f"A /= B: {a}")

a //= b
print(f"A //= B: {a}")

a %= b
print(f"A %= B: {a}") 

a **= b
print(f"A **= B: {a}")

print(f"Maior potencia de 2: {2 ** sys.float_info.max_exp}")
print(f"Menor potencia de 2: {2 ** sys.float_info.min_exp}")

print('Variaveis imutaveis')
a = 10.5
b = a
print(f"Antes da operação: a={a}, b={b}")

a += 5.4
print(f"Depois da operação: a={a}, b={b}")

a = 10.5
print(f"{dir(a)}")
print('=====================================')

""" 
Exercício 5-> Manipulando listas
"""
print('>>> Exercicio 6')
print(' Manipulando listas ')

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[::-1])
print(L[-1::])
print(L[:-1:])
print(L[::-2])
print(L[-2::])
print(L[:-2:])

print("Insira seu ano de nascimento:")
ano = int(input())
print(f"Seu signo chinês é: ", end="")

match (ano % 12):
    case 0:
        print("Macaco")
    case 1:
        print("Galo")
    case 2:
        print("Cão")
    case 3:
        print("Porco")
    case 4:
        print("Rato")
    case 5:
        print("Boi")
    case 6:
        print("Tigre")
    case 7:
        print("Coelho")
    case 8:
        print("Dragão")
    case 9:
        print("Serpente")
    case 10:
        print("Cavalo")
    case 11:
        print("Carneiro")
    case _:
        print("Valor inválido")


print('=====================================')