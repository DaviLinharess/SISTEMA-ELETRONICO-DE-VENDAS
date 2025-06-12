from View.View import View

class UI:

    @staticmethod
    def Main():
        View.cadastrar_admin() #garantir q o admin existe

        while True:
            print("\n--- SISTEMA DE VENDAS ---")
            print("1 - Fazer Login")
            print("2 - Criar Novo Cliente")
            print("0 - Sair")
            try:
                op = int(input("Escolha uma opção: "))
                if op == 0:
                    print("Encerrando o sistema.")
                    break
                elif op == 1:
                    usuario = UI.Login()
                    if usuario:
                        if usuario.get_e_admin():
                            UI.Menu_Admin()
                        else:
                            UI.Menu_Cliente(usuario.get_id())
                elif op == 2:
                    UI.Criar_Conta()
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

            usuario = None
            while usuario is None:
                usuario = UI.Login()

            if usuario.get_e_admin():
                UI.Menu_Admin()
            else:
                UI.Menu_Cliente(usuario.get_id())

#PARTE LOGIN
    @staticmethod
    def Login():
        print("\n--- Login ---")
        email = input("Email: ")
        senha = input("Senha: ")
        for cliente in View.Cliente_Listar():
            if cliente.get_email() == email and cliente.get_senha() == senha:
                print(f"Bem-vindo, {cliente.get_nome()}!")
                return cliente
        print("Login inválido.")
        return None
    
    @staticmethod
    def Menu_Admin():
        while True:
            print("\n--- MENU ADMIN ---")
            print("1 - Listar Clientes")
            print("2 - Inserir Cliente")
            print("3 - Atualizar Cliente")
            print("4 - Excluir Cliente")
            print("5 - Listar Categorias")
            print("6 - Inserir Categoria")
            print("7 - Atualizar Categoria")
            print("8 - Excluir Categoria")
            print("9 - Listar Produtos")
            print("10 - Inserir Produto")
            print("11 - Atualizar Produto")
            print("12 - Excluir Produto")
            print("13 - Reajustar Preços dos Produtos")
            print("14 - Listar produtos por categoria")
            print("0 - Sair")
            try:
                op = int(input("Escolha uma opção: "))
                if op == 0: break
                elif op == 1: UI.Cliente_Listar()
                elif op == 2: UI.Cliente_Inserir()
                elif op == 3: UI.Cliente_Atualizar()
                elif op == 4: UI.Cliente_Excluir()
                elif op == 5: UI.categoria_listar()
                elif op == 6: UI.categoria_inserir()
                elif op == 7: UI.categoria_atualizar()
                elif op == 8: UI.categoria_excluir()
                elif op == 9: UI.Produto_Listar()
                elif op == 10: UI.Produto_Inserir()
                elif op == 11: UI.Produto_Atualizar()
                elif op == 12: UI.Produto_Excluir()
                elif op == 13: UI.Produto_Reajustar()
                elif op == 14: UI.produto_listar_por_categoria()

                else: print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

    @staticmethod
    def Menu_Cliente(id_cliente):
        while True:
            print("\n--- MENU CLIENTE ---")
            print("1 - Listar Produtos")
            print("2 - Ver Carrinho")
            print("3 - Adicionar Produto ao Carrinho")
            print("4 - Finalizar Compra")
            print("5 - Listar Produtos por Categoria")
            print("0 - Sair")
            try:
                op = int(input("Escolha uma opção: "))
                if op == 0: break
                elif op == 1: UI.Produto_Listar()
                elif op == 2: UI.carrinho_listar_id(id_cliente)
                elif op == 3: UI.carrinho_adicionar_id(id_cliente)
                elif op == 4: UI.carrinho_finalizar_id(id_cliente)
                elif op == 5: UI.produto_listar_por_categoria()
                else: print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")
        
#PARTE DOS CLIENTES
    
    @staticmethod
    def Criar_Conta():
        print("\n--- Criar Novo Cliente ---")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        fone = input("Telefone: ")
        try:
            View.Cliente_Inserir(email, senha, nome, fone)
            print("Cadastro realizado! Faça login.")
        except Exception as e:
            print(f"Erro no cadastro: {e}")

    @staticmethod
    def Cliente_Listar():
        print("\n--- Lista de Clientes ---")
        for cliente in View.Cliente_Listar():
            print(cliente)

    @staticmethod
    def Cliente_Inserir():
        print("\n--- Inserir Cliente ---")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        fone = input("Fone: ")
        View.Cliente_Inserir(nome, email, senha, fone)

    @staticmethod
    def Cliente_Atualizar():
        print("\n--- Atualizar Cliente ---")
        try:
            id = int(input("ID do cliente: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            fone = input("Novo fone: ")
            View.Cliente_Atualizar(id, nome, email, fone)
        except ValueError:
            print("ID inválido.")

    @staticmethod
    def Cliente_Excluir():
        print("\n--- Excluir Cliente ---")
        try:
            id = int(input("ID do cliente a excluir: "))
            View.Cliente_Excluir(id)
        except ValueError:
            print("O ID inserido está inválido.")


#PARTE DA CATEGORIA

    @staticmethod
    def categoria_listar():
        print("\n--- Lista de Categorias ---")
        for categoria in View.categoria_listar():
            print(categoria)

    @staticmethod
    def categoria_inserir():
        print("\n--- Inserir Categoria ---")
        descricao = input("Descrição: ")
        View.categoria_inserir(descricao)

    @staticmethod
    def categoria_atualizar():
        print("\n--- Atualizar Categoria ---")
        try:
            id = int(input("ID da categoria: "))
            descricao = input("Nova descrição: ")
            View.categoria_atualizar(id, descricao)
        except ValueError:
            print("O ID inserido está inválido.")

    @staticmethod
    def categoria_excluir():
        print("\n--- Excluir Categoria ---")
        try:
            id = int(input("ID da categoria pra excluir: "))
            View.categoria_excluir(id)
        except ValueError:
            print("ID inválido.")

    @staticmethod
    def produto_listar_por_categoria():
        try:
            id_categoria = int(input("ID da categoria: "))
            produtos = View.produto_listar_por_categoria(id_categoria)
            if not produtos:
                print("Sem produtos na categoria.")
            for produto in produtos:
                print(produto)
        except ValueError:
            print("ID inválido.")

#PARTE DO PRODUTO

    @staticmethod
    def Produto_Listar():
        print("\n--- Lista de Produtos ---")
        for produto in View.Produto_Listar():
            print(produto)

    @staticmethod
    def Produto_Inserir():
        print("\n--- Inserir Produto ---")
        descricao = input("Descrição: ")
        try:
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            idCategoria = int(input("ID da categoria: "))
            View.Produto_Inserir(descricao, preco, estoque, idCategoria)
        except ValueError:
            print("Use '.' ao invés de ','")

    @staticmethod
    def Produto_Atualizar():
        print("\n--- Atualizar Produto ---")
        try:
            id = int(input("ID do produto: "))
            descricao = input("Nova descrição: ")
            preco = float(input("Novo preço: "))
            estoque = int(input("Novo estoque: "))
            idCategoria = int(input("Novo ID da categoria: "))
            View.Produto_Atualizar(id, descricao, preco, estoque, idCategoria)
        except ValueError:
            print("Dados inválidos.")

    @staticmethod
    def Produto_Excluir():
        print("\n--- Excluir Produto ---")
        try:
            id = int(input("ID do produto pra excluir: "))
            View.Produto_Excluir(id)
        except ValueError:
            print("ID inválido.")

    @staticmethod
    def Produto_Reajustar():
        print("\n--- Reajustar Preço dos Produtos ---")
        try:
            percentual = float(input("Percentual de reajuste: "))    #(ex: 10 para +10%, -5 para -5%)
            View.Produto_Reajustar(percentual)
        except ValueError:
            print("Percentual inválido.")


#PARTE DO CARRINHO
    @staticmethod
    def Carrinho_Listar():
        print("\n--- Itens no Carrinho ---")
        try:
            id_cliente = int(input("ID do Cliente: "))
            itens = View.Carrinho_Listar(id_cliente)
            if len(itens) == 0:
                print("Carrinho vazio.")
            for item in itens:
                print(item)
        except ValueError:
            print("ID inválido.")

    @staticmethod
    def Carrinho_Adicionar():
        print("\n--- Adicionar Produto ao Carrinho ---")
        try:
            id_cliente = int(input("ID do Cliente: "))
            id_produto = int(input("ID do Produto: "))
            qtd = int(input("Quantidade: "))
            View.Carrinho_Adicionar(id_cliente, id_produto, qtd)
            print("Produto adicionado ao carrinho.")
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def Carrinho_Finalizar():
        print("\n--- Finalizar Compra ---")
        try:
            id_cliente = int(input("ID do Cliente: "))
            View.Carrinho_Finalizar(id_cliente)
            print("Compra finalizada.")
        except Exception as e:   #classe base pra erros no python
            print(f"Erro: {e}")  #so pra ter a mensagem de "Erro:"

#CARRINHO PELO ID
    @staticmethod
    def carrinho_listar_id(id_cliente):
        print("\n--- Itens no Carrinho ---")
        try:
            itens = View.carrinho_listar(id_cliente)
            if not itens:
                print("Carrinho vazio.")
            for item in itens:
                print(item)
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def carrinho_adicionar_id(id_cliente):
        print("\n--- Adicionar Produto ao Carrinho ---")
        try:
            id_produto = int(input("ID do Produto: "))
            qtd = int(input("Quantidade: "))
            View.carrinho_adicionar(id_cliente, id_produto, qtd)
            print("Produto adicionado ao carrinho.")
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def carrinho_finalizar_id(id_cliente):
        print("\n--- Finalizar Compra ---")
        try:
            View.carrinho_finalizar(id_cliente)
            print("Compra finalizada.")
        except Exception as e:
            print(f"Erro: {e}")



    