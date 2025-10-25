# Ler um número inteiro e imprimir seu sucessor e seu antecessor.
import streamlit as st

numero = st.number_input("Digite um  número inteiro:  ")
sucessor = numero + 1 
antecessor = numero - 1
st.write(f"o sucessor é {sucessor} e o antecessor é {antecessor}")