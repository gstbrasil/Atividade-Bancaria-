# Atividade bancaria
from datetime import datetime
import pytz


menu = """

[d] depositar
[s] saque
[e] extrato
[q] interromper procedimento
[nu] cadastrar usuario
[nc] cadastrar conta bancaria
[lc] lista de contas

==> """




deposito = 0
saque = 500
extrato = ""
numero_saques = 0
total_saques = 3
saldo = 0
historico_transacoes = []
limite_transacoes = 0
total_transacoes = 10
usuarios = []
conta = []
nc = 1




def deposito():
    global saldo, limite_transacoes, total_transacoes
    
    while True:
        try: 
            valor = float(input("Quanto voce deseja depositar? R$"))
            if valor < 0:
                print("Por favor, digite um valor positivo")
            elif limite_transacoes > total_transacoes:
                print("Voce excedeu o numero de transações permitidas para hoje")
            else:
                saldo += valor
                historico_transacoes.append(f"Deposito: R${saldo:.2f} feito no data de {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}")
                limite_transacoes += 1
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
                historico_transacoes.append(f"Saque: R${valor:.2f} feito no data de {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}")
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




def novo_usuario():
    while True:
        nome = str(input("Insira o nome do usuário: ")).lower().strip()
        data_de_nascimento = input("Qual a data de nascimento do usuaario: (dd/mm/AAAA) ==> ")
        
        try:
            data_formatada = datetime.strptime(data_de_nascimento, "%d/%m/%Y")
            print(f"Data de nascimento é {data_formatada.strftime('%d/%m/%Y')}")
        except ValueError:
            print("Data esta inserida de forma equivocada, tente novamente.")
            continue
        
        cpf = input("Digite o CPF do usuario: (somente numero!)")
        
        if len(cpf) == 11 and cpf.isdigit():
            if cpf not in [usuario["CPF"] for usuario in usuarios]:
                print("CPF valido")
            else:
                print("CPF ja existente")
                return
        else:
            print("CPF invalido")
            continue
        
        print("Informe os dados a seguir sobre seu endereço:")
        try:
            logradouro = str(input("Logradouro: "))
            nro = int(input("Numero (caso não haja numero, digite 00): "))
            bairro = str(input("Bairro: "))
            cid_est = str(input("Cidade e sigla do estado: "))
        except ValueError:
            print("Valor invalido, tente novamente! (caso não possua numero onde mora, coloque 00)")
            continue
        
        
        usuario = {
            "Nome": nome,
            "Data de Nascimento": data_formatada,
            "CPF": cpf,
            "Logradouro": logradouro,
            "Numero": nro,
            "Bairro": bairro,
            "Cidade e Estado": cid_est
            
        }
        
        usuarios.append(usuario)
        print(f"Usuario {nome} cadastrado com sucesso")
        
        confirmacao = str(input("Deseja fazer outro cadastro? ")).strip
        while True:
            if confirmacao == "sim":
                break
            elif confirmacao == "nao" or "não":
                return
            else:
                print("Por gentileza, apenas sim ou nao")




def nova_conta():
    global usuarios
    global nc
    
    while True:
        vincular = input("Qual o usuario que deseja vincular essa conta? (utilize o cpf do usario) ").lower().strip()
        
        usuario_encontrado = 0
        for usuario in usuarios:
            if vincular == usuario['CPF']:
                usuario_encontrado = usuario
            else:
                print("Usuario inexistente")
                break
        
        if usuario_encontrado:
            print(f"Conta vinculada com usuario {usuario_encontrado['Nome']} com sucesso.")
            conta_corrente = {
                "agencia": "0001",
                "numero": nc,
                "usuário": usuario_encontrado['Nome']
            }
            conta.append(conta_corrente)
            nc += 1
            print(conta_corrente)
        
        
        else:
            print("conta inexistente")
            break
        
        confirmacao = str(input("Deseja fazer outro cadastro? ")).strip()
        while True:
            if confirmacao == "sim":
                break
            elif confirmacao == "nao" or confirmacao == "não":
                return
            else:
                print("Por favor, digite apenas sim ou não")




def lista_contas():
    global usuarios
    
    print("\n=========Usuarios=========\n")
    if not usuarios:
        print("Não existe nenhum usario cadastrado")
    else:
        for usuario in usuarios:
            print(f"{usuario['Nome']}\n{usuario['Data de Nascimento']}\n{usuario['CPF']}\n{usuario['Logradouro']}\n{usuario['Numero']}\n{usuario['Bairro']}\n{usuario['Cidade e Estado']}" )
    print("\n========================\n")
    
    
    print("\n=========Contas==========\n")
    for lista in conta:
        print(f"{lista['agencia']}\n{lista['numero']}\n{lista['usuário']}")
    print("\n=========================\n")




while True:
    
    opção = input(menu)
    
    if opção == "d":
        deposito()
    
    elif opção == "s":
        saque()
    
    elif opção == "e":
        extrato()
    
    elif opção == "nu":
        novo_usuario()
        
    elif opção == "nc":
        nova_conta()
        
    elif opção == "lc":
        lista_contas()
    
    elif opção == "q":
        break
    
    else:
        print("A opção selecionada não existe")
    

