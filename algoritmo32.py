# Ler um número inteiro e imprimi-lo.
import streamlit as st

numero_int = st.number_input("Digite um número inteiro:  ")
st.write("o numero é:", numero_int)