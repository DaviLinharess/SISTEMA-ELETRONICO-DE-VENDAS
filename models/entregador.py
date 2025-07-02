import json
from models.modelo import Modelo

class Entregador:
    def __init__(self, id, nome, email, senha, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__fone = fone

#começa os set's

    def set_id(self, id):
        if (id == ""):
            raise ValueError("ID não pode estar vazio")
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode estar vazio")
        self.__nome = nome

    def set_email(self, email):
        if (email == ""):
            raise ValueError("Email não pode estar vazio")
        self.__email = email

    def set_senha(self, senha):
        if (senha == ""):
            raise ValueError("Senha não pode estar vazia")
        self.__senha = senha

    def set_fone(self, fone):
        if fone == "":
            raise ValueError("Telefone não pode estar vazio")
        self.__fone = fone


#começa os get's
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
    
    def get_senha(self):
        return self.__senha
    
    def get_fone(self):
        return self.__fone
    
    
    
#str

    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, Email: {self.__email}"
    
    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "fone": self.__fone
        }

class Entregadores(Modelo):

    def abrir(cls):
        cls.objetos = []
        try:     
            with open("entregadores.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Entregador(id=dic["id"],
                                    nome=dic["nome"],
                                    email=dic["email"],
                                    senha=dic["senha"],
                                    fone=dic["fone"]
                                    )
                        
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def salvar(cls):
        with open("entregadores.json", mode="w") as arquivo:
            json.dump([e.to_json() for e in cls.objetos], arquivo, indent=4)