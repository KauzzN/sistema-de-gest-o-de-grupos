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
                
                #Adicionao aluno ao banco de dados
                novo_aluno = Alunos(nome = nome)
                Sistema.alunos[novo_aluno.ID_ALUNO] = novo_aluno
                print(f"Aluno {nome} cadastrado, ID: {novo_aluno.ID_ALUNO}")

                novo_aluno.status = "inativo"

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
    def adicionarFalta(cls):
        Sistema.carregar()

        try:
            alunoIdAsk = int(input("Digite o ID do aluno: "))
        except ValueError:
            print("ID não identificado!")
            return

        aluno = Sistema.alunos.get(alunoIdAsk)
        if aluno is None:
            print("Aluno não encontrado!")
            return

        print(aluno.faltas)
        aluno.faltas += 1
        Sistema.salvar()
        print(f"Falta adicionada para aluno {aluno.nome}")
        print(aluno.faltas)


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

        #Alterando o status do aluno
        if aluno.status == "inativo":
            aluno.status = "ativo"

        #Salvando as alterações
        Sistema.salvar()
        print(f"ID: {aluno.ID_ALUNO} Aluno: {aluno.nome} transferido para turma {turma.nome}")

    @classmethod
    def transferirProf(cls):

        #Inserir os ID's do prof e da turma referente
        profIdAsk = int(input("Digite o ID do Professor: "))
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
                turmaAntiga.professores.remove(prof.id_professor) 

        #Adicionando o aluno a turma escolhida
        prof.turma = turma.ID_TURMA
        if prof.id_professor not in turma.professores:
            turma.professores.append(prof.id_professor)

        #Salvando as alterações
        Sistema.salvar()
        print(f"ID: {prof.id_professor} Aluno: {prof.nome_professor} transferido para turma {turma.nome}")
    

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

    @classmethod
    def removerProfessor(cls):
        #Dependencias
        Sistema.carregar()

        #Inserindo os dados
        try:
            profIdAsk = int(input("Digite o ID do professor: "))
            turmaIdAsk = int(input("Digite o ID da turma: "))
        except ValueError:
            print("Digite um ID válido!")
            return
        #Checando se professor existe
        prof = Sistema.professores.get(profIdAsk)
        if prof is None:
            print("ID do professor não identificado!")
            return

        #Checando se turma existe
        turma = Sistema.turmas.get(turmaIdAsk)
        if turma is None:
            print("ID da turma não identificado!")
            return

        #Checando se o professor está na turma selecionada e removendo ele
        if profIdAsk in turma.professores:
            turma.professores.remove(profIdAsk)
            print(f"Professor removido da turma: {turma.nome}!")
            Sistema.salvar()

        else:
            print("Professor não está na turma!")

    #Mudar status dos alunos de uma turma para concluintes
    @classmethod
    def adicionarConcluintes(cls):
        #Carregando banco de dados
        Sistema.carregar()

        #Inserindo o id da turma desejada
        turmaIdAsk = int(input("Digite o ID da turma: "))

        #identificando  aturma
        turma = Sistema.turmas.get(turmaIdAsk)

        #Checando se a turma existe
        if turma is None:
            print("Turma não encontrada!")
            return
        
        #Checando se a turma possui alunos
        if not turma.alunos:
            print("Essa turma não possui alunos!")
            return
        
        #iterando a turma
        for alunos in turma.alunos:
            #Identificando os alunos
            aluno = Sistema.alunos[alunos]
            #Checando se o aluno está ativo
            if aluno.status == "ativo":
                del Sistema.alunos[aluno.ID_ALUNO]
                Sistema.concluintes[aluno.ID_ALUNO] = aluno
                aluno.status = "Concluinte" 

        Sistema.salvar()


    #Listar alunos de forma separada ou conjunta
    @classmethod
    def Listar(cls):
        Sistema.carregar()
        print("""
        Oque deseja listar?
            1. Todos os alunos
            2. Listar alunos sem turma
            3. Listar por turmas
            4. Listar turmas
            5. Listar concluintes
    """)

        opcao = int(input("> "))

        match opcao:

            #Listar todos os alunos
            case 1:
                if Sistema.alunos is None:
                    print("Nenhum aluno cadastrado!")

                for ID_ALUNO, aluno in Sistema.alunos.items():
                    if aluno.turma is None:
                        print(f"Aluno: {aluno.nome} ID: {aluno.ID_ALUNO}, sem Turma")
                    else:
                        print(f"Aluno: {aluno.nome} ID: {aluno.ID_ALUNO}, turma: {aluno.turma}")

            #Listar alunos sem turmas
            case 2:
                if Sistema.alunos is None:
                    print("Nenhum aluno sem turma!")
                    return

                for ID_ALUNO, aluno in Sistema.alunos.items():
                    if aluno.turma is None:
                        print(f"Aluno: {aluno.nome} ID: {aluno.ID_ALUNO}")

            #Listar por turmas
            case 3:
                turmaIdAsk = int(input("Digite o iD da turma: "))

                turma = Sistema.turmas.get(turmaIdAsk)
                if turma is None:
                    print("Turma não encontrada!")
                    return
                
                for ID_ALUNO, aluno in turma.alunos:
                    print(f"Aluno {aluno.nome} ID: {aluno.ID_ALUNO}")

            #Listar turmas
            case 4:
                turmas = Sistema.turmas.items()
                if turmas is None:
                    print("Turma não encontrada!")
                    return
                
                for ID_TURMA, turma in Sistema.turmas.items():
                    print(f"Turma {turma.nome} ID: {turma.ID_TURMA}")

            #listar concluintes
            case 5:
                Sistema.carregar()
                concluintes = Sistema.concluintes

                if concluintes is None:
                    print("Nenhum aluno concluinte")

                for concluinte in concluintes.values():
                    print(f"{concluinte.nome} ID: {concluinte.ID_ALUNO}")



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
    9. Remover Professor
    10. Adicionar Falta
    11. Finalizar
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

                #Transferir professor
                case 6:
                    Utils.transferirProf()

                #Adicionar concluintes
                case 7:
                    Utils.adicionarConcluintes()
                    
                #Listar
                case 8:
                    Utils.Listar()
                    
                #Remover Professor
                case 9:
                    Utils.removerProfessor()

                #Adicionar Faltas
                case 10:
                    Utils.adicionarFalta()

                #Finalizar
                case 11:
                    break
