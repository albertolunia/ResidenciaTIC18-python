# Lista dos animais do zodíaco chinês
zodiaco_chines = ['Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Cabra', 'Macaco', 'Galo', 'Cão', 'Porco']

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Calcula o índice do animal do zodíaco chinês
indice = ano_nascimento  % 12

# Imprime o animal do zodíaco chinês do usuário
print("Seu signo no zodíaco chinês é: " + zodiaco_chines[indice])
