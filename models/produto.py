import json
from models.modelo import Modelo

class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__id_categoria = id_categoria

#set

    def set_id(self, id):
        if (id == ""): 
            raise ValueError("O ID não pode estar vazio")
        self.__id = id

    def set_descricao(self, descricao):
        if (descricao == ""): 
            raise ValueError("A descrição não pode estar vazia")
        self.__descricao  = descricao

    def set_preco(self, preco):
        if (preco == ""): 
            raise ValueError("O preço não pode estar vazio")
        self.__preco = preco
        
    def set_estoque(self, estoque):
        if (estoque == ""): 
            raise ValueError("O estoque não pode estar vazio")
        self.__estoque = estoque

    def set_id_categoria(self, id_categoria):
        if (id_categoria == ""): 
            raise ValueError("A categoria não pode estar vazia")
        self.__id_categoria = id_categoria

#get

    def get_id(self):
        return self.__id
    
    def get_descricao(self):
        return self.__descricao
    
    def get_preco(self):
        return self.__preco
    
    def get_estoque(self):
        return self.__estoque
        
    def get_id_categoria(self):
        return self.__id_categoria
    
#str
    def __str__(self):
        return f"ID: {self.__id}, Produto: {self.__descricao}, Preço: R$ {self.__preco:.2f}, Estoque: {self.__estoque}, ID Categoria: {self.__id_categoria}"
    
    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "preco": self.__preco,
            "estoque": self.__estoque,
            "id_categoria": self.__id_categoria
        }

class Produtos(Modelo):
    
    @classmethod
    def abrir(cls):
        cls.objetos = [] 
        try:   
            with open("produtos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Produto(
                        dic["id"], 
                        dic["descricao"],
                        dic["preco"], 
                        dic["estoque"],
                        dic["id_categoria"])
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass        

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo, indent=4)