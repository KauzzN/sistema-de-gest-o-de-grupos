from dataclasses import dataclass

@dataclass
class Professor:
    id_professor: int
    nome_professor: str
    
    def todict(self):
        return {
            "id_professor": self.id_professor,
            "nome_professor": self.nome_professor
        }
    
