def fibonacci(n):
    """Gera a sequência de Fibonacci até que o último número seja maior ou igual a n."""
    sequencia = [0, 1]
    while sequencia[-1] < n:
        prox_num = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_num)
    return sequencia

def pertence_a_fibonacci(num):
    """Verifica se um número pertence à sequência de Fibonacci."""
    if num < 0:
        return False
    sequencia = fibonacci(num)
    return num in sequencia

# Exemplo de uso
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
