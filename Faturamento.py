import json

# carrega os dados do faturamento mensal a partir do arquivo json
with open('dados.json', 'r') as f:
    faturamento = json.load(f)

# calcular o menor valor de faturamento
menor_valor = min(faturamento)
print(f'Menor valor de faturamento: {Menor_valor}')

# calcular o maior valor de faturamento
maior_valor = max(faturamento)
print(f'Maior valor de faturamento: {maior_valor}')

# calcular a média mensal de faturamento
soma_faturamento = sum(faturamento)
dias_com_faturamento = len([x for x in faturamento if x > 0])  # ignorar dias sem faturamento
media_mensal = soma_faturamento / dias_com_faturamento
print(f'Média mensal de faturamento: {media_mensal}')

# calcular o número de dias em que o faturamento foi superior à média mensal
dias_acima_media = len([x for x in faturamento if x > media_mensal])
print(f'Número de dias com faturamento acima da média: {dias_acima_media}')
