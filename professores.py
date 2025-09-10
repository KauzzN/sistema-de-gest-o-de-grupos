from dataclasses import dataclass, field
from typing import List

@dataclass
class Professor:
    id_professor: int
    email: str
    senha: str 
    nome_professor: str 
    turmas: List["Turmas"] = field(default_factory=list)
                 
    
    def ToDict(self):
        return {
            "id_professor": self.id_professor,
            "email": self.email,
            "senha": self.senha,
            "nome_professor": self.nome_professor,
            "turmas": self.turmas
        }
    
