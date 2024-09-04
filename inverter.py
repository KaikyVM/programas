# Função para inverter uma string
def inverter(s):
    # Convertemos a string para uma lista para facilitar a manipulação
    lista_caracteres = list(s)
    # Inicializamos os índices para o início e o fim da lista
    inicio = 0
    fim = len(lista_caracteres) - 1

    # Troca os caracteres do início com os do fim até o meio da lista
    while inicio < fim:
        # Troca os caracteres
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        # Move os índices em direção ao centro
        inicio += 1
        fim -= 1

    # Convertemos a lista de volta para uma string
    return ''.join(lista_caracteres)

# Entrada da string
entrada = input("Digite uma string para inverter: ")


resultado = inverter(entrada)
print(f"String invertida: {resultado}")
