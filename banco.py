menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_limite = valor > limite
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        
        elif excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente para realizar o saque de R$ {valor:.2f}.")
        
        elif excedeu_saques:
            print(f"Operação falhou! Número máximo de saques diários ({LIMITE_SAQUES}) excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")

