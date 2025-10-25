# Ler dois números inteiros e imprimi-los.
import streamlit as st

numero_1 = st.number_input("Digite o primeiro número inteiro:  ")
numero_2 = st.number_input("Digite o segundo número inteiro:  ")
st.write("os números são:", numero_1,"e",numero_2)