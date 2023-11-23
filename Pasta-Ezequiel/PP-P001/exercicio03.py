# Imprime cada caractere numérico e seu código numérico correspondente
print("Caracteres numéricos e seus códigos numéricos:")
for i in range(10):
    print(f"'{i}' - {ord(str(i))} (decimal), {oct(ord(str(i)))} (octal), {hex(ord(str(i)))} (hexadecimal)")

# Lê um caractere da entrada padrão
char = input("\nDigite um caractere: ")
print(f"'{char}' - {ord(char)} (decimal), {oct(ord(char))} (octal), {hex(ord(char))} (hexadecimal)")

# Trabalha com caracteres especiais
print("\nCaracteres especiais:")
special_chars = ['ç', 'ã']
for char in special_chars:
    print(f"'{char}' - {ord(char)} (decimal), {oct(ord(char))} (octal), {hex(ord(char))} (hexadecimal)")
