# 🛍️ Sistema de Gestão Comercial (Python)
Este projeto é um sistema de gerenciamento comercial desenvolvido em **Python**, utilizando estruturas como **listas e dicionários** para simular o controle de **clientes, produtos, estoque e vendas**.

Ele tem como objetivo **treinar habilidades de lógica de programação, organização de código e boas práticas**, sendo também o primeiro passo para projetos maiores com banco de dados e interface gráfica.

---

## ✅ Funcionalidades

- **Clientes**
  - Cadastro com validação de nome, CPF e e-mail
  - Alteração de dados
  - Atribuição de níveis de fidelidade
  - Listagem de todos os clientes

- **Produtos**
  - Cadastro com código automático e categorias
  - Alteração de nome, preço, categoria e código
  - Listagem de todos os produtos

- **Estoque**
  - Vinculado automaticamente aos produtos cadastrados
  - Adição e subtração com validações
  - Impede estoques negativos
  - Visualização completa

- **Vendas**
  - Seleção do cliente
  - Adição de múltiplos produtos (carrinho)
  - Verificação de estoque
  - Atualização automática do total gasto e estoque

---

## 🧠 Estrutura do Projeto

O projeto está modularizado da seguinte forma:

- `clientes.py`: lógica de cadastro e alteração de clientes
- `produtos.py`: lógica dos produtos e categorias
- `estoque.py`: controle de quantidade dos produtos
- `vendas.py`: lógica de carrinho e compra
- `main.py`: ponto de entrada do sistema com menus interativos

Todo o sistema roda no terminal, sem dependências externas além do próprio Python 3.

---

## ▶️ Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/caiorodrigues-hub/projeto-sistema-gestao
cd projeto-sistema-gestao  
python main.py
```
Este projeto foi desenvolvido por Caio Rodrigues, estudante de Ciência da Computação, como parte do processo de aprendizagem e construção de portfólio.

# Linkedin: https://www.linkedin.com/in/caio-rodrigues02/

📌 Próximos passos planejados para o projeto:
- Conexão com banco de dados SQL (persistência de dados)
- Criação de interface gráfica usando Tkinter
- Geração de relatórios e gráficos com vendas e estoque
- Exportação de dados em CSV
- Empacotamento do sistema em executável (.exe) com PyInstaller
- Integração com login e controle de usuários

