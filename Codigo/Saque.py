def saque():
    global saldo
    global numero_saques
    global total_saques
    global limite_transacoes
    global total_transacoes
    
    
    while True:
        try:
            valor = float(input("Quanto voce deseja sacar? R$"))
            if saldo < valor:
                print("voce não possui dinheiro suficiente para o saque")
            elif numero_saques > total_saques:
                print("Seu limite de saques diarios esgotou")
            elif valor < 0:
                print("digite um valor valido")
            elif limite_transacoes > total_transacoes:
                print("Voce excedeu o numero de transações permitidas para hoje")
            elif valor > 500:
                print("Voce estrapolou o limite de valor por saque, o maximo é R$500")
            else:
                saldo -= valor
                historico_transacoes.append(f"Saque: R${valor:.2f} feito no data de {datetime.datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}")
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