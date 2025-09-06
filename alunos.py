#Importando biblioteca de json
import json

DBFile = "DataBase.json"

class Alunos:

    #inicializador da classe
    def __init__(self, ID_ALUNO, nome):
        self.ID_ALUNO = ID_ALUNO
        self.nome = nome
        self.turma = None #quando criar a função criar_turma torcar esse valor para receber o id da turma ja criada
        self.status = None


    #Transforma um aluno em dicionario
    def ToDict(self):
        return {"id_aluno": self.ID_ALUNO, "nome": self.nome, "turma": self.turma, "status": self.status}

class Turmas:
    def __init__(self, ID_TURMA, nome_turma, id_escola):
        
    #inicializador da classe
        self.ID_TURMA = ID_TURMA
        self.nome_turma = nome_turma
        self.id_escola = id_escola
        self.lista_professor = []
        self.lista_alunos = []


    #Adiciona o aluno a turma desejada
    def addAluno(self, aluno):
        #Checa se o aluno ja está na turma
        if aluno.turma:
            Sistema.turmas[aluno.turma].alunos.remove(aluno.ID_ALUNO)
            
        #Adiciona o aluno a turma no self.turma da classe aluno
        aluno.turma = self.ID_TURMA
        #Adiciona o aluno a lista alunos no self.alunos na classe Turmas
        self.alunos.append(aluno.ID_ALUNO)


    #Transforma a turma em dicionario
    def ToDict(self):
        return{"id_turma": self.ID_TURMA, "nome": self.nome, "alunos": self.alunos}


class Sistema:
    alunos = {}
    turmas = {}
    concluintes = set()


    #Salva a turma e alunos no DataBase
    @classmethod
    def salvar(cls, arquivo = DBFile):
        #Juntando turma e alunos
        dados = {
            "alunos": {id_a: aluno.ToDict() for id_a, aluno in cls.alunos.items()},
            "turmas": {id_t: turma.ToDict() for id_t, turma in cls.turmas.items()},
            "concluintes": list(cls.concluintes)
        }

        #abrindo o arquivo "DBFile" para rescrever adicionando as turmas
        with open(arquivo, "w", encoding = "utf-8") as file:
            json.dump(dados, file, indent = 4, ensure_ascii = False)


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
    
    #Listar alunos de forma separada ou conjunta
    @classmethod
    def ListarAlunos(cls, opcao):
        #Decide qual opção o usuario irá usar
        match opcao:
            #Lista todos os alunos ativos
            case 1:
                #percorre a lista vendo todos os alunos
                for aluno in cls.alunos.values():
                    #Checa se os alunos são ativos
                    if aluno.status == "ativo":
                        #checa se os alunos não tem turmas
                        if aluno.turma is None:
                            #Diz que o aluno não possui uma turma
                            turma_nome = "sem turma"
                    
                        #nomea a turma caso o aluno possua uma
                        else:
                            turma_nome = cls.aluno[aluno.turma].nome
                    
                        #Lista todos os alunos e sua turma
                        print(f"ID: {aluno.ID_ALUNO} Nome: {aluno.nome}, Turma: {turma_nome}")
                
            
            #Lista os usuarios por turma
            case 2:
                #escolhe qual turma checar
                turmaID = int(input("Digite o ID da turma "))
                
                #Checa se a turma existe
                if turmaID not in cls.turmas:
                    print("Turma não encontrada!")
                    return

                turma = cls.turmas[turmaID]
                
                #Mostra todos os alunos na turma desejada
                for aluno in cls.alunos.values():
                    if aluno.turma == turma.ID_TURMA:
                        print(f"ID: {aluno.ID_ALUNO} Nome: {aluno.nome}")

            #Lista todas as turmas do sistema
            case 3:
                for turma in cls.turmas.values():
                    print(f"ID: {turma.ID_TURMA} Nome: {turma.nome}")

            #Lista todos os alunos sem turmas
            case 4: 
                for aluno in cls.alunos.values():
                    if aluno.turma is None:
                        print(f"ID: {aluno.ID_ALUNO} Nome: {aluno.nome} Status: {aluno.status}")

            #Lista todos os concluintes
            case 5:
                for id_aluno in cls.concluintes:
                    aluno = cls.alunos[id_aluno]
                    print(f"ID: {aluno.ID_ALUNO} Nome: {aluno.nome}")


    #Carregar o banco de dados
    @classmethod
    def carregar(cls, arquivo = DBFile):
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