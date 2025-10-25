# Ler nome, endereço e telefone e imprimi-los.
import streamlit as st

nome = st.text_input("Digite seu nome: ")
endereco = st.text_input("Digite seu endereço: ")
telefone = st.text_input("Digite seu telefone: ")

st.write("\n--- Seus Dados ---")
st.write(f"Nome: {nome}")
st.write(f"Endereço: {endereco}")
st.write(f"Telefone: {telefone}")