# Declare uma variável nome atribuindo a ela seu nome completo
nome_completo = "Ana Maria Braga"

# Separe em duas variáveis novas seu nome do seu sobrenome
nome, sobrenome = nome_completo.split()

# Verifique qual das duas novas variáveis antecede a outra na ordem alfabética
if nome < sobrenome:
    print(f"{nome} vem antes de {sobrenome} na ordem alfabética.")
else:
    print(f"{sobrenome} vem antes de {nome} na ordem alfabética.")

# Verifique a quantidade de caracteres de cada uma das novas variáveis
print(f"O nome {nome} tem {len(nome)} caracteres.")
print(f"O sobrenome {sobrenome} tem {len(sobrenome)} caracteres.")

# Verifique se seu nome é um palíndromo
nome_invertido = nome[::-1]
if nome == nome_invertido:
    print(f"O nome {nome} é um palíndromo.")
else:
    print(f"O nome {nome} não é um palíndromo.")
