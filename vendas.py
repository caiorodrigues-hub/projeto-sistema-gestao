from clientes import lista_clientes, cpf_existe, limpar_cpf
from produtos import lista_produtos, codigo_existe
from estoque import estoque

def seleciona_cliente():
    cpf = limpar_cpf(input("Digite o cpf: ").strip())
    if cpf_existe(cpf, lista_clientes):
        for cliente in lista_clientes:
            if cliente["cpf"] == cpf:
                return cliente
        return None

def verifica_quantidade(quantidade):
    return(quantidade > 0 and quantidade <= 100)

def verifica_estoque(qtd, codigo):
    return (qtd <= estoque[codigo])

def mostra_estoque_item(codigo):
    disponivel = estoque[codigo]
    return disponivel
 
def atualiza_estoque(carrinho):
    for item in carrinho:
        codigo = item["codigo"]
        quantidade = item["quantidade"]
        estoque[codigo] -= quantidade
 
def aprova_produto():
    while True:
        try:
            codigo = input("Digite o código do produto ou 0 para sair: ").upper()
            
            if codigo == '0':
                print("Operação Finalizada.")
                break
            
            if not codigo_existe(codigo):
                print("❗ Código não existente")
                continue
            
            qtd = int(input("Digite a quantidade: "))
            
            if not verifica_quantidade(qtd):
                print("❗ Quantidade inválida")
                continue
            
            if not verifica_estoque(qtd, codigo):
                print("❗ Estoque indisponível.")
                continue
            
            for produto in lista_produtos:
                if produto["codigo"] == codigo:
                    item = {
                        "codigo": codigo,
                        "nome": produto["nome"],
                        "quantidade": qtd,
                        "preço_unitário": produto["preço"],
                        "subtotal": qtd * produto["preço"],
                                }
                    break
            return item
                
        except Exception as e:
            print(f"Error {e}")

def mostra_carrinho(carrinho):
    for item in carrinho:
        for chave, valor in item.items():
            print(f"{chave}: {valor}")
    print(f"Valor total: {total_compra(carrinho)}")
            
def total_compra(carrinho):
    total = sum(item["subtotal"] for item in carrinho)
    return total

def atualiza_gasto(cliente, total):
    cliente["total_gasto"] += total

    if cliente["total_gasto"] >= 1000 and cliente["total_gasto"] < 5000:
        cliente["nivel"] = "Prata"
        return
    
    if cliente["total_gasto"] >= 5000 and cliente["total_gasto"] < 10000:
        cliente["nivel"] = "Ouro"
        return
    
    if cliente["total_gasto"] >= 10000 and cliente["total_gasto"] < 20000:
        cliente["nivel"] = "Platina"
        return
    
    if cliente["total_gasto"] >= 20000 and cliente["total_gasto"] < 50000:
        cliente["nivel"] = "Diamante"
        return
    
    if cliente["total_gasto"] >= 50000 and cliente["total_gasto"]:
        cliente["nivel"] = "Black"
        return
    
def realiza_venda():
    carrinho = []
    while True:
        try:
            cliente = seleciona_cliente()
            if not cliente:
                print("❗ Cliente não encontrado.")
                continue
            else:
                break
        except Exception as e:
            print(f"Error {e}")
    
    while True:
        try:
            item = aprova_produto()
            if item is None:
                break
            else:
                carrinho.append(item)
                print(f"{item['nome']}: adicionado!")
            
            continuar = int(input("Digite 1 para continuar ou 0 para sair: "))
            if continuar == 1:
                continue
            else:
                print("✅ Carrinho finalizado.")
                break
        except Exception as e:
            print(f"Error {e}")
    
    if not carrinho:
        print("❗ Carrinho vazio")
        return
    
    mostra_carrinho(carrinho)
        
    finaliza = input("Deseja realizar a compra? 1- (SIM) / 2- (NÃO): ").strip()
    if finaliza == '1':
        atualiza_estoque(carrinho)
        atualiza_gasto(cliente, total_compra(carrinho))
        for item in carrinho:
            print(f"Compra de {item['nome']} x{item['quantidade']} efetuada.")
    
    else:
        print("❗ Compra cancelada.")
        return