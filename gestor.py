from dataclasses import dataclass, field
from typing import List
from professores import Professor
from escola import Escola

@dataclass
class Gestor:
    id_gestor: int
    nome_gestor: str
    professores: List[Professor] = field(default_factory=list)
    escolas: List[Escola] = field(default_factory=list)

    def todict(self):
        return {
            "id_gestor": self.id_gestor,
            "nome_gestor": self.nome_gestor,
            "professores": [prof.todict() for prof in self.professores],
            "escolas": [es.toDict() for es in self.escolas]
        }   
    
    def cadastrar_professor(self):
        nome_prof = input("Digite o nome do novo professor: ")
        id_prof = len(self.professores) + 1
        novo_professor = Professor(id_prof, nome_prof)
        self.professores.append(novo_professor)
        print(f"Professor {nome_prof} possui o id {id_prof:03d}")
        return novo_professor
    

gestor = Gestor(id_gestor=5, nome_gestor="Caua")
gestor.cadastrar_professor()


