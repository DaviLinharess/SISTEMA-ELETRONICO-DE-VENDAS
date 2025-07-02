import json
from models.modelo import Modelo

class VendaItem:
    def __init__(self, id, qtd, preco, id_venda, id_produto):
        self.__id = id       
        self.__qtd = qtd
        self.__preco = preco
        self.__id_venda = id_venda
        self.__id_produto = id_produto

    def set_id(self, id):
        if (id == ""):
            raise ValueError("O ID não pode estar vazio")
        self.__id = id
    
    def set_qtd(self, qtd):
        if (qtd < 0):
            raise ValueError("A quantidade não pode ser Negativa")
        self.__qtd = qtd

    def set_preco(self, preco):
        if (preco < 0):
            raise ValueError("O preço não pode estar negativo")
        self.__preco = preco

    def set_id_venda(self, id_venda):
        if (id_venda < 0):
            raise ValueError("O ID da venda nao pode ser negativo")
        self.__id_venda = id_venda
        
    def set_id_produto(self, id_produto):
        if (id_produto < 0):
            raise ValueError("O ID do produto nao pode ser negativo")
        self.__id_produto = id_produto

    def get_id(self):
        return self.__id
    
    def get_qtd(self):
        return self.__qtd
    
    def get_preco(self):
        return self.__preco
    
    def get_id_venda(self):
        return self.__id_venda
    
    def get_id_produto(self):
        return self.__id_produto
    
    def __str__(self):
        return f"ID: {self.__id}. Quantidade: {self.__qtd}, Preço: R$ {self.__preco:.2f}, Venda: {self.__id_venda}, Produto: {self.__id_produto}"
        
    def to_json(self):
        return {
            "id": self.__id,
            "qtd": self.__qtd,
            "preco": self.__preco,
            "id_venda": self.__id_venda,
            "id_produto": self.__id_produto
        }

class VendaItens(Modelo):    # Persistência - Armazena os objetos em um arquivo/banco de dados
    
    @classmethod
    def abrir(cls):
        cls.objetos = [] 
        try:   
            with open("vendaitens.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = VendaItem(dic["id"], 
                                    dic["qtd"], 
                                    dic["preco"],
                                    dic["id_venda"],
                                    dic["id_produto"])
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass  
                  
    @classmethod
    def salvar(cls):
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump([v.to_json() for v in cls.objetos], arquivo, indent=4)