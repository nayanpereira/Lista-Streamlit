# Ler dois números inteiros e imprimir a soma. Antes do resultado, deverá aparecer a mensagem: Soma
import streamlit as st

numero1 = st.number_input("Digite um número inteiro: ")
numero2 = st.number_input("Digite um segundo inteiro: ")
soma = numero1 + numero2


st.write(f"Soma: {soma}")