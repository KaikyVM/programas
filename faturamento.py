import json

# Carregando os dados JSON
with open('faturamento.json') as f:
    dados = json.load(f)

# Filtrando os dias com faturamento maior que zero
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calculando o menor e maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calculando a média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Contando os dias em que o faturamento foi superior à média
dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
