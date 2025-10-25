import streamlit as st
# Lista de exemplo usada no vídeo
mercado = ['ações', 'opções', 'futuro', 'Dolar', 'Ouro', 'Criprtomoedas']
st.write(mercado)

# Inserir "fundo de investimento" no índice 2
mercado.insert(2, "fundo de investimento")

# Imprimir a lista modificada
st.write(mercado)