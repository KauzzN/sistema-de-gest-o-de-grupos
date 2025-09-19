#Funções gerais


#Dependencias
from Sistema import Sistema
from alunos import Alunos, Turmas
from gestor import Gestor
from professores import Professor
from escolas import Escolas
from LoginUtils import Login


#Sistema de cadastro e gerencia
class Utils:

    
    #Menu inicial de Login
    @staticmethod
    def mostrarMenuLogin():
        print("""
        Oque deseja fazer?
            1. Cadastrar Gestor
            2. Efetuar login
            3. Finalizar
    """)
    #Menu de gerencia dos alunos e turmas
    @staticmethod
    def mostrarMenuCad():
        print("""
        Menu cadastro:
            1. Cadastrar aluno
            2. Cadastrar escola
            3. Cadastrar professor
            4. Cadastrar Gestor
            5. Criar turma  
            6. Adicionar/Transferir aluno
            7. Listar alunos/turmas
            8. Adicionar turma concluinte
            9. Finalizar
    """)

    @staticmethod
    def mostrarMenuList():
        print("""
        Oque deseja listar?
            1. Todos os alunos
            2. Listar por turma  
            3. Listar grupos
            4. Listar alunos sem grupos
            5. Listar concluintes
    """)

    @classmethod
    def cadastrarAluno(cls):
        #pegando as informações do aluno
                nome = input("Qual o nome do aluno: ")
                id_turma = int(input("Digite o ID da turma referida: "))

                turma = Sistema.turmas.get(id_turma)
                if turma is None:
                    print("Turma não encontrada!")
                    return
                
                #Adicionao aluno ao banco de dados
                novo_aluno = Alunos(nome = nome)
                Sistema.alunos[novo_aluno.ID_ALUNO] = novo_aluno
                print(f"Aluno {nome} cadastrado, ID: {novo_aluno.ID_ALUNO}")

                #Adiciona o aluno a uma turma
                novo_aluno.turma = turma.ID_TURMA
                if novo_aluno.ID_ALUNO not in turma.alunos:
                    turma.alunos.append(novo_aluno.ID_ALUNO)

                Sistema.salvar()

    @classmethod
    def criarTurma(cls):
        #pegando informações da turma
            nome = input("Qual o nome da turma: ")
            id_escola = input("Digite o ID da escola: ")

            #Adicionando a turma ao banco de dados
            nova_turma = Turmas(nome = nome, id_escola = id_escola)
            Sistema.turmas[nova_turma.ID_TURMA] = nova_turma
            print(f"Turma {nome} cadastrada. ID: {nova_turma.ID_TURMA}")

            Sistema.salvar()   


    @classmethod
    def transferirAluno(cls):
        #Inserir os ID's do aluno e da turma referente
        alunoIdAsk = int(input("Digite o ID do aluno: "))
        turmaIdAsk = int(input("Digite o ID da turma: "))

        #checando se o aluno existe
        aluno = Sistema.alunos.get(alunoIdAsk)
        if aluno is None:
            print("Aluno não encontrado!")
            return
        
        #Checando se a turma existe
        turma = Sistema.turmas.get(turmaIdAsk)
        if turma is None:
            print("Turma não encontrada!")
            return

        #Checando se o aluno já possui uma turma e removendo caso necessario
        if aluno.turma:
            turmaAntiga = Sistema.turmas.get(aluno.turma)
            if turmaAntiga and aluno.ID_ALUNO in turmaAntiga.alunos:
                turmaAntiga.alunos.remove(aluno.ID_ALUNO)

        #Adicionando o aluno a turma escolhida
        aluno.turma = turma.ID_TURMA
        if aluno.ID_ALUNO not in turma.alunos:
            turma.alunos.append(aluno.ID_ALUNO)

        #Salvando as alterações
        Sistema.salvar()
        print(f"ID: {aluno.ID_ALUNO} Aluno: {aluno.nome} transferido para turma {turma.nome}")

    @classmethod
    def transferirProf(cls):

        #Inserir os ID's do prof e da turma referente
        profIdAsk = int(input("Digite o ID do aluno: "))
        turmaIdAsk = int(input("Digite o ID da turma: "))

        #checando se o prof existe
        prof = Sistema.professores.get(profIdAsk)
        if prof is None:
            print("Aluno não encontrado!")
            return
        
        #Checando se a turma existe
        turma = Sistema.turmas.get(turmaIdAsk)
        if turma is None:
            print("Turma não encontrada!")
            return

        #Checando se o professor já possui uma turma e removendo caso necessario
        for id_antiga in prof.turmas:
            turmaAntiga = Sistema.turmas.get(id_antiga)
            if turmaAntiga and prof.ID_ALUNO in turmaAntiga.professores:
                turmaAntiga.professorews.remove(prof.id_professor)

        #Adicionando o aluno a turma escolhida
        prof.turma = turma.ID_TURMA
        if prof.id_professor not in turma.professores:
            turma.professores.append(prof.ID_ALUNO)

        #Salvando as alterações
        Sistema.salvar()
        print(f"ID: {prof.ID_ALUNO} Aluno: {prof.nome} transferido para turma {turma.nome}")
    

    @classmethod
    def cadastrarEscola(cls): 
        #Pegando os dados da escola a ser cadastrada
        nomeEscola = Sistema.input_nao_vazio("Digite o nome da escola: ")
        cidade = Sistema.input_nao_vazio("Digite a cidade onde está localizada: ")
        bairro = Sistema.input_nao_vazio("Digite o bairro: ")

        #Adiciona a escola ao Sistema
        escolaRegistrada = Escolas(nomeEscola, cidade, bairro)
        Sistema.escolas[escolaRegistrada.id_escola] = escolaRegistrada

        #Printa as informações e salva no banco de dados
        print(f"ID: {escolaRegistrada.id_escola} Nome: {nomeEscola} Registrada no sistema")
        Sistema.salvar()


    #Mudar status dos alunos de uma turma para concluintes
    @classmethod
    def AdicionarConcluintes(cls):
                turma = int(input("Digite o ID da turma: "))

                for aluno in Sistema.alunos.values():
                    if aluno.turma == turma.ID_TURMA:
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
        while True:
            print("""
    1. Cadastrar escola
    2. Cadastrar professor
    3. Cadastrar turma
    4. Cadastrar aluno
    5. Transferir aluno
    6. Transferir professor
    7. Adicionar Concluintes
    8. Listar Alunos
    9. Finalizar
""")
            while True:
                entrada = input("> ").strip()
                if not entrada.isdigit():
                    print("Digite um número válido!")
                    continue
                
                Ask1 = int(entrada)
                break

            match Ask1:
                #cadastrar escola
                case 1:
                    Utils.cadastrarEscola()

                #Cadastrar professor
                case 2:
                    #Pegando os dados para cadastro do professor
                    nome = Sistema.input_nao_vazio("Digite um nome: ")
                    email = Sistema.input_nao_vazio("DIgite um email: ")
                    senha = Sistema.input_nao_vazio("Digite uma senha: ")
                    id_turma = int(input("digite o ID da turma referida: "))

                    #Salva o cadastro no banco de dados
                    Login.cadastrarProfessor(nome, email, senha, id_turma)

                #cadastra a turma
                case 3:
                    Utils.criarTurma()
                    
                #Cadastrar aluno
                case 4:
                    Utils.cadastrarAluno()
                
                #Transferir aluno
                case 5:
                    Utils.transferirAluno()

                #Adicionar concluintes 
                case 6:
                    #inserir a turma a ser concluinte
                    turma = int(input("Digite o ID da turma: "))

                    Utils.AdicionarConcluintes(turma)

                #Listar alunos
                case 7:
                    Utils.mostrarMenuList()
                    listarAsk = int(input("> "))

                    Utils.ListarAlunos(listarAsk)
                    
                case 8:
                    break

