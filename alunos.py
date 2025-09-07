#Dependencias
from Sistema import Sistema


#Importando biblioteca de json
import json

DBFile = "DataBase.json"

class Alunos:

    #inicializador da classe
    def __init__(self, ID_ALUNO, nome):
        self.ID_ALUNO = ID_ALUNO
        self.nome = nome
        self.turma = None
        self.status = None


    #Transforma um aluno em dicionario
    def ToDict(self):
        return {"id_aluno": self.ID_ALUNO, "nome": self.nome, "turma": self.turma, "status": self.status}


class Turmas:

    #inicializador da classe
    def __init__(self, ID_TURMA, nome):
        self.ID_TURMA = ID_TURMA
        self.nome = nome
        self.alunos = []


    #Adiciona o aluno a turma desejada
    def addAluno(self, aluno):
        #Checa se o aluno ja está na turma
        if aluno.turma:
            Sistema.turmas[aluno.turma].alunos.remove(aluno.ID_ALUNO)
            
        #Adiciona o aluno a turma no self.turma da classe aluno
        aluno.turma = self.ID_TURMA
        #Adiciona o aluno a lista alunos no self.alunos na classe Turmas
        self.alunos.append(aluno.ID_ALUNO)


    #Transforma a turma em dicionario
    def ToDict(self):
        return{"id_turma": self.ID_TURMA, "nome": self.nome, "alunos": self.alunos}


