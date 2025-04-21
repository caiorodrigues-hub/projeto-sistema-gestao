from datetime import datetime

lista_clientes = []

niveis = {
    1: "Bronze",
    2: "Prata",
    3: "Ouro",
    4: "Platina",
    5: "Diamante",
    6: "Black",
}

def verifica_nome(nome):
    return all(parte.isalpha() for parte in nome.split())

def verificar_cpf(cpf):
    #verifica o tamanho do cpf
    if len(cpf) != 11:
        return False
    
    #verifica se todos os digitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # cálculo do primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # cálculo do segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # compara com os dois últimos dígitos do CPF original
    return cpf[-2:] == f"{digito1}{digito2}"
    
def limpar_cpf(cpf):
    return ''.join(filter(str.isdigit, cpf))

def cpf_existe(cpf, lista_clientes):
    for cliente in lista_clientes:
        if cliente["cpf"] == cpf:
            return True
    return False

def verificar_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

def cadastrar_clientes():
    print("---Cadastro---")
    
    #criacao da identificação do cliente
    identificacao = len(lista_clientes) + 1
    
    #cadastro do nome
    while True: 
        nome = input("Nome: ").lower().title().strip()
        if verifica_nome(nome): break
        else: print("❗ Nome inválido. Apenas letras são válidas. (ex: João Pedro Silva)")

    #cadastro, limpeza e veracidade do cpf
    while True:
        cpf = input("CPF (apenas dígitos): ").strip()
        cpf = limpar_cpf(cpf)
        if verificar_cpf(cpf):
            break
        else: print("❗ CPF inválido! Tente novamente")
    
    if cpf_existe(cpf, lista_clientes): 
        print("❗ CPF já cadastrado!")
        return
    
    #cadastro do email e verificando se tem os componentes básicos de um email verídico
    while True:
        email = input("Digite o E-mail: ").lower().strip()
        if verificar_email(email): break
        else: print("❗ E-mail inválido!")
            
    #registro da data de cadastro
    data_cadastro = datetime.today().strftime("%d/%m/%Y")
    
    novo_cliente = {
        "id": identificacao,
        "nome": nome,
        "cpf": cpf,
        "e-mail": email,
        "data": data_cadastro,
        "total_gasto": 0.0,
        "nivel": "bronze"
    }
    
    lista_clientes.append(novo_cliente)
    print("✅ Cliente cadastrado com sucesso!")
    
def atribui_novo_nome_cliente(cpf, novo_nome):
    for cliente in lista_clientes:
        if cliente["cpf"] == cpf:
            cliente["nome"] = novo_nome
            return True    
    else:
        return False
    
def altera_nome_cliente():
    
    while True:
        try:
            cpf = limpar_cpf(input("Digite o CPF do usuário: ").strip())
            if not verificar_cpf(cpf):
                print('❗ CPF inválido.')
                continue
            
            if not cpf_existe(cpf, lista_clientes):
                print("❗ CPF inexistente.")
                continue
            
            novo_nome = input("Digite o novo nome: ").lower().strip().title()
            
            if not verifica_nome(novo_nome):
                print("❗ Nome inválido.")
                continue
            
            if atribui_novo_nome_cliente(cpf, novo_nome):
                print("✅ Nome alterado com sucesso!")
                break
            else: 
                print("❗ Erro ao alterar o nome.")
                continue
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def atribui_novo_email_cliente(cpf, novo_email):
    for cliente in lista_clientes:
        if cliente["cpf"] == cpf:
            cliente["e-mail"] = novo_email
            return True    
    else:
        return False

def altera_email_cliente():
    while True:
        try:
            cpf = limpar_cpf(input("Digite o CPF do usuário: ").strip())
            if not verificar_cpf(cpf):
                print('❗ CPF inválido.')
                continue
            
            if not cpf_existe(cpf, lista_clientes):
                print("❗ CPF inexistente.")
                continue
            
            novo_email = input("Digite o novo E-Mail: ").lower().strip()
            
            if not verificar_email(novo_email):
                print("❗ E-Mail inválido.")
                continue
            
            if atribui_novo_email_cliente(cpf, novo_email):
                print("✅ E-Mail alterado com sucesso!")
                break
            else:
                print("❗ Erro ao alterar o E-mail.")
                continue
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def mostra_niveis():
    for cod, nivel in niveis.items():
        print(f"{cod}: {nivel}")

def verifica_nivel(cod):
    if cod in niveis:
        return True
    else: return False

def atribui_novo_nivel_cliente(cpf, novo_nivel):
    for cliente in lista_clientes:
        if cliente["cpf"] == cpf:
            nome_nivel = niveis[novo_nivel]
            cliente["nivel"] = nome_nivel
            return True    
    else:
        return False
    
def altera_nivel_cliente():
    while True:
        try:
            cpf = limpar_cpf(input("Digite o CPF do usuário: ").strip())
            if not verificar_cpf(cpf):
                print('❗ CPF inválido.')
                continue
            
            if not cpf_existe(cpf, lista_clientes):
                print("❗ CPF inexistente.")
                continue
            
            mostra_niveis()
            novo_nivel = int(input("Digite o código do novo nível: "))
            
            if not verifica_nivel(novo_nivel):
                print("❗ Nível inválido.")
                continue
            
            if atribui_novo_nivel_cliente(cpf, novo_nivel):
                print("✅ Nível alterado com sucesso!")
                break
            else:
                print("❗ Erro ao alterar Nível")
                continue
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def altera_cliente():
    print("Selecione a alteração:")
    print("1 - Nome\n2 - E-mail\n3 - Nível\n0 - Sair")
    opcao = int(input("Opção: "))
    
    match opcao:
        case 1: 
            print("---Alteração de Nome---")
            altera_nome_cliente()
        case 2: 
            print("---Alteração de E-mail---")
            altera_email_cliente()
        case 3: 
            print("---Alteração de Nível---")
            altera_nivel_cliente()
        case 0: 
            print("---Operação Finalizada---")
        case _: 
            print("❗ Opção inválida.") 

def exibir_clientes():
    print("\n{:<5}  {:<20}  {:<15}  {:<40}  {:<15}  {:<10}".format(
        "ID", "NOME", "CPF", "E-MAIL", "TOTAL GASTO", "NÍVEL"))
    print("-" * 125)
    
    for cliente in lista_clientes:
        print("{:<5}  {:<20}  {:<15}  {:<40}  R${:<13.2f}  {:<10}".format(
            cliente['id'],
            cliente['nome'],
            cliente['cpf'],
            cliente['e-mail'],
            cliente['total_gasto'],
            cliente['nivel'].title()))
    print("-" * 125)
    print(f"Total de clientes: {len(lista_clientes)}\n")