import streamlit as st
# Lista de exemplo
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptomoedas"]

# --- Parte 1: Simplesmente inverter a lista ---
mercado.reverse() 
st.write(mercado)

# --- Parte 2: Ordenar de forma decrescente (reversa) ---
# O vídeo mostra a ordenação reversa ignorando o case,

# para o exemplo de casefold)
mercado = ["Ações", "opções", "futuro", "dólar", "ouro", "Criptomoedas"]

lista_reversa_insensitive = sorted(mercado, key=str.casefold, reverse=True)

st.write(lista_reversa_insensitive)