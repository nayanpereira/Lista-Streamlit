import streamlit as st

# Lista de ações do índice Ibovespa
Ibov = ["PETR4", "BBAS3", "USIM5", "GGBR4", "VALE3"]

# Mostra a lista completa
st.write("Lista completa:", Ibov)

# Elementos do índice 2 ao 3
st.write("Elementos de índice 2 a 3:", Ibov[2:4])

# Elemento do índice 1 até o último
st.write("Do índice 1 até o último:", Ibov[1:])

# Do elemento inicial (índice 0) ao elemento de índice 2
st.write("Do início até o índice 2:", Ibov[:3])

# Do elemento inicial ao último, saltando de dois em dois
st.write("Pulando de dois em dois:", Ibov[0:5:2])  # ou Ibov[::2]

# Selecionar os três últimos elementos
st.write("Três últimos elementos:", Ibov[-3:])

# Selecionar todos, exceto os três últimos
st.write("Todos, exceto os três últimos:", Ibov[:-3])
