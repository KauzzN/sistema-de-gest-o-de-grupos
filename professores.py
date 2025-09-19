from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Professor:
    
    id_professor: Optional[int] = None
    email: str = ""
    senha: str = ""
    nome_professor: str = ""
    turmas: List[int] = field(default_factory=list)

    _next_id: int = field(init=False, default=1, repr=False)
                 
    def __post_init__(self):
        if self.id_professor is None:
            self.id_professor = Professor._next_id
            Professor._next_id += 1

    def ToDict(self):
        return {
            "id_professor": self.id_professor,
            "email": self.email,
            "senha": self.senha,
            "nome_professor": self.nome_professor,
            "turmas": self.turmas
        }
    
