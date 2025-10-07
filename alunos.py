


#Importando biblioteca de json
from dataclasses import dataclass, field
from typing import List
import json


@dataclass
class Alunos:
    
    ID_ALUNO: int = None #type: ignore
    nome: str = ""
    turma: int = None #type: ignore
    status: str = ""
    faltas: int = 0

    _next_id: int = field(init = False, default = 1, repr = False)

    def __post_init__(self):
        if self.ID_ALUNO is None:
            self.ID_ALUNO = Alunos._next_id
            Alunos._next_id += 1

    #Transforma um aluno em dicionario
    def ToDict(self):
        return {
            "id_aluno": self.ID_ALUNO,
            "nome": self.nome, 
            "turma": self.turma, 
            "status": self.status,
            "faltas": self.faltas
        }

@dataclass
class Turmas:

    ID_TURMA: int = None #type: ignore
    nome: str = ""
    professores: List[int] = field(default_factory=list)
    alunos: List[int] = field(default_factory=list)
    id_escola: int = None #type: ignore

    _next_id: int = field(init = False, default = 1, repr = False)

    def __post_init__(self):
        if self.ID_TURMA is None:
            self.ID_TURMA = Turmas._next_id
            Turmas._next_id += 1
        
        #Impedindo de alunos e professores vir como None
        if self.professores is None:
            self.professores = []
        if self.alunos is None:
            self.alunos = []
    

    #Transforma a turma em dicionario
    def ToDict(self):
        return{
            "id_turma": self.ID_TURMA,
            "nome": self.nome,
            "professores": self.professores,
            "alunos": self.alunos,
            "id_escola": self.id_escola
            }


