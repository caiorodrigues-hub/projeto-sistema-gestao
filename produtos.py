
lista_produtos = []

categorias = {
    "001": "Eletrônicos",
    "002": "Livros",
    "003": "Roupas, Calçados e Joias",
    "004": "Casa e Cozinha",
    "005": "Beleza e Cuidados Pessoais",
    "006": "Saúde e Cuidados com a Casa",
    "007": "Brinquedos e Jogos",
    "008": "Esportes e Atividades ao Ar Livre",
    "009": "Automotivo",
    "010": "Industrial e Científico",
    "011": "Alimentos e Bebidas",
    "012": "Informática e Acessórios",
    "013": "Instrumentos Musicais",
    "014": "Pet Shop",
    "015": "Ferramentas e Materiais de Construção",
    "016": "Filmes e Séries de TV",
    "017": "Videogames",
    "018": "Papelaria e Escritório",
    "019": "Jardim e Piscina",
    "020": "Bebês"
}

def cria_codigo():
    if not lista_produtos:
        return "P00001"
    else:
        ultimo = max(int(produto["codigo"][1:]) for produto in lista_produtos)
        return f"P{ultimo+ 1:05d}"

def verificar_preco(preco):
    return preco > 0

def mostra_categoria():
    print("Categorias disponíveis:")
    for id, categoria in categorias.items():
        print(f"{id}: {categoria}")
   
def verifica_categoria(categoria):
    return categoria in categorias
    
def cadastrar_novo_produto():
    print("---Cadastro Produto---")

    #criando um codigo unico para o produto
    codigo = cria_codigo()
    
    #nome do produto
    nome = input("Nome:  ").lower().strip().title()

    #validando e atribuindo o preço
    while True:
        try: 
            preco = float(input("Preço: "))
            if verificar_preco(preco):
                break
            else:
                print("❗ Apenas números positivos e diferentes de 0 são válidos.")
        except ValueError :
            print("❗ Valor inválido! Digite apenas números. (Exemplo: 99.99)")
            
    #mostra as categorias disponiveis e depois atribui a categoria pelo ID    
    while True:
        try:
            mostra_categoria()
            categoria = input("ID da Categoria: ").zfill(3)
            if verifica_categoria(categoria):
                break
            else: print("❗ Categoria inválida!")
        except ValueError:
            print("❗ Valor inválido! Digite apenas números. (Exemplo: 001)")
    
    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categorias[categoria],
        "preço": preco,
    }
    
    lista_produtos.append(novo_produto)
    from estoque import atualiza_estoque_ao_cadastrar
    atualiza_estoque_ao_cadastrar(novo_produto["codigo"])
    print("✅ Produto cadastrado com sucesso!")

def formato_valido_codigo(codigo):
    return (len(codigo) == 6 and
            codigo.startswith("P") and
            codigo[1:].isdigit()
            )

def codigo_existe(codigo):
    return any(produto["codigo"] == codigo for produto in lista_produtos)

def atribui_novo_codigo(codigo_antigo, codigo_novo):
    for produto in lista_produtos:
        if produto["codigo"] == codigo_antigo:
            from estoque import estoque
            if codigo_antigo in estoque:
                estoque[codigo_novo] = estoque.pop(codigo_antigo)
            produto["codigo"] = codigo_novo
            return True
    return False
            
def altera_codigo_produto():
    while True:
        try:
            codigo_atual = input("Digite o código do produto ou 0 para sair: ").strip().upper()
            if codigo_atual == "0":
                print("Operação cancelada!")
                break
            
            if not formato_valido_codigo(codigo_atual):
                print("❗ Formato inválido.")
                continue
            
            if not codigo_existe(codigo_atual):
                print("❗ Código do produto não encontrado.")
                continue
            
            codigo_novo = input("Digite o novo código. ex(P0001): ").strip().upper()
            
            if not formato_valido_codigo(codigo_novo):
                print("❗ Formato inválido.")
                continue
            
            if codigo_existe(codigo_novo):
                print("❗ Código já registrado. Digite um código novo e válido.")
                continue
            
            if atribui_novo_codigo(codigo_atual, codigo_novo):
                print("✅ Código alterado com sucesso.")
                break
            else:
                print("❗ Erro ao alterar o código.")
                continue
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def nome_produto_existe(nome):
    return any(produto["nome"] == nome for produto in lista_produtos)

def atribui_novo_nome_produto(codigo, nome_novo):
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            produto["nome"] = nome_novo
            return True
    else:
        print("Erro ao alterar nome")
        return False

def altera_nome_produto():
    while True: 
        try:
            codigo = input("Digite o codigo do produto que deseja alterar ou 0 para sair: ").strip().upper()
            if codigo == "0":
                print("Operação cancelada")
                break
            
            if not formato_valido_codigo(codigo):
                print("❗ Formato inválido.")
                continue
            
            if not codigo_existe(codigo):
                print("❗ Código não existe.")
                continue
            
            nome_novo = input("Digite o novo nome do produto: ").strip().title()
            if nome_produto_existe(nome_novo):
                print("❗ Nome já existente.")
                continue
            
            if atribui_novo_nome_produto(codigo, nome_novo):
                print("✅ Nome alterado com sucesso.")
                break
            else:
                print("❗ Erro ao alterar o produto.")
                continue
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def verifica_preco(preco):
    return preco > 0

def atribui_novo_preco(codigo, preco_novo):
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            produto["preço"] = preco_novo
            return True
    else:
        return False

def altera_preco_produto():
     while True: 
        try:
            codigo = input("Digite o codigo do produto que deseja alterar ou 0 para sair: ").strip().upper()
            if codigo == "0":
                print("Operação cancelada")
                break
            
            if not formato_valido_codigo(codigo):
                print("❗ Formato inválido.")
                continue
            
            if not codigo_existe(codigo):
                print("❗ Código não existe.")
                continue
            
            preco_novo = float(input("Digite o novo preço do produto: "))
            if not verifica_preco(preco_novo):
                print("❗ Preço inválido.")
                continue
            
            if atribui_novo_preco(codigo, preco_novo):
                print("✅ Preço alterado com sucesso!")
                break
            else:
                print("❗ Erro ao alterar o preço.")
                continue    
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def atribui_nova_categoria(codigo, categoria_nova):
    nome_categoria = categorias[categoria_nova]
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            produto["categoria"] = nome_categoria
            return True
    else:
        return False

def altera_categoria_produto():
    while True: 
        try:
            codigo = input("Digite o codigo do produto que deseja alterar ou 0 para sair: ").strip().upper()
            if codigo == "0":
                print("Operação cancelada")
                break
            
            if not formato_valido_codigo(codigo):
                print("❗ Formato inválido.")
                continue
            
            if not codigo_existe(codigo):
                print("❗ Código não existe.")
                continue
            
            mostra_categoria()
            categoria_nova = input("Digite a nova categoria do produto: ").zfill(3)
            
            if not verifica_categoria(categoria_nova):
                print("❗ Categoria inválida.")
                continue
            
            if atribui_nova_categoria(codigo, categoria_nova):
                print("✅ Categoria alterada com sucesso")
                break
            else:
                print("❗ Erro ao alterar categoria.")
                continue
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def altera_produto():
    print("Selecione a alteração:")
    print("1- Código\n2- Nome\n3- Preço\n4- Categoria\n0- Sair")
    print("-" * 40)
    opcao = int(input("Opção: "))
    
    match opcao:
        case 1: 
            print("---Alteração de código---")
            altera_codigo_produto()
        case 2: 
            print("---Alteração de nome---")
            altera_nome_produto()
        case 3: 
            print("---Alteração de preço---")

            altera_preco_produto()
        case 4: 
            print("---Alteração de categoria---")
            altera_categoria_produto()
        case 0: 
            print("Operação Finalizada.")
        case _: 
            print("❗ Opção inválida.") 

def exibir_produtos():
    print("\n{:<10} {:<25} {:<30} {:<10}".format(
        "CÓDIGO", "NOME", "CATEGORIA", "PREÇO"))
    print("-" * 85)
    
    for produto in lista_produtos:
        print("{:<10} {:<25} {:<30} R${:<8.2f}".format(
            produto['codigo'],
            produto['nome'],
            produto['categoria'],
            produto['preço']))
    print("-" * 85)
    print(f"Total de produtos: {len(lista_produtos)}\n")