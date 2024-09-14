# Atividade bancaria

menu = """

[d] depositar
[s] saque
[e] extrato
[q] interromper procedimento

==> """




deposito = 0
saque = 500
extrato = ""
numero_saques = 0
total_saques = 3
saldo = 0
historico_transacoes = []




def deposito():
    global saldo, historico_transacoes
    
    while True:
        try: 
            valor = float(input("Quanto voce deseja depositar? R$"))
            if valor < 0:
                print("Por favor, digite um valor positivo")
            else:
                saldo += valor
                historico_transacoes.append(f"Deposito: R${saldo:.2f}")
                print(f"Seu saldo ficou de {saldo:.2f}")
        except ValueError:
            print("Por favor, insira um numero valido")
            continue
        
        while True:
            r = input(str("deseja fazer outro saldo? (sim/não): ")).strip().lower()
            if r == "nao" or r == "não":
                print("Obrigado pela preferência")
                return
            elif r == "sim":
                break
            else:
                print("Por gentileza, responsa apenas com sim ou nao!")




def saque():
    global saldo
    global numero_saques
    global total_saques
    
    while True:
        try:
            valor = float(input("Quanto voce deseja sacar? R$"))
            if saldo < valor:
                print("voce não possui dinheiro suficiente para o saque")
            elif numero_saques > total_saques:
                print("Seu limite de saques diarios esgotou")
            elif valor < 0:
                print("digite um valor valido")
            elif valor > 500:
                print("Voce estrapolou o limite de valor por saque, o maximo é R$500")
            else:
                saldo -= valor
                historico_transacoes.append(f"Saque: R${valor:.2f}")
                numero_saques += 1
        except ValueError:
            print("Digite um valor numerico valido.")
            continue
                
        while True:
            r = str(input("Deseja fazer mais algum saque? (sim/não)"))
            if r == "não" or r == "nao":
                print("Obrigado pela preferencia")
                return
            elif r == "sim":
                break
            else:
                print("Selecione apenas sim ou não")




def extrato():
    global saldo, historico_transacoes
    
    print("\n========Extrato=========\n")
    if not historico_transacoes:
        print("Não houve transações!")
    else:
        for transacoes in historico_transacoes:
            print(transacoes)
    print(f"Saldo: R${saldo:.2f}")
    print("\n=====================\n")





while True:
    
    opção = input(menu)
    
    if opção == "d":
        deposito()
    
    elif opção == "s":
        saque()
    
    elif opção == "e":
        extrato()
    
    elif opção == "q":
        break
    
    else:
        print("A opção selecionada não existe")
    

