import json
from datetime import datetime
from models.modelo import Modelo

class Venda:
    def __init__(self, id, data, total, id_cliente, carrinho, entregue):
        self.__id = id       
        self.__data = data
        self.__total = total
        self.__id_cliente = id_cliente
        self.__carrinho = carrinho
        self.__entregue = entregue

    # Setters
    def set_id(self, id):
        if id == "":
            raise ValueError("O ID não pode estar vazio")
        self.__id = id

    def set_data(self, data):
        if data > datetime.now():
            raise ValueError("A data não pode estar no futuro")
        self.__data = data

    def set_total(self, total):
        if total < 0:
            raise ValueError("O Total não pode estar negativo")
        self.__total = total

    def set_id_cliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("O ID do Cliente não pode ser negativo")
        self.__id_cliente = id_cliente

    def set_carrinho(self, carrinho):
        if carrinho < 0:
            raise ValueError("O carrinho não pode estar negativo")
        self.__carrinho = carrinho

    def set_entregue(self, entregue):
        self.__entregue = entregue

    # Getters
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_total(self):
        return self.__total

    def get_id_cliente(self):
        return self.__id_cliente

    def get_carrinho(self):
        return self.__carrinho

    def get_entregue(self):
        return self.__entregue

    # Representação textual
    def __str__(self):
        return f"ID: {self.__id}, Data: {self.__data.strftime('%d/%m/%Y %H:%M')}, Total: R$ {self.__total:.2f}, ID do Cliente: {self.__id_cliente}"

    # Serialização para JSON
    def to_json(self):
        dic = {}
        dic["id"] = self.__id       
        dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M")
        dic["total"] = self.__total
        dic["id_cliente"] = self.__id_cliente
        dic["carrinho"] = self.__carrinho
        dic["entregue"] = self.__entregue
        return dic

# Classe de persistência
class Vendas(Modelo):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    obj = Venda(
                        dic["id"],
                        datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"),
                        dic["total"],
                        dic["id_cliente"],
                        dic["carrinho"],
                        dic.get("entregue", False)  # se não existir, assume False
                    )
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump([v.to_json() for v in cls.objetos], arquivo, indent=4)
