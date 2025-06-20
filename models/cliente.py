import json

class Cliente:
    def __init__(self, id, email, senha, nome, fone, e_admin):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__fone = fone
        self.__e_admin = e_admin

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

    def set_e_admin(self, e_admin):
        if not isinstance(e_admin, bool):      #se o admin não for True or False
            raise ValueError("e_admin deve ser True ou False")
        self.__e_admin = e_admin

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
    
    def get_e_admin(self):
        return self.__e_admin
    
    
#str

    def __str__(self):
        tipo = "Admin" if self.__e_admin else "Cliente"
        return f"ID: {self.__id}, Nome: {self.__nome}, Email: {self.__email}, Telefone: {self.__fone}, Tipo: {tipo}"
    
    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "fone": self.__fone,
            "e_admin": self.__e_admin
        }


class Clientes:
    objetos = []   #estático - Não tem instância
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        if (len(cls.objetos) > 0):
            m = max(cls.objetos, key=lambda c: c.get_id()).get_id()
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
        if (x is not None): 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if (x is not None): 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("clientes.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Cliente(dic["id"],
                                  dic["email"], 
                                  dic["senha"], 
                                  dic["nome"],
                                  dic["fone"],
                                  dic["e_admin"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass      

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:  #abre ou cria o "clientes.json para escrita (model ="w")
            json.dump([c.to_json() for c in cls.objetos], arquivo) #json.dump() pra escrever os dados em JSON
                                                                   #cls.objetos é a lista de instancias da class "Cliente"
                                                                   #c.to_json() método de cada objeto Cliente, transforma os dados
                                                                   # em um dicionario serializavel 
                                                                   # o [] converte os objetos "Cliente" para dicionarios JSON