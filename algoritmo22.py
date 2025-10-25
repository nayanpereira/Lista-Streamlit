import streamlit as st
mercado = ["ações", "opções", "futuro", "dólar", "ouro", "criptomoedas"]

st.write(mercado)
# Remover o item "ouro" da lista
# É importante notar que o item deve ser escrito exatamente
mercado.remove("ouro")

# Imprimir a lista modificada
st.write(mercado)