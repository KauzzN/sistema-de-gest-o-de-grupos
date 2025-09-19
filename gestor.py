from dataclasses import dataclass,field
from typing import List, Optional

@dataclass
class Gestor:
    nome_gestor: str
    email: str = ""
    senha: str = ""
    id_gestor: Optional[int] = None
    professores: List[int] = field(default_factory=list)
    escolas: List[int] = field(default_factory=list)
    turmas: List[int] = field(default_factory=list)

    _next_id: int = field(init = False, default = 1, repr = False)

    def __post_init__(self):
        if self.id_gestor is None:    
            self.id_gestor = Gestor._next_id
            Gestor._next_id += 1
 
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
    
    
        



