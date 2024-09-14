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