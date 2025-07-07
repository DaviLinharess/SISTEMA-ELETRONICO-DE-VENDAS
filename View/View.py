from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.vendaitem import VendaItem, VendaItens
from models.venda import Venda, Vendas
from models.entrega import Entrega, Entregas
from models.entregador import Entregador, Entregadores




class View:
    @staticmethod
    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.get_email() == "admin@gmail.com": 
                return 
        cliente = Cliente(None, "admin@gmail.com", "1234", "Admin", "0000", True)  #ID: None, Email: admin, Senha: 1234, Nome: Admin, Telefone: 0000
        Clientes.inserir(cliente)  #salva 
#MÉTODOS DE CLIENTE

    @staticmethod
    def autenticar_usuario(email, senha):
        for cliente in Clientes.listar(): #tenta entrar como cliente ou admin
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return {
                    "id": cliente.get_id(),
                    "nome": cliente.get_nome(),
                    "e_admin": cliente.get_e_admin(),
                    "e_entregador": False  # não é um entregador
                }
    
        for entregador in Entregadores.listar(): #se não é cliente, tenta como entregador
            if entregador.get_email() == email and entregador.get_senha() == senha:
                return {
                    "id": entregador.get_id(),
                    "nome": entregador.get_nome(),
                    "e_admin": False, # não é  admin
                    "e_entregador": True  # é entregador
                }
        
        return None #se não encontrou nenhum, retorna None

    @staticmethod
    def Cliente_Listar():
        return Clientes.listar()

    @staticmethod
    def Cliente_Inserir(email: str, senha: str, nome: str, fone: str):
        for c in Clientes.listar():
            if c.get_email().lower() == email.lower(): #caso o email ja esteja cadastrado
                raise ValueError("Este email já está cadastrado.")
        
        cliente = Cliente(None,email, senha, nome, fone, False)
        Clientes.inserir(cliente)

    @staticmethod
    def Cliente_Atualizar(id: int, nome: str, email: str, fone: str):
        cliente = Clientes.listar_id(id)
        if cliente is None:       #se o se o ID não estiver na lista de ID atual
            raise ValueError("O ID está inválido")     #o ID sera invalido
        cliente.set_nome(nome)
        cliente.set_email(email)
        cliente.set_fone(fone)
        Clientes.atualizar(cliente)
       

    @staticmethod
    def Cliente_Excluir(id: int):
        cliente = Clientes.listar_id(id)
        if cliente is None:     #se o ID nao estiver na lista
            raise ValueError("O ID está inválido")     #o ID sera invalido
        Clientes.excluir(cliente)                    #remover o cliente do [id]

#MÉTODOS DE CATEGORIA

    @staticmethod
    def categoria_listar():
        return Categorias.listar()

    @staticmethod
    def categoria_inserir(descricao):
        categoria = Categoria(None, descricao)
        Categorias.inserir(categoria)

    @staticmethod
    def categoria_atualizar(id, descricao):
        categoria = Categorias.listar_id(id)
        if categoria is None:
            raise ValueError("ID inválido")
        categoria.set_descricao(descricao)  
        Categorias.atualizar(categoria)

    @staticmethod
    def categoria_excluir(id):
        categoria = Categorias.listar_id(id)
        if categoria is None:
            raise ValueError("O ID está inválido")
        Categorias.excluir(categoria)

    @staticmethod
    def produto_listar_por_categoria(id_categoria):
        return [p for p in Produtos.listar() if p.get_id_categoria() == id_categoria]

#MÉTODOS DE PRODUTO

    @staticmethod
    def Produto_Listar():
        return Produtos.listar()

    @staticmethod
    def Produto_Inserir(descricao, preco, estoque, idCategoria):
        produto = Produto(None, descricao, preco, estoque, idCategoria)
        Produtos.inserir(produto)

    @staticmethod
    def Produto_Atualizar(id, descricao, preco, estoque, idCategoria):
        produto = Produtos.listar_id(id)
        if produto is None:
            raise ValueError("O ID está inválido")
        produto.set_descricao(descricao)
        produto.set_preco(preco)
        produto.set_estoque(estoque)
        produto.set_id_categoria(idCategoria)
        Produtos.atualizar(produto)

    @staticmethod
    def Produto_Excluir(id):
        produto = Produtos.listar_id(id)
        if produto is None:
            raise ValueError("O ID está inválido")
        Produtos.excluir(produto)

    @staticmethod
    def Produto_Reajustar(percentual: float):
        for produto in Produtos.listar():
            preco = produto.get_preco()
            novo_preco = preco + (preco * percentual / 100)
            produto.set_preco(novo_preco)
            Produtos.atualizar(produto)
    
#MÉTODO ENTREGADOR
    @staticmethod
    def Entregador_Listar():
        return Entregadores.listar()
    
    @staticmethod
    def Entregador_Inserir(nome, email, senha, fone):
        for entregador in Entregadores.listar():
            if entregador.get_email().lower() == email().lower():
                raise ValueError(f"O email '{email}' já está em uso.")
        novo_entregador=Entregador(None, nome, email, senha, fone)
        Entregadores.inserir(novo_entregador)

    @staticmethod
    def Entregador_Atualizar(id, nome, email, fone):
        entregador = Entregadores.listar_id(id)
        if entregador is None:
            raise ValueError("ID do entregador é inválido")
        
        entregador.set_nome(nome)
        entregador.set_email(email)
        entregador.set_fone(fone)
        Entregadores.atualizar(entregador)

    @staticmethod
    def Entregador_Excluir(id):
        entregador = Entregadores.listar_id(id)
        if entregador is None:
            raise ValueError("ID do entregador é inválido")
        Entregadores.excluir(entregador)

    @staticmethod
    def Entrega_Listar_Entregador(id_entregador): #retorna uma lista de entregas de certo entregador
        minhas_entregas = []
        for entrega in Entregas.listar():
            if entrega.get_id_entregador() == id_entregador:
                minhas_entregas.append(entrega)
        return minhas_entregas
    
    @staticmethod
    def Confirmar_Entrega(id_entrega): #altera o endereço da entrega para "Entregue"
        entrega = Entregas.listar_id(id_entrega)
        if entrega is None:
            raise ValueError("ID de entrega inválido")
        
        if entrega.get_status() == "Entregue":
            raise ValueError("Essa entrega ja foi confirmada.")
        
        entrega.set_status("Entregue")
        Entregas.atualizar(entrega)

#MÉTODOS DE CLIENTE (Complemento)
    @staticmethod
    def Cliente_Listar_id(id: int):
        return Clientes.listar_id(id)

#MÉTODOS DE PRODUTO (Complemento)
    @staticmethod
    def Produto_Listar_id(id: int):
        return Produtos.listar_id(id)

#MÉTODOS DE VENDA
    @staticmethod
    def Venda_Listar():
        # Retorna todas as vendas que não são mais carrinhos
        return [v for v in Vendas.listar() if not v.get_carrinho()]

    @staticmethod
    def Venda_Listar_Cliente(cls, id_cliente):
        cls.Venda_abrir()
        
        vendas_do_cliente = []

        for venda in Vendas.listar():
            if venda.get_id_cliente() == id_cliente:
                vendas_do_cliente.append(venda)
                
        return vendas_do_cliente
    
    @staticmethod
    def Venda_Listar_Cliente(id_cliente):
        # Retorna as vendas finalizadas de um cliente específico
        return [v for v in Vendas.listar() if v.get_id_cliente() == id_cliente and not v.get_carrinho()]

    @staticmethod
    def Venda_Itens_Listar(id_venda):
        # Retorna os itens de uma venda específica
        return [item for item in VendaItens.listar() if item.get_id_venda() == id_venda]

    @staticmethod
    def Venda_Listar_Pendentes(): #vendas finalizadas que não foram entregues
        vendas_finalizadas = [v for v in Vendas.listar() if not v.get_carrinho()]
        entregas_iniciadas_ids = [e.get_id_venda() for e in Entregas.listar()]

        vendas_pendentes = []
        for v in vendas_finalizadas: #entre as vendas finalizadas
            if v.get_id() not in entregas_iniciadas_ids: #se ela nao tiver sido entregue ainda
                vendas_pendentes.append(v) #adiciona  alista de vendas pendentes
        return vendas_pendentes
    
    
    @staticmethod
    def Iniciar_Entrega(id_venda, id_entregador):
        from datetime import datetime

        for entrega_existente in Entregas.listar(): #se a venda ja foi escolhida por um entregador
            if entrega_existente.get_id_venda() == id_venda:
                raise ValueError("Esta venda ja possui entrega escolhida")
            
        nova_entrega = Entrega(
            id=None,
            id_venda=id_venda,
            id_entregador=id_entregador,
            status="Pendente",
            data=datetime.now()
        )
        Entregas.inserir(nova_entrega)

            
    

#CARRINHO
    @staticmethod
    def carrinho_adicionar(id_cliente, id_produto, qtd):
        from datetime import datetime
        vendas = Vendas.listar()
        carrinho = None # busca carrinho existente
        for v in vendas:  #procurando se cliente ja tem carrinho em aberto
            if v.get_id_cliente() == id_cliente and v.get_carrinho(): #se a venda é do cliente atual e se ainda é um carrinho (nao foi finalizada)
                carrinho = v      #se encontrar, guarda a variavel no carrinho e interrompe o laço, pois so pode ter 1 carrinho por cliente
                break
        
        if carrinho is None:
            carrinho = Venda(None, datetime.now(), 0, id_cliente, True)
            Vendas.inserir(carrinho)    #criando carrinho caso n tenha nenhum
        
        produto = Produtos.listar_id(id_produto)
        if produto is None:
            raise ValueError("Produto inválido")
        if produto.get_estoque() < qtd:
            raise ValueError("Estoque insuficiente")

        item = VendaItem(None, qtd, produto.get_preco(), carrinho.get_id(), id_produto)
        VendaItens.inserir(item)

    @staticmethod
    def carrinho_listar(id_cliente):
        carrinho = None
        for v in Vendas.listar():           #procurando nas vendas 
            if v.get_id_cliente() == id_cliente and v.get_carrinho(): #se o cliente  ja tiver carrinho
                carrinho = v                    #o carrinho do cliente é o da venda que achou
                break                           #encerra laço p ter so 1 carrinho
        if carrinho is None:                    #se nao tem carrinho
            return []                           #retorna vazio

        return [item for item in VendaItens.listar() if item.get_id_venda() == carrinho.get_id()] #itens do carrinho
    
    @staticmethod
    def carrinho_finalizar(id_cliente):
        carrinho = None
        for v in Vendas.listar():
            if v.get_id_cliente() == id_cliente and v.get_carrinho():
                carrinho = v
                break
        if carrinho is None:
            raise ValueError("Carrinho vazio.")

        total = 0
        for item in VendaItens.listar():
            if item.get_id_venda() == carrinho.get_id():
                total += item.get_qtd() * item.get_preco()
                produto = Produtos.listar_id(item.get_id_produto())
                produto.set_estoque(produto.get_estoque() - item.get_qtd())
                Produtos.atualizar(produto)

        carrinho.set_total(total)
        carrinho.set_carrinho(False)
        Vendas.atualizar(carrinho)