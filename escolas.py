from dataclasses import dataclass

@dataclass
class Escolas:
    id_escola: int
    nome_escola: str 
    cidade: str 
    bairro: str 
    turmas = []

    def ToDict(self):
        return {
            "id_escola": self.id_escola,
            "nome_escola": self.nome_escola, 
            "cidade": self.cidade,
            "bairro": self.bairro
        } 