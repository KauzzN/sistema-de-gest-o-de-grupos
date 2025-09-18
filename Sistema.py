#Dependencias
from escolas import Escolas
import json
import os

DBFile = "DataBase.json"
DBLfile = "DataBAseLogin.json"

class Sistema:
    alunos = {}
    turmas = {}
    escolas = {}
    professores = {}
    gestores = {}
    concluintes = set()


    #Salva a turma e alunos no DataBase
    @classmethod
    def salvar(cls):
        #Juntando turma e alunos
        dados = {
            "alunos": {id_a: aluno.ToDict() for id_a, aluno in cls.alunos.items()},
            "turmas": {id_t: turma.ToDict() for id_t, turma in cls.turmas.items()},
            "escolas": {id_e: escola.ToDict() for id_e, escola in cls.escolas.items()},
            "professores": {str(id_p): professor.ToDict() for id_p, professor in cls.professores.items()},
            "gestores": {str(id_g): gestor.ToDict() for id_g, gestor in cls.gestores.items()},
            "concluintes": list(cls.concluintes)
        }

        #abrindo o arquivo "DBFile" para rescrever adicionando as turmas
        with open(DBFile, "w", encoding = "utf-8") as file:
            json.dump(dados, file, indent = 4, ensure_ascii = False)


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

    #Carregar o banco de dados
    @classmethod
    def carregar(cls):
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
            "concluintes": list(cls.concluintes),
            "professores": {id_p: professor.ToDict() for id_p, professor in cls.professores.items()},
            "gestores": {id_g: gestor.ToDict() for id_g, gestor in cls.gestores.items()}
        }

        with open(DBFile, "w", encoding="utf-8") as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)

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

    #Gerando ID automatico do aluno
    @classmethod
    def gerarIdAluno(cls):
        #Checagem pra saber se o dicionario Alunos possui algum aluno cadastrado
        if not cls.alunos:
            return 1

        #Pega o maior Id do dicionario Alunos e soma +1
        return max(cls.alunos.keys()) + 1
    
    #Gerando ID automatico da turma]
    @classmethod
    def gerarIdTurma(cls):
        #checagem pra saber se o dicionario Turmas possui algum aluno cadastrado
        if not cls.turmas:
            return 1
        
        return max(cls.turmas.keys()) + 1
        #Pega o maior Id do dicionario Turmas e soma +1

    @classmethod
    def gerarIdEscola(cls):
        #checando se o dicionario Escolas possui alguma ja datada
        if not cls.escolas:
            return 1
        
        #Pega o numero maximo de escolas por ID
        return max(cls.escolas.keys()) + 1
    
    @classmethod
    def gerarIdProf(cls):
        #checando se o dicionario Professores possui alguma ja datada
        if not cls.professores:
            return 1
        
        #Pega o numero maximo de escolas por ID
        return max(cls.professores.keys()) + 1
    
    @classmethod
    def gerarIdGestor(cls):
        #checando se o dicionario Professores possui alguma ja datada
        if not cls.gestores:
            return 1
        
        #Pega o numero maximo de escolas por ID
        return max(cls.gestores.keys()) + 1
    
    
    @staticmethod
    def input_nao_vazio(msg):
        while True:
            valor = input(msg).strip()
            if valor:
                return valor
            print("O campo não pode ficar vazio!")