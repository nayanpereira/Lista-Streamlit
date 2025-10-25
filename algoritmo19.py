import streamlit as st
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptomoedas"]

# Imprimir a lista original
st.write(mercado)

# Ordenar a lista em ordem crescente
mercado.sort()

# Imprimir a lista ordenada
st.write(mercado)