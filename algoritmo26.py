# Criar um menu de opções 
#match case

"""
append() : Adiconar um elemento na lista
clear() : Limpar a lista
count() : conta quantos elementos
extend() : retorna o valor do indece

insert() : 
Reverse() :
sort ()
... entre outras 
"""
# estrutura de condição ou seleção
# if 
# if else
# if elif else 
# match case

'''
Create() : Criar
Read() : Ler/visualizar
Update: Atualizar/editar
Delete (Excluir/Deletar)
'''
import os

print ("Sistema de Barbearia")
print (" ")
clientes = []

cont = True
while cont == True:
    print("\n--- Sistema de Gerenciamento de Barbearia ---")
    print("1. Agendar cliente no final da fila (CREATE - append)")
    print("2. Visualizar Agendamentos (READ)")
    print("3. Atualizar Agendamento (UPDATE)")
    print("4. Cancelar Agendamento (DELETE)")
    print("-----------------------------------------------")
    print("5. Inserir cliente em posição específica (insert)")
    print("6. Ordenar agendamentos (A-Z) (sort)")
    print("7. Inverter ordem dos agendamentos (reverse)")
    print("-----------------------------------------------")
    print("8. Sair")

    opcao = 0 
    try:
        opcao = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("Erro: Por favor, digite apenas um número.")
        continue 

    # 
    # É AQUI QUE O 'MATCH CASE' COMEÇA
    # 
    match opcao: # 'match' é o 'switch'
        
        case 1: # 'case' é o 'case'
            nome = input("Digite o nome do cliente: ")
            clientes.append(nome)
            print(f"Cliente '{nome}' agendado com sucesso no FIM da fila.")

        case 2: # READ
            if not clientes: 
                print("Nenhum agendamento cadastrado.")
            else:
                print("\n--- Lista de Agendamentos ---")
                for i, cliente in enumerate(clientes, 1):
                    print(f"{i}. {cliente}")

        case 3: # UPDATE
            if not clientes:
                print("Nenhum agendamento para atualizar.")
            else:
                nome_antigo = input("Digite o nome do cliente que deseja ATUALIZAR: ")
                if nome_antigo in clientes:
                    index = clientes.index(nome_antigo) 
                    nome_novo = input(f"Digite o novo nome para '{nome_antigo}': ")
                    clientes[index] = nome_novo
                    print("Agendamento atualizado com sucesso!")
                else:
                    print(f"Cliente '{nome_antigo}' não encontrado na lista.")

        case 4: # DELETE
            if not clientes:
                print("Nenhum agendamento para cancelar.")
            else:
                nome_remover = input("Digite o nome do cliente que deseja CANCELAR: ")
                if nome_remover in clientes:
                    clientes.remove(nome_remover)
                    print(f"Agendamento de '{nome_remover}' cancelado com sucesso.")
                else:
                    print(f"Cliente '{nome_remover}' não encontrado na lista.")

        case 5: # Usando insert()
            print("--- Inserir em Posição Específica ---")
            if not clientes:
                posicao = 0
            else:
                print(f"Posições disponíveis: 0 (início) até {len(clientes)} (final).")
                try:
                    posicao = int(input("Digite a posição (índice) onde deseja inserir: "))
                    if posicao < 0 or posicao > len(clientes):
                         posicao = len(clientes) 
                except ValueError:
                    posicao = len(clientes)
            
            nome = input("Digite o nome do cliente a inserir: ")
            clientes.insert(posicao, nome)
            print(f"Cliente '{nome}' inserido na posição {posicao}.")

        case 6: # Usando sort()
            if not clientes:
                print("Lista vazia, nada para ordenar.")
            else:
                clientes.sort()
                print("Agendamentos ordenados de A-Z com sucesso.")

        case 7: # Usando reverse()
            if not clientes:
                print("Lista vazia, nada para inverter.")
            else:
                clientes.reverse()
                print("Ordem dos agendamentos foi invertida com sucesso.")
        
        case 8: # Sair
            print("Saindo do sistema...")
            cont = False 

        case _: # 'case _' é o 'default' (caso padrão)
            print("Opção inválida! Por favor, escolha um número do menu.")

    # Pausa para o usuário ler a saída antes de limpar
    if cont == True:
        input("\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa o console

print("Sistema de Barbearia finalizado.")