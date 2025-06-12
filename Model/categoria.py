import json

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


class Categorias:
    objetos = []   # Não tem instância
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        if len(cls.objetos) > 0:
            m = max(cls.objetos, key=lambda x: x.get_id()).get_id()
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
            with open("categorias.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Categoria(dic["id"], 
                                    dic["descricao"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo)

    
    