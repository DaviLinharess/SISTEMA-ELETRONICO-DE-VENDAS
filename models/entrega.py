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
        