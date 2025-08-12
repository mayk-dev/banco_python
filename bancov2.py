from datetime import datetime
import random

# Função para gerar um número de conta aleatório
def gerar_numero_conta():
    return random.randint(100000, 999999)

# Função de cadastro de usuário
def cadastrar_usuario():
    nome_usuario = input("Digite seu nome: ")
    numero_conta = gerar_numero_conta()
    agencia = "0001"  # Número da agência fixo
    print(f"\nCadastro realizado com sucesso!\nNome: {nome_usuario}\nNúmero da conta: {numero_conta}\nAgência: {agencia}\n")
    return nome_usuario, numero_conta, agencia

# Função de menu
def exibir_menu():
    return input("""
 _________________________________
|                                 |    
|      BEM VINDO AO MAYKBANK      |
|_________________________________|
|------DIGITE [S] PARA SACAR      |
|                                 |    
|------DIGITE [D] PARA DEPOSITO   |
|                                 |    
|------DIGITE [E] PARA VER EXTRATO|
|                                 |    
|------DIGITE [Q] PARA SAIR       |
|                                 |    
|----DIGITE [C] PARA CADASTRO ----|
|          DE USUARIO             |   
|_________________________________|  
|                                 |    
|      digite a opção desejada    |
|_________________________________|              
""")

# Função principal para o banco
def banco():
    saldo = 1512.00
    limite_diario = 500.00
    saques_feitos = 0
    LIMITE_SAQUE_DIARIO = 3
    extrato = []  # Lista para armazenar as transações
    data = datetime.now()
    data_extrato = data.strftime("%d/%m/%Y %H:%M:%S")

    nome_usuario, numero_conta, agencia = cadastrar_usuario()

    while True:
        opcao = exibir_menu().lower()

        if opcao == "d":
            valor = float(input("Informe valor que deseja depositar ou digite 0 para cancelar operação: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")  # Adiciona o depósito no extrato
                print(f"Depósito feito com sucesso! Seu novo saldo é de R$ {saldo:.2f}")
            elif valor == 0:
                print("Operação cancelada.")

        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor <= 0:
                print("Valor inválido. Tente novamente.")
            elif valor > saldo:
                print("Saldo insuficiente para realizar a operação.")
            elif saques_feitos >= LIMITE_SAQUE_DIARIO:
                print("Limite de saques diário excedido. Operação indisponível até as 23:59.")
                break
            elif valor > limite_diario:
                print("Esse valor excede o seu limite de saque diário.")
            else:
                saldo -= valor
                limite_diario -= valor
                saques_feitos += 1
                extrato.append(f"Saque: R$ {valor:.2f}")  # Adiciona o saque no extrato
                print(f"Saque de R$ {valor:.2f} realizado com sucesso! Seu novo saldo é de R$ {saldo:.2f}.")
                print(f"Limite diário restante: R$ {limite_diario:.2f}. Saques feitos hoje: {saques_feitos}/{LIMITE_SAQUE_DIARIO}.")

        elif opcao == "e":
            # Exibe extrato bancário completo
            print(f"""
            ===========================================
                     EXTRATO BANCÁRIO
            ===========================================
            Nome: {nome_usuario}
            Número da Conta: {numero_conta}
            Agência: {agencia}
            Saldo atual: R$ {saldo:.2f}    Data: {data_extrato}
            
            {'\n'.join(extrato) if extrato else "Nenhuma movimentação encontrada."}
            
            ===========================================
            """)

        elif opcao == "q":
            print("Saindo... Até logo!")
            break
        elif opcao == "c":
            nome_usuario, numero_conta, agencia = cadastrar_usuario()  # Permite cadastrar um novo usuário
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função do banco
banco()
