import sys

# Operadores aritméticos e aritméticos compostos
a = 10.0
b = 3.0
print("Operadores aritméticos:")
print(a + b)  # Adição
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a / b)  # Divisão
print(a ** b) # Exponenciação

print("\nOperadores aritméticos compostos:")
a += b  # Equivalente a a = a + b
print(a)
a -= b  # Equivalente a a = a - b
print(a)
a *= b  # Equivalente a a = a * b
print(a)
a /= b  # Equivalente a a = a / b
print(a)
a **= b # Equivalente a a = a ** b
print(a)

# Maior e menor potência de 2 que pode ser representada com variáveis de ponto flutuante
print("\nMaior e menor potência de 2:")
max_exp = sys.float_info.max_exp
if max_exp < 1024:  # 1024 é um valor seguro para a maioria dos sistemas
    print(2.0 ** max_exp)  # Maior potência de 2
else:
    print("O expoente é muito grande para calcular a potência.")
print(2.0 ** sys.float_info.min_exp)  # Menor potência de 2

# Imutabilidade das variáveis numéricas
print("\nImutabilidade das variáveis numéricas:")
a = 10.0
print(id(a))  # Imprime o identificador de 'a'
a += 1.0
print(id(a))  # Imprime o novo identificador de 'a'

# Métodos disponíveis para variáveis de ponto flutuante
print("\nMétodos disponíveis para variáveis de ponto flutuante:")
print(dir(float))
