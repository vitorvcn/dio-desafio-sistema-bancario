menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
movimentacoes = []
numero_movimentacoes = 0

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        deposito = float(input("Informe o valor para deposito: "))
        if deposito > 0:
            numero_movimentacoes+=1
            saldo += deposito
            movimentacoes.append(["Depósito", numero_movimentacoes, deposito, saldo])
            print(f"Deposito realizado com sucesso, seu novo saldo é: R$ {saldo:.2f}")
        else:
            print("Informe um valor positivo maior que zero para deposito!")
        continue
        
    
    if opcao == "s":
        print("Saque")
        if 0 <= numero_saques < LIMITE_SAQUES:
            saque = float(input("Informe o valor para saque: "))
            if saque <= saldo:
                if 0 < saque <= limite:
                        saldo -= saque
                        numero_saques+=1
                        numero_movimentacoes+=1
                        movimentacoes.append(["Saque",numero_movimentacoes, saque, saldo])
                        print(f"Valor do saque: R$ {saque:.2f}\n")
                        print(f"Seu novo saldo é: {saldo:.2f}")
                        print(f"Quantidade de saques efetuados: {numero_saques} de {LIMITE_SAQUES}")
                        
                else:
                    print(f"Informe um valor maior que zero até o limite de: R$ {limite:.2f}")
            else:
                print("Saldo insuficiente!")        
        else:
            print(f"Limite de {LIMITE_SAQUES} saques diários já atingidos!")
        continue
    
    
    if opcao == "e":
        print("Extrato")
        for movimentacao in movimentacoes:
            print(f"Número: {movimentacao[1]}")
            print(f"Tipo: {movimentacao[0]}")
            print(f"Valor: R${movimentacao[2]:.2f}")
            print(f"Saldo final: R${movimentacao[3]:.2f}\n")
        continue
        
        
    if opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")