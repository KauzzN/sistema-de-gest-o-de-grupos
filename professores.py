from dataclasses import dataclass

@dataclass
class Professor:
    id_professor: int
    nome_professor: str
    turmas = []
    
    def Todict(self):
        return {
            "id_professor": self.id_professor,
            "nome_professor": self.nome_professor
        }
    
