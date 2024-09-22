

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar novo usuário
    [f] Filtrar usuário
    [c] Criar nova conta
    [q] Sair

    =>""" 
    return input(menu)



def depositar(saldo, valor, extrato, numero_movimentacoes, /):
    if valor > 0:
        numero_movimentacoes+=1
        saldo += valor
        extrato.append(["Depósito", numero_movimentacoes, valor, saldo])
        print(f"Deposito realizado com sucesso, seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Informe um valor positivo maior que zero para deposito!")
   
    return numero_movimentacoes, saldo, extrato





def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques, numero_movimentacoes):
    if 0 <= numero_saques < limite_saques:
        if valor <= saldo:
            if 0 < valor <= limite:
                    saldo -= valor
                    numero_saques+=1
                    numero_movimentacoes+=1
                    extrato.append(["Saque",numero_movimentacoes, valor, saldo])
                    print(f"Saque efetuado com sucesso!\nValor do saque: R$ {valor:.2f}\n")
                    print(f"Seu novo saldo é: {saldo:.2f}")
                    print(f"Quantidade de saques efetuados: {numero_saques} de {limite_saques}")
                    
            else:
                print(f"Informe um valor maior que zero até o limite de: R$ {limite:.2f}")
        else:
            print("Saldo insuficiente!")        
    else:
        print(f"Limite de {limite_saques} saques diários já atingidos!")
    return numero_movimentacoes, numero_saques, saldo, extrato


    
def gerar_extrato(saldo, /, *, extrato):
    if extrato:
        for movimentacao in extrato:
            print(f"Número: {movimentacao[1]}".center(40))
            print(f"Tipo: {movimentacao[0]}".center(40))
            print(f"Valor: R${movimentacao[2]:.2f}".center(40))
            print(f"Saldo final: R${movimentacao[3]:.2f}\n".center(40))
        print(f"Seu saldo atual é: R${saldo:.2f}\n".center(40))
    else:
        print("Não foram realizadas movimentações.".center(40))
        
    print("#"*40)

    
    return extrato


def criar_usuario(usuarios):
    usuario_cpf = input("Informe o CPF do usuário (apenas os números): ")
    cpf_valido = validar_cpf(usuarios, usuario_cpf)
    if cpf_valido == -1:
        return
    usuario_nome = input("Informe o nome do usuário: ")
    usuario_data_nascimento = input("Informe a data de nascimento do usuário: ")
    usuario_logradouro = input("Informe o logradouro do endereço do usuário: ")
    usuario_numero = input("Informe o número da residencia do usuário: ")
    usuario_bairro = input("Informe o bairro do usuário: ")
    usuario_cidade = input("Informe a cidade do usuário: ")
    usuario_sigla_estado = input("Informe a sigla do estado do usuário: ")
    
    usuario_endereço = f"{usuario_logradouro}, {usuario_numero} - {usuario_bairro} - {usuario_cidade}/{usuario_sigla_estado}"  
    
    return {"nome": usuario_nome, "cpf": usuario_cpf, "data_nascimento": usuario_data_nascimento, "endereco": usuario_endereço}
   
   
def filtrar_usuario(usuarios, cpf):
    if usuarios:
        for numero_usuario, usuario in enumerate(usuarios):
            if cpf in usuario.values():
                cpf_cadastrado = True
                return cpf_cadastrado, numero_usuario
        else:
            print("Usuário não cadastrado!u")
            return not usuarios, -1
    else:
        print("Nenhum usuário cadastrado!")
        return not usuarios, -1

    
def validar_cpf(usuarios, cpf):
    print("Validando CPF\n")
    while True:
        if usuarios:
            for usuario in usuarios:
                if cpf in usuario.values():
                    cpf_valido = False
                else:
                    cpf_valido = True 
               
            if cpf_valido:
                print("CPF valido")
                return cpf
                break
            else:
                print("CPF já está cadastrado no sistema!")
                continuar = input("Deseja informar outro CPF? [s]/[n]")
                if continuar == "s":
                    cpf = input("Informe outro CPF: ")
                else:
                    return -1
                    break
        else:
            print("CPF valido")
            return cpf
            break
            
    
def criar_conta(agencia, numero_conta, usuarios):
    usuario_cpf = input("Informe o CPF do usuáiro: ")
    cpf_cadastrado, numero_usuario = filtrar_usuario(usuarios, usuario_cpf)
    if cpf_cadastrado:
        numero_conta+=1
        nova_conta = {"agencia": agencia, "numero_conta": numero_conta, "numero_usuario": numero_usuario}
        return nova_conta, numero_conta
        
    else:
        print("Usuário não encontrado!")
        return

    
    
def main():
    
    saldo = 0
    limite = 500
    extrato = []
    usuarios = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    numero_movimentacoes = 0
    agencia = "0001"
    numero_conta = 0
    contas = []
    while True:
    
        opcao = menu()
        
        if opcao == "d":
            print("Depósito")
            valor = float(input("Informe o valor para deposito: "))
            numero_movimentacoes, saldo, extrato = depositar(saldo, valor, extrato, numero_movimentacoes)
            continue
            
        
        if opcao == "s":
            print("Saque")
            valor = float(input("Informe o valor para saque: "))
            numero_movimentacoes, numero_saques, saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, numero_movimentacoes = numero_movimentacoes)

            continue
        
        
        if opcao == "e":
            print("Extrato".center(40, "#")+"\n")
            extrato = gerar_extrato(saldo, extrato=extrato)
            continue
        
        if opcao == "u":
            print("Cadastrar novo usuário")
            novo_usuario = criar_usuario(usuarios)
            if novo_usuario:
                usuarios.append(novo_usuario)
                print(usuarios)
            continue
        
        if opcao == "c":
            print("Criar nova conta")
            nova_conta, numero_conta = criar_conta(agencia, numero_conta, usuarios)
            if nova_conta:
                contas.append(nova_conta)
                print(contas)
            continue

        if opcao == "f":
            print("Filtrar usuário")
            cpf = input("Informe o CPF do usuário que deseja buscar: ")
            cpf_cadastrado, numero_usuario = filtrar_usuario(usuarios, cpf)
            if cpf_cadastrado:
                print(f"Usuário cadastrado:")
                print(f"Número do usuário: {numero_usuario+1}")
                print(f"CPF:{usuarios[numero_usuario]['cpf']}")
                print(f"Nome:{usuarios[numero_usuario]['nome']}")
                print(f"Data de Nascimento:{usuarios[numero_usuario]['data_nascimento']}")
                print(f"Endereço:{usuarios[numero_usuario]['endereco']}")
            continue
            
        if opcao == "q":
            print("Saíndo...")
            break
        
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")

main()

