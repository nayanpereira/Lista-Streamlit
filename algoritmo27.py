Ibov = ["PETR4", "BBAS3", 'USIMS', "GGBR4", "VALE3"]

# Elementos do índice 2 ao 3
print(Ibov[2:4])

# Elemento do índice 1 até o último
print(Ibov[1:])

# Do elemento inicial (índice 0) ao elemento de índice 2
print(Ibov[:3])

# Do elemento inicial ao último, saltando de dois em dois
print(Ibov[0:5:2]) # ou print(Ibov[::2])

# Selecionar os três últimos elementos
print(Ibov[-3:])

# Selecionar todos, exceto os três últimos (no vídeo, "os dois primeiros")
print(Ibov[:-3])