#Enunciado: Imprimir seu nome
import streamlit as st

# Solicita o nome do usuário
nome = st.text_input("Digite seu nome:")

# Mostra o nome digitado
if nome:  # só mostra se o usuário digitou algo
    st.write("Seu nome é:", nome)