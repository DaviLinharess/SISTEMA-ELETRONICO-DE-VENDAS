import json
from abc import ABC, abstractmethod

class Modelo(ABC):
    #persistencia de dados
    
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for x in cls.objetos:
            if (x.get_id() > m): 
                m = x.get_id()

        obj.set_id(m + 1)
            
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if (obj.get_id() == id):
                return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x is not None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x is not None:
            cls.objetos.remove(x)
            cls.salvar()

    #toda classe filha vai ser obrigada a implementar
    @classmethod
    @abstractmethod
    def salvar(cls):
        pass