#Funções gerais


#Dependencias
from Sistema import Sistema
from alunos import Alunos, Turmas
from gestor import Gestor
from professores import Professor
from escolas import Escolas


#Sistema de cadastro e gerencia
class Utils:

    @classmethod
    def cadastrarAluno(cls):
        #pegando as informações do aluno
                nome = input("Qual o nome do aluno: ")
                novoId = Sistema.gerarIdAluno()
                
                #Adicionao aluno ao banco de dados
                novo_aluno = Alunos(novoId, nome)
                Sistema.alunos[novoId] = novo_aluno
                print(f"Aluno {nome} cadastrado, ID: {novoId}")

                Sistema.salvar()

    @classmethod
    def criarTurma(cls):
        #pegando informações da turma
            nome = input("Qual o nome da turma: ")
            novoId = Sistema.gerarIdTurma()

            #Adicionando a turma ao banco de dados
            novo_grupo = Turmas(novoId, nome)
            Sistema.turmas[novoId] = novo_grupo
            print(f"Turma {nome} cadastrada. ID: {novoId}")

            Sistema.salvar()    
    
    #Adicionar/Transferir alunos entre grupos
    @classmethod
    def transferirALuno(cls, alunoIdAsk, turmaIdAsk):
                
            while True:
                #Checa se o aluno existe no sistema
                if alunoIdAsk not in Sistema.alunos:
                    print("Aluno não encontrado!")
                    return
                
                #Checa se a turma existe no Sistema
                if turmaIdAsk not in Sistema.turmas:
                    print("Turma não encontrada!")
                    return
                
                    #Identifica o aluno
                aluno = Sistema.alunos[alunoIdAsk]

                    #Identifica a turma
                turma = Sistema.turmas[turmaIdAsk]

                #Checando se o aluno já possui uma turma
                if aluno.turma is not None:

                    #identificando a turma do aluno
                    turmaAntiga = Sistema.turmas[aluno.turma]

                    #identifica e remove o aluno da turma
                    if aluno.ID_ALUNO in turmaAntiga.alunos:
                        turmaAntiga.alunos.remove(aluno.ID_ALUNO)

                #Adiciona o iD da turma ás informações do aluno
                aluno.turma = turma.ID_TURMA

                #Adiciona o aluno ás informações da turma
                if aluno.ID_ALUNO not in turma.alunos:
                       turma.alunos.append(aluno.ID_ALUNO)

                #Atualiza status automatico
                Sistema.AtualizarStatus()

                print("")
                print(f"Aluno {aluno.nome} foi adicionado/transferido para turma {turma.nome}!")

                Sistema.salvar()        

    #Mudar o status do aluno para concluinte
    @classmethod
    def adicionarConcluinte(cls, concluinte):
            #Adicionar concluinte unico
                
                #Adiciona o aluno ao sistema Concluintes 
                Sistema.concluintes.add(concluinte.ID_ALUNO)
                print(f"ID: {concluinte.ID_ALUNO} Aluno: {concluinte.nome} adicionado a CONCLUINTES")

                Sistema.AtualizarStatus()
                Sistema.salvar()

    #Mudar status dos alunos de uma turma para concluintes
    @classmethod
    def AdicionarConcluintes(cls, turmaX):

                for aluno in Sistema.alunos.values():
                    if aluno.turma == turmaX.ID_TURMA:
                        Sistema.concluintes.add(aluno.ID_ALUNO)
                        print("ID: {aluno.ID_ALUNO} Nome: {aluno.nome} adicionado a concluintes ")

                Sistema.AtualizarStatus()
                Sistema.salvar()

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

    @staticmethod
    def PainelGestão():
        painelAsk = int(input("Digite um numero")) 
        match painelAsk:
            #Menu Gestor
            case 1:
                while True:
                    print("""
    1. Cadastrar escola
    2. Cadastrar professor
    3. Cadastrar turma
    4. Cadastrar aluno
    5. Transferir aluno
    6. Adicionar Concluintes
    7. Listar Alunos
""")
                    Ask1 = int(input("> "))
                    match Ask1:
                        case 1:
                            
                            #Pegando os dados da escola a ser cadastrada
                            nomeEscola = Sistema.input_nao_vazio("Digite o nome da escola: ")
                            cidade = Sistema.input_nao_vazio("Digite a cidade onde está localizads: ")
                            bairro = Sistema.input_nao_vazio("Digite o bairro: ")

                            #Gera um ID unico
                            id_escola = Sistema.gerarIdEscola()

                            #Adiciona a escola ao Sistema
                            escolaRegistrada = Escolas(id_escola, nomeEscola, cidade, bairro)
                            Sistema.escolas[id_escola] = escolaRegistrada

                            #Printa as informações e salva no banco de dados
                            print(f"ID: {id_escola} Nome: {nomeEscola} Registrada no sistema")
                            Sistema.salvar()

                        case 2:
                            
                            #pegando informações da turma
                            nome = Sistema.input_nao_vazio("Qual o nome da turma: ")
                            novoId = Sistema.gerarIdTurma()

                            #Adicionando a turma ao banco de dados
                            novo_grupo = Turmas(novoId, nome)
                            Sistema.turmas[novoId] = novo_grupo

                            print(f"Turma {nome} cadastrada. ID: {novoId}")
                            Sistema.salvar()



                        case 3:
                            pass
                         
                        case 4:
                            pass
                        
                        case 5:
                            pass
                         
                        case 6:
                            pass
                        
                        case 7:
                            pass
                         
                        case 8:
                            pass


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
