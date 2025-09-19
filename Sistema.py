#Dependencias
from escolas import Escolas
import json
import os

DBFile = "DataBase.json"    

class Sistema:
    alunos = {}
    turmas = {}
    escolas = {}
    professores = {}
    gestores = {}
    concluintes = set()

    # Salvar tudo em um único JSON
    @classmethod
    def salvar(cls):
        dados = {
            "alunos": {id_a: aluno.ToDict() for id_a, aluno in cls.alunos.items()},
            "turmas": {id_t: turma.ToDict() for id_t, turma in cls.turmas.items()},
            "escolas": {id_e: escola.ToDict() for id_e, escola in cls.escolas.items()},
            "professores": {id_p: professor.ToDict() for id_p, professor in cls.professores.items()},
            "gestores": {id_g: gestor.ToDict() for id_g, gestor in cls.gestores.items()},
            "concluintes": list(cls.concluintes)
        }

        with open(DBFile, "w", encoding = "utf-8") as file:
            json.dump(dados, file, indent = 4, ensure_ascii = False)

    # Carregar todos os dados
    @classmethod
    def carregar(cls):
        from alunos import Alunos, Turmas
        from professores import Professor
        from gestor import Gestor

        if not os.path.exists(DBFile):
            cls.alunos, cls.turmas, cls.escolas, cls.professores, cls.gestores, cls.concluintes = {}, {}, {}, {}, {}, set()
            return

        with open(DBFile, "r", encoding="utf-8") as file:
            dados = json.load(file)

        cls.alunos = {
            int(id_a): Alunos(int(id_a), info["nome"])
            for id_a, info in dados.get("alunos", {}).items()
        }
        for id_a, info in dados.get("alunos", {}).items():
            cls.alunos[int(id_a)].turma = info["turma"]

        cls.turmas = {
            int(id_t): Turmas(
            int(id_t),
            info["nome"],
            info.get("id_escola", None)  # <-- usa None se não existir
        )
        for id_t, info in dados.get("turmas", {}).items()
        }

        cls.escolas = {
                int(id_e): Escolas(int(id_e), info["nome_escola"], info["cidade"], info["bairro"])
                for id_e, info in dados.get("escolas", {}).items()
        }
        cls.concluintes = set(dados.get("concluintes", []))

        cls.professores = {
            int(id_p): Professor(**prof) for id_p, prof in dados.get("professores", {}).items()
        }
        cls.gestores = {
            int(id_g): Gestor(**ges) for id_g, ges in dados.get("gestores", {}).items()
        }

    #Atualizar status dos alunos
    @classmethod
    def AtualizarStatus(cls):
        #Lê todos os IDS de alunos e atualiza seu status para "ativo" ou "inativo"
        for id_aluno, aluno in Sistema.alunos.items():
            #checa se o aluno está em uma turma mas não concluiu
            if aluno.turma is not None and aluno.ID_ALUNO not in Sistema.concluintes:
                #Atualiza o status para ativo
                aluno.status = "ativo"
            #Checa se o aluno ja concluiu
            elif aluno.ID_ALUNO in Sistema.concluintes:
                #Atualiza o status para inativo
                aluno.status = "inativo"
            #Se não estiver em uma turma, nem em ter concluido, status volta par None
            else:
                aluno.status = None


    @classmethod
    def _gerarId(cls, collection):
        if not collection:
            return 1
        return max(collection.keys()) + 1

    @classmethod
    def gerarIdAluno(cls):
        return cls._gerarId(cls.alunos)

    @classmethod
    def gerarIdTurma(cls):
        return cls._gerarId(cls.turmas)

    @classmethod
    def gerarIdEscola(cls):
        return cls._gerarId(cls.escolas)

    @classmethod
    def gerarIdProf(cls):
        return cls._gerarId(cls.professores)

    @classmethod
    def gerarIdGestor(cls):
        return cls._gerarId(cls.gestores)

    
    
    @staticmethod
    def input_nao_vazio(msg):
        while True:
            valor = input(msg).strip()
            if valor:
                return valor
            print("O campo não pode ficar vazio!")