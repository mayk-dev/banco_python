from datetime import datetime



menu = input("""
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
|_________________________________|  
|                                 |
|      digte a opção desejada     |
|_________________________________|              
""")


saldo = 1512.00
limite_diario = 500.00
saques_feitos = 0
LIMITE_SAQUE_DIARIO = 3
extrato = ""
data = datetime.now()
data_extrato = data.strftime("%d/%m/%Y %H:%M:%S")
while True :

    opcao = (menu)

    if opcao == "d":
        
        valor = float(input("informe valor que deseja depositar ou digite 0 para cancelar operação: "))
        if valor > 0:
            saldo += valor
            print(f"""
            Deposito Feito com Sucesso seus novo saldo é de R$ {saldo:.2f}
                """)
            extrato += f"Deposito R$ {valor:.2f} "
        elif valor <= 0:
            break

    elif opcao == "s":
        valor = float(input("digite o valor que Deseja Sacar: "))
        if valor <= 0:
            print("valor invalido")
        elif saldo - valor >= 0:
            saldo -= valor
            limite_diario -= valor
            saques_feitos += 1
            print(f"""
                  Saque de R$ {valor:.2f} Realizado com Sucesso seu novo saldo é de R$ {saldo:.2f}
                  
                  Seu Limite de Saque diario é 3 foram feitos {saques_feitos} saques hoje.

                  e Seu limite diario em reais Restante é R$ {limite_diario:.2f}
                  
 
                   """)
            if saques_feitos == 3:
                print("limite de saque excedido operação indisponivel até as 23:59 de hoje")
                break

        if saldo - valor < limite_diario:
                print("esse valor excede seu total de  limite de saque diario ")



        elif saldo - valor <= 0:
                print("Saldo insuficiente para realizar operação")




    elif opcao == "e":
         print(f"""                   ===========================================
                  |              EXTRATO BANCARIO             |  
                   ===========================================
                  |Saldo {saldo:.2f}     data: {data_extrato:}|
                   
                  |Saques    : Nenhuma Movimentação Encontrada|

                  |Depositos : Nenhuma Movimentação Encontrada|

                   
                """)
         break
    



    elif opcao == "q":
        break
    
        



      


# opcao = int(input("---Digite a opção desejada : "))
# saldo = 100




# if opcao == 1:
#    print("quanto deseja sacar ?")
 #   valor_saque = int(input("Qual Valor Deseja Sacar: "))
 #   if valor_saque <= saldo:
 #       print(f"saque de {valor_saque} Realizado com Sucesso !")
 #   else:
 #       print("Saldo insufiente para saque")
