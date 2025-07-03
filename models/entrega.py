import json
from datetime import datetime
from models.modelo import Modelo

class Entrega:
    def __init__(self, id, id_venda, id_entregador, status, data):
        self.__id = id
        self.__id_venda = id_venda
        self.__id_entregador = id_entregador
        self.__status = status
        self.__data = data

    def set_id(self, id):
        if (id < 0):
            raise ValueError("ID da entrega não pode ser vazio")
        self.__id = id
        
    def set_id_venda(self, id_venda):
        if (id_venda < 0):
            raise ValueError("ID da venda não pode ser vazio")
        self.__id_venda = id_venda
        
    def set_id_entregador(self, id_entregador):
        if (id_entregador < 0):
            raise ValueError("ID do entregador não pode ser vazio")
        self.__id_entregador = id_entregador
    
    def set_status(self, status):
        if (status == ""):
            raise ValueError("O status não pode estar vazio")
        self.__status = status

    def set_data(self, data):
        if (data > datetime.now()):
            raise ValueError("A data de entrega não pode ser maior que a atual")
        self.__data = data

    def get_id(self):
        return self.__id
    
    def get_id_venda(self):
        return self.__id_venda
    
    def get_id_entregador(self):
        return self.__id_entregador

    def get_status(self):
        return self.__status
        
    def get_data(self):
        return self.__data

    def __str__(self):
        return f"ID: {self.__id}, ID_Venda: {self.__id_venda}, Entregador: {self.__id_entregador}, Status: {self.__status}"
    
    def to_json(self):
        return {
            "id": self.__id,
            "id_venda": self.__id_venda,
            "entregador": self.__id_entregador,
            "status": self.__status,
            "data": self.__data.strftime("%d/%m/%Y %H:%M")
        }

class Entregas(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("entregas.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    data_obj = datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
                    
                    obj = Entrega(dic["id"],
                                  dic["id_venda"],
                                  dic["id_entregador"],
                                  dic["status"],
                                  data_obj)
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("entregas.json", mode="w") as arquivo:
            json.dump([e.to_json() for e in cls.objetos], arquivo, indent=4)

        