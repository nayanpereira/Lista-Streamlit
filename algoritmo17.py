import streamlit as st

# Use a função count() para quantas vezes apareu dolar
mercado = ["Ações", "Opções", "Futuro", "Dolar", "Ouro", "Criptomoedas"]
mercado.append('Dolar')

st.write(mercado)
st.write(f'A quantidade de ocorrência do Dolar na lista é : {mercado.count('Dolar')}')