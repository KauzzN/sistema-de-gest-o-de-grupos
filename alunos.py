


#Importando biblioteca de json
import json

DBFile = "DataBase.json"

class Alunos:

    #inicializador da classe
    def __init__(self, ID_ALUNO, nome):
        self.ID_ALUNO = ID_ALUNO
        self.nome = nome
        self.turma = None #quando criar a função criar_turma torcar esse valor para receber o id da turma ja criada
        self.status = None


    #Transforma um aluno em dicionario
    def ToDict(self):
        return {"id_aluno": self.ID_ALUNO, "nome": self.nome, "turma": self.turma, "status": self.status}

class Turmas:
    def __init__(self, ID_TURMA, nome_turma, id_escola):
        
    #inicializador da classe
        self.ID_TURMA = ID_TURMA
        self.nome_turma = nome_turma
        self.id_escola = id_escola
        self.lista_professor = []
        self.lista_alunos = []


    #Adiciona o aluno a turma desejada
    def addAluno(self, aluno):
        #Dependencias
        from Sistema import Sistema

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


