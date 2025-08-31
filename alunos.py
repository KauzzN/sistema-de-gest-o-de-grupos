
class Aluno: 
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
    
    def __str__(self):
        return f"Aluno: {self.nome}, {self.idade} anos"
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "matricula": self.matricula
        }
    