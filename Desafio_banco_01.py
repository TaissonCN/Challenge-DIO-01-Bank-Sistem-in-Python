menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
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
            print("O valor do depósito deve ser positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Não há saldo suficiente para realizar o saque.")

        elif valor > limite:
            print(f"O valor do saque excede o limite.")

        elif numero_de_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do saque deve ser positivo.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        if extrato:
            print(extrato)
        else:
            print("Nenhuma movimentação realizada.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================\n")

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
s