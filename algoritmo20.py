# Lista de exemplo com letras maiúsculas e minúsculas
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptomoedas"]

print(mercado)

# Ordenar a lista ignorando o case
mercado.sort(key=str.casefold) 

# Imprimir a lista ordenada
print(mercado)