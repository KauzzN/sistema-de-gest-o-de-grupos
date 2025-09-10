from dataclasses import dataclass, field
from typing import List
from professores import Professor
from escolas import Escola
from alunos import Turmas, Alunos

@dataclass
class Gestor:
    id_gestor: int
    nome_gestor: str
    professores: List[Professor] = field(default_factory=list)
    escolas: List[Escola] = field(default_factory=list)
    turmas: List[Turmas] = field(default_factory=list)
    alunos:List[Alunos] = field(default_factory=list)

    def Tdict(self):
        return {
            "id_gestor": self.id_gestor,
            "nome_gestor": self.nome_gestor,
            "professores": [prof.todict() for prof in self.professores],
            "escolas": [es.toDict() for es in self.escolas]
        }   
    
    def cadastrar_escola(self):
        nome_escola = input("Digite o nome da escola: ")
        cidade = input("Digite o nome da cidade onde fica a escola: ")
        bairro = input("Digite o nome do Bairro onde fica a escola: ")
        id_escola = len(self.escolas) + 1
        escola_registrada = Escola(id_escola, nome_escola, cidade, bairro)
        self.escolas.append(escola_registrada)
        print(f"A escola {nome_escola} possui o id {id_escola:02d}")
        return escola_registrada

    def cadastrar_professor(self):
        nome_prof = input("Digite o nome do novo professor: ")
        id_prof = len(self.professores) + 1
        novo_professor = Professor(id_prof, nome_prof)
        self.professores.append(novo_professor)
        print(f"Professor {nome_prof} possui o id {id_prof:03d}")
        return novo_professor
    
    def cadastrar_turma(self, id_escola):
        nome_turma = input("Digite o nome da nova turma: ")
        id_turma = len(self.turmas) + 1 
        nova_turma = Turmas(id_turma, nome_turma, id_escola)
        print(f"A turma {nome_turma} possui o id {id_turma}")
        return nova_turma
    
    def cadastrar_aluno(self):
        nome_aluno = input("Digite o nome do novo aluno: ")
        id_aluno = len(self.alunos) + 1
        novo_aluno = Alunos(id_aluno, nome_aluno)
        print(f"O aluno {nome_aluno} possui o id {id_aluno:04d} ")
        return novo_aluno
        
gestor = Gestor(id_gestor=5, nome_gestor="Caua")
escola = Escola(id_escola=1, nome_escola="Lafayete", cidade="Itambe", bairro="carice")

gestor.cadastrar_professor()
gestor.cadastrar_escola()
gestor.cadastrar_turma(escola.id_escola)
gestor.cadastrar_aluno()



