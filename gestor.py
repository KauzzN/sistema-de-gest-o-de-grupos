

class Gestor:
    def __init__(self, ID_GESTOR, nome, email, senha):
        self.id_gestor = ID_GESTOR
        self.nome_gestor = nome
        self.email = email
        self.senha = senha
        self.professores = []
        self.escolas = []
        self.turmas = []

    def Todict(self):
        return {
            "id_gestor": self.id_gestor,
            "nome_gestor": self.nome_gestor,
            "professores": [prof.todict() for prof in self.professores],
            "escolas": [es.toDict() for es in self.escolas]
        }   
    
    
        



