def verificar_letra_a(s):
    """Verifica a letra 'a' quantas vezes ela ocorre."""
    # Convertendo a string para minúsculas para facilitar a contagem
    s = s.lower()
    # Contando a ocorrência da letra 'a'
    contagem = s.count('a')
    
    if contagem > 0:
        print(f"A letra 'a' ocorre {contagem} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Exemplo de uso com entrada do usuário
string = input("Digite uma string para verificar a ocorrência da letra 'a': ")
verificar_letra_a(string)
