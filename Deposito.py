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
