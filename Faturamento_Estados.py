# Valores dos estados
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

# Calcula o valor total
total = sp + rj + mg + es + outros

# Calcula o percentual de representação de cada estado
sp_percent = (sp / total) * 100
rj_percent = (rj / total) * 100
mg_percent = (mg / total) * 100
es_percent = (es / total) * 100
outros_percent = (outros / total) * 100

# Exibe os resultados
print(f"SP: {sp_percent:.2f}%")
print(f"RJ: {rj_percent:.2f}%")
print(f"MG: {mg_percent:.2f}%")
print(f"ES: {es_percent:.2f}%")
print(f"Outros: {outros_percent:.2f}%")
