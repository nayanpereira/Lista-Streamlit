import streamlit as st
mercado = ["Ações", "Opções", "Futuro", "Dolar", "Ouro", "Criptomoedas"]
st.write(mercado)

mercado.extend(['Petrobras','BB','Vale'])

st.write(mercado)