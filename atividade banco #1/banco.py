print("Banco Cauane do Brasil")

conta = 1000.00
saques_feitos=  0
extrato = []

while True:
    print("ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS:")
    print("[1] Saque")
    print("[2] Depósito")
    print("[3] Extrato")
    print("[4] ENCERRAR")

    opcao = int(input("Selecione uma opção: "))
    if opcao == 4:
        break

    if opcao == 1:
        saque = float(input("quanto você deseja sacar? "))
        if saque > conta:
            print("operação invalida, saldo insuficiente")
        elif saques_feitos == 3:
            print("Limite de saques atingido.")
        else:
            conta -= saque
            saques_feitos += 1
            print(f"Você sacou R${saque:.2f}")
            extrato.append(("saque", saque))
    elif opcao == 2:
        deposito = float(input("quanto você deseja depositar? "))
        conta += deposito  
        print(f"você depositou R${deposito:.2f}, seu saldo agora é de R${conta:.2f}")
        extrato.append(("deposito", deposito))
    elif opcao == 3:
        for movimentacao in extrato:
            print(f"{movimentacao[0]}: R${movimentacao[1]}")
        print(f"O saldo atual é R${conta:.2f}")
    