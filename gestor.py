from dataclasses import dataclass,field
from typing import List

@dataclass
class Gestor:
    id_gestor: int
    nome_gestor: str
    email: str
    senha: str
    professores: List['Professor'] = field(default_factory=list)
    escolas: List['Escola'] = field(default_factory=list)
    turmas: List['Turmas'] = field(default_factory=list)
 
    def ToDict(self):
        return {
            "id_gestor": self.id_gestor,
            "nome_gestor": self.nome_gestor,
            "email": self.email,
            "senha": self.senha,
            "professores": [prof.id_professor for prof in self.professores],
            "escolas": [es.id_escola for es in self.escolas],
            "turmas": [t.ID_TURMA for t in self.turmas]
        }   
    
    
        



