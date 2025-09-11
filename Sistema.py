#Dependencias
from escolas import Escolas
import json
import os

DBFile = "DataBase.json"
DBLfile = "DataBaseLogin.json"

class Sistema:
    alunos = {}
    turmas = {}
    escolas = {}
    professores = {}
    gestores = {}
    concluintes = set()


    #Salva a turma e alunos no DataBase
    @classmethod
    def salvar(cls, arquivo = DBFile):
        #Juntando turma e alunos
        dados = {
            "alunos": {id_a: aluno.ToDict() for id_a, aluno in cls.alunos.items()},
            "turmas": {id_t: turma.ToDict() for id_t, turma in cls.turmas.items()},
            "escolas": {id_e: escola.ToDict() for id_e, escola in cls.escolas.items()},
            "concluintes": list(cls.concluintes)
        }

        #abrindo o arquivo "DBFile" para rescrever adicionando as turmas
        with open(arquivo, "w", encoding = "utf-8") as file:
            json.dump(dados, file, indent = 4, ensure_ascii = False)


    @staticmethod
    def carregarLogins():
        if not os.path.exists(DBLfile):
            return {"professores": {}, "gestores": {}}
        try:
            with open(DBLfile, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Caso o arquivo esteja vazio ou corrompido
            return {"professores": {}, "gestores": {}}

    @staticmethod
    def salvarLogin(professores=None, gestores=None):
        dados = Sistema.carregarLogins()
        professores = professores or {}
        gestores = gestores or {}
        
        # Atualiza dados existentes
        for id_p, prof in professores.items():
            dados["professores"][str(id_p)] = prof.ToDict()
        for id_g, ges in gestores.items():
            dados["gestores"][str(id_g)] = ges.ToDict()

        with open(DBLfile, "w", encoding="utf-8") as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)

            


    #Atualizar status dos alunos
    @staticmethod
    def AtualizarStatus():
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
    def carregar(cls, arquivo = DBFile):
        #Dependencias
        from alunos import Alunos, Turmas
        try:
            #abre o arquivo "DBFile" para
            with open(arquivo, "r", encoding = "utf-8") as file:
                dados = json.load(file)

            #identifica o aluno dentro da dataBase
            cls.alunos = {
                int(id_a): Alunos(int(id_a), info["nome"])
                for id_a, info in dados.get("alunos", {}).items()
            }
            for id_a, info in dados.get("alunos", {}).items():
                cls.alunos[int(id_a)].turma = info["turma"]

            #identifica a classe dentro da dataBase
            cls.turmas = {
                int(id_t): Turmas(int(id_t), info["nome"])
                for id_t, info in dados.get("turmas", {}).items()
            }
            for id_t, info in dados.get("turmas", {}).items():
                cls.turmas[int(id_t)].alunos = info["alunos"]

            cls.concluintes = set(dados.get("concluintes", []))

        
        #checagem para não dar erro caso o aluno e a turma não seja encontrado
        except FileNotFoundError:
            cls.alunos, cls.turmas, cls.concluintes = {}, {}, set()
    

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
        if not cls.gestores:
            return 1
        
        return max(cls.gestores.keys()) + 1
    
    
    @staticmethod
    def input_nao_vazio(msg):
        while True:
            valor = input(msg).strip()
            if valor:
                return valor
            print("O campo não pode ficar vazio!")