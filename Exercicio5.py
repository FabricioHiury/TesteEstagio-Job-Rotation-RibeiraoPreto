string = input("Digite uma string: ")
tamanho = len(string)

# Criando uma lista com os caracteres da string
lista = []
for i in range(tamanho):
    lista.append(string[i])

# Invertendo a ordem dos caracteres
for i in range(tamanho // 2):
    lista[i], lista[tamanho - i - 1] = lista[tamanho - i - 1], lista[i]

# Criando a string invertida
string_invertida = ""
for i in range(tamanho):
    string_invertida += lista[i]

print("A string invertida é:", string_invertida)