import json
from models.modelo import Modelo #classe base

class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao

#set

    def set_id(self, id):
        if (id == ""):
            raise ValueError("O ID não pode estar vazio")
        self.__id = id

    def set_descricao(self, descricao):
        if (descricao == ""):
            raise ValueError("A descrição não pode estar vazia")
        self.__descricao = descricao
        
#get

    def get_id(self):
        return self.__id
    
    def get_descricao(self):
        return self.__descricao
    
#str

    def __str__(self):
        return f"ID: {self.__id}, Categoria: {self.__descricao}"
    
    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao
        }


class Categorias(Modelo): #herdando "Modelo"

    @classmethod
    def abrir(cls):
        cls.objetos = [] 
        try:    
            with open("categorias.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Categoria(dic["id"], 
                                    dic["descricao"])
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError): #caso nao exista ou estar vazio
            pass

    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo, indent=4)