#Criar um algoritmo que imprima a média aritmética entre os números 
import streamlit as st

numero1 = st.number_input("Digite o primeiro número: ")
numero2 = st.number_input("Digite o segundo número: ")
media = (numero1 + numero2) / 2

st.write(f"A média entre {numero1} e {numero2} é: {media}")

