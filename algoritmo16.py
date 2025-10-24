import streamlit as st

mercado = ['ações','Opções','Futuro','Dolar','Ouro','Criptomoedas']
st.write(mercado)

mercado[0:2] = ['tesouro', 'títulos']

st.write(mercado)