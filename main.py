from clientes import lista_clientes, cadastrar_clientes, altera_cliente, exibir_clientes
from produtos import lista_produtos, cadastrar_novo_produto, altera_produto, exibir_produtos
from estoque import estoque, adiciona_estoque, subtrai_estoque, exibir_estoque
from vendas import realiza_venda

def exibir_titulo(titulo):
    print(f"\n{'=' * 30}")
    print(f"{titulo:^30}")
    print(f"{'=' * 30}")

def menu_clientes():
    while True:
        exibir_titulo("MENU CLIENTES")
        print("selecione uma opção")
        print("1 - CADASTRAR CLIENTE")
        print("2 - ALTERAR CLIENTE")
        print("3 - EXIBIR CLIENTES")
        print("0 - SAIR")
        
        try:
            opcao = input("Opção: ").strip()
            match opcao:
                case '1':
                    exibir_titulo("CADASTRO")
                    cadastrar_clientes()
                case '2':
                    exibir_titulo("ALTERAÇÃO")
                    altera_cliente()
                case '3':
                    exibir_titulo("LISTAGEM DE CLIENTES")
                    exibir_clientes()
                case '0':
                    exibir_titulo("Operação Encerrada.")
                    break
                case _:
                    exibir_titulo("❗ Operação Inválida.")
        except Exception as e:
            print(f"Error {e}")

def menu_produtos():
    while True:
        exibir_titulo("MENU PRODUTOS")
        print("selecione uma opção")
        print("1 - CADASTRAR PRODUTO")
        print("2 - ALTERAR PRODUTO")
        print("3 - EXIBIR PRODUTOS")
        print("0 - SAIR")
        
        try:
            opcao = input("Opção: ").strip()
            match opcao:
                case '1':
                    exibir_titulo("CADASTRO")
                    cadastrar_novo_produto()
                case '2':
                    exibir_titulo("ALTERAÇÃO")
                    altera_produto()
                case'3':
                    exibir_titulo("LISTAGEM DE PRODUTOS")
                    exibir_produtos()
                case '0':
                    exibir_titulo("Operação Encerrada.")
                    break
                case _:
                    exibir_titulo("❗ Operação Inválida.")
        except Exception as e:
            print(f"Error {e}")

def menu_estoques():
    while True:
        exibir_titulo("MENU ESTOQUES")
        print("selecione uma opção")
        print("1 - ADICIONAR ESTOQUE")
        print("2 - REMOVER ESTOQUE")
        print("3 - EXIBIR ESTOQUE")
        print("0 - SAIR")
        
        try:
            opcao = input("Opção: ").strip()
            match opcao:
                case '1':
                    exibir_titulo("ADICIONAR")
                    adiciona_estoque()
                case '2':
                    exibir_titulo("REMOVER")
                    subtrai_estoque()
                case '3':
                    exibir_titulo("LISTAGEM DE ESTOQUE")
                    exibir_estoque()
                case '0':
                    exibir_titulo("Operação Encerrada")
                    break
                case _:
                    exibir_titulo("❗ Operação Inválida.")
        except Exception as e:
            print(f"Error {e}")

def menu_vendas():
    while True:
        exibir_titulo("MENU VENDAS")
        print("selecione uma opção")
        print("1 - VENDER")
        print("0 - SAIR")
        
        try:
            opcao = input("Opção: ").strip()
            match opcao:
                case '1':
                    exibir_titulo("VENDER")
                    realiza_venda()
                case '0':
                    exibir_titulo("Operação Encerrada")
                    break
                case _:
                    exibir_titulo("❗ Operação Inválida.")
        except Exception as e:
            print(f"Error {e}")

def menu():
    while True:
        exibir_titulo("MENU PRINCIPAL")
        print("selecione a área desejada")
        print("1 - CLIENTES")
        print("2 - PRODUTOS")
        print("3 - ESTOQUES")
        print("4 - VENDAS")
        print("0 - SAIR")

        try:
            opcao = input("Opção: ").strip()
            match opcao:
                case "1":
                    menu_clientes()
                case "2": 
                    menu_produtos()
                case "3": 
                    menu_estoques()
                case "4": 
                    menu_vendas()
                case "0": 
                    print("Operação Encerrada")
                    break
                case _:
                    print("❗ Operação Inválida.")
        except Exception as e:
            print(f"Error {e}")
            
if __name__ == "__main__":
    menu()