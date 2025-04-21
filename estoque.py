
estoque = {}

def atualiza_estoque_ao_cadastrar(codigo):
    estoque[codigo] = 0

def codigo_existe_estoque(codigo):
    return codigo in estoque

def valida_positivo(n):
    return n > 0

def adiciona_estoque():
    while True:
        try:
            codigo = input("Digite o código do produto ou 0 para sair: ").upper()
            if codigo == "0":
                print("Operação finalizada.")
                break
            
            if not codigo_existe_estoque(codigo):
                print("❗ Código não existente")
                continue
            
            adiciona = int(input("Quantidade adicionada: "))
            
            if not valida_positivo(adiciona):
                print("❗ Quantidade inválida.")
                continue
            
            estoque[codigo] += adiciona
            print(f"✅ Adicionado(s) {adiciona} item(s) com sucesso!")
            break
        
        except Exception as e:
            print(f"Error {e}")

def estoque_nao_zerado(codigo):
    return estoque[codigo] > 0

def estoque_nao_negativo(codigo, subtrai):
    return (estoque[codigo] - subtrai >= 0)

def subtrai_estoque():
    while True:
        try:
            codigo = input("Digite o código do produto ou 0 para sair: ").upper()
            if codigo == "0":
                print("Operação finalizada.")
                break
            
            if not codigo_existe_estoque(codigo):
                print("❗ Código não existente")
                continue
            
            if not estoque_nao_zerado(codigo):
                print("❗ Estoque não pode ser subtraído.")
                continue
            
            subtrai = int(input("Quantidade subtraída: "))
            
            if not valida_positivo(subtrai):
                print("❗ Operação inválida")
                continue
                
            if not estoque_nao_negativo(codigo, subtrai):
                print("❗ Estoques negativos não são permitidos.")
                continue
            
            estoque[codigo] -= subtrai
            print(f"✅ Subtraído(s) {subtrai} item(s) com sucesso!")
            break
        
        except Exception as e:
            print(f"Error {e}")
            
def exibir_estoque():
    print("\n{:<10} {:<15} {:<10}".format(
        "CÓDIGO", "PRODUTO", "ESTOQUE"))
    print("-" * 45)
    
    
    from produtos import lista_produtos
    
    for codigo, qtd in estoque.items():
        nome_produto = next((p['nome'] for p in lista_produtos if p['codigo'] == codigo), "Desconhecido")
        print("{:<10} {:<15} {:<10}".format(
            codigo,
            nome_produto[:15] + ('...' if len(nome_produto) > 15 else ''),
            qtd))
    
    print("-" * 45)
