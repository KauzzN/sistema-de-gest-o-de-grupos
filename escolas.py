from dataclasses import dataclass, field
from typing import List

@dataclass
class Escolas:

    nome_escola: str = ""
    cidade: str = ""
    bairro: str = ""
    id_escola: int = None
    turmas: List[int] = field(default_factory = list)

    _next_id: int = field(init = False, default = 1, repr = False )
    

    def __post_init__(self):
        if self.id_escola is None:
            self.id_escola = Escolas._next_id
            Escolas._next_id += 1

    def ToDict(self):
        return {
            "id_escola": self.id_escola,
            "nome_escola": self.nome_escola, 
            "cidade": self.cidade,
            "bairro": self.bairro
        } 