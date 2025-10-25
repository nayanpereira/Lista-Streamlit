import streamlit as st

st.title("💈 Sistema de Barbearia (versão simples)")

# Lista de clientes (guardada em sessão, para não sumir ao clicar)
if "clientes" not in st.session_state:
    st.session_state.clientes = []

clientes = st.session_state.clientes

# Menu principal — simulando o menu de opções
opcao = st.selectbox(
    "Escolha uma opção:",
    [
        "1 - Agendar cliente no final da fila (CREATE)",
        "2 - Visualizar Agendamentos (READ)",
        "3 - Atualizar Agendamento (UPDATE)",
        "4 - Cancelar Agendamento (DELETE)",
        "5 - Inserir cliente em posição específica (insert)",
        "6 - Ordenar agendamentos (A-Z) (sort)",
        "7 - Inverter ordem dos agendamentos (reverse)",
        "8 - Sair",
    ],
)

st.write("---")

# Match case simplificado usando if/elif
if "Sair" in opcao:
    st.success("Saindo do sistema... (basta fechar a aba)")
elif "Agendar" in opcao:
    nome = st.text_input("Digite o nome do cliente para agendar:")
    if st.button("Salvar agendamento"):
        if nome:
            clientes.append(nome)
            st.success(f"Cliente '{nome}' agendado com sucesso!")
        else:
            st.warning("Por favor, digite um nome.")
elif "Visualizar" in opcao:
    if not clientes:
        st.info("Nenhum agendamento cadastrado.")
    else:
        st.subheader("📋 Lista de Agendamentos")
        for i, cliente in enumerate(clientes, 1):
            st.write(f"{i}. {cliente}")
elif "Atualizar" in opcao:
    if not clientes:
        st.info("Nenhum agendamento para atualizar.")
    else:
        nome_antigo = st.selectbox("Selecione o cliente:", clientes)
        nome_novo = st.text_input("Digite o novo nome:")
        if st.button("Atualizar"):
            index = clientes.index(nome_antigo)
            clientes[index] = nome_novo
            st.success(f"'{nome_antigo}' atualizado para '{nome_novo}'.")
elif "Cancelar" in opcao:
    if not clientes:
        st.info("Nenhum agendamento para cancelar.")
    else:
        nome_remover = st.selectbox("Selecione o cliente:", clientes)
        if st.button("Cancelar agendamento"):
            clientes.remove(nome_remover)
            st.success(f"Agendamento de '{nome_remover}' cancelado.")
elif "Inserir" in opcao:
    nome = st.text_input("Digite o nome do cliente:")
    pos = st.number_input(
        f"Digite a posição (0 até {len(clientes)}):",
        min_value=0,
        max_value=len(clientes),
        step=1,
    )
    if st.button("Inserir cliente"):
        clientes.insert(pos, nome)
        st.success(f"Cliente '{nome}' inserido na posição {pos}.")
elif "Ordenar" in opcao:
    if clientes:
        clientes.sort()
        st.success("Agendamentos ordenados de A-Z!")
    else:
        st.info("Lista vazia.")
elif "Inverter" in opcao:
    if clientes:
        clientes.reverse()
        st.success("Ordem dos agendamentos invertida.")
    else:
        st.info("Lista vazia.")

st.write("---")
st.caption("Versão simplificada do sistema de barbearia — feita com Streamlit.")
