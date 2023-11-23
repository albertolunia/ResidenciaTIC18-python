# Importando o módulo necessário
import math

# Operadores aritméticos e aritméticos compostos
a = 10
b = 3
print("Operadores aritméticos:")
print(a + b)  # Adição
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a / b)  # Divisão (Em C++, a divisão de inteiros resulta em um inteiro)
print(a // b) # Divisão inteira
print(a % b)  # Módulo
print(a ** b) # Exponenciação (Não disponível em C++)

print("\nOperadores aritméticos compostos:")
a += b  # Equivalente a a = a + b
print(a)
a -= b  # Equivalente a a = a - b
print(a)
a *= b  # Equivalente a a = a * b
print(a)
a /= b  # Equivalente a a = a / b (Em C++, a divisão de inteiros resulta em um inteiro)
print(a)
a //= b # Equivalente a a = a // b
print(a)
a %= b  # Equivalente a a = a % b
print(a)
a **= b # Equivalente a a = a ** b (Não disponível em C++)
print(a)

# Números inteiros significativamente grandes
print("\nFatorial de 30:")
print(math.factorial(30))  # Calcula o fatorial de 30 (Em C++, inteiros têm um limite máximo)

# Imutabilidade das variáveis numéricas
print("\nImutabilidade das variáveis numéricas:")
a = 10
print(id(a))  # Imprime o identificador de 'a'
a += 1
print(id(a))  # Imprime o novo identificador de 'a' (Em C++, o valor de uma variável pode ser alterado sem criar uma nova instância)

# Métodos disponíveis para variáveis inteiras
print("\nMétodos disponíveis para variáveis inteiras:")
print(dir(int))  # Em C++, os inteiros são tipos primitivos e não têm métodos associados
