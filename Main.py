 
#Dependencias
from LoginUtils import Login
from alunos import Alunos
from alunos import Turmas
from alunos import Sistema


#login System

#Menu inicial de Login
def mostrarMenuLogin():
    print("""
    Oque deseja fazer?
        1. Cadastrar usuario
        2. Efetuar login
        3. Finalizar
""")
#Menu de gerencia dos alunos e turmas
def mostrarMenuCad():
    print("""

        1. Cadastrar aluno
        2. Criar turma  
        3. Adicionar/Transferir aluno
        4. Listar alunos/turmas
        5. Finalizar
""")
    
def mostrarMenuList():
    print("""
Oque deseja listar?
    1. Todos os alunos
    2. Listar por turma  
    3. Listar grupos
    4. Listar alunos sem grupos
    5. Listar concluintes
""")

#Sistema de cadastro e gerencia
def executarCadSystem():
    #Carrega a dataBase
    Sistema.carregar()

    mostrarMenuCad()

    while True:
        #checagem pra previnir erros
        try:
            menuCadAsk = int(input("> "))
        except ValueError:
            print("Digite um numero válido")
            continue
        match menuCadAsk:

            #cadastrar Aluno
            case 1:
                #pegando as informações do aluno
                nome = input("Qual o nome do aluno")
                novoId = Sistema.gerarIdAluno()
                
                #Adicionao aluno ao banco de dados
                novo_aluno = Alunos(novoId, nome)
                Sistema.alunos[novoId] = novo_aluno
                print(f"Aluno {nome} cadastrado, ID: {novoId}")

            #Adicionar a uma turma
            case 2:
                #pegando informações da turma
                nome = input("Qual o nome da turma")
                novoId = Sistema.gerarIdTurma()

                #Adicionando a turma ao banco de dados
                novo_grupo = Turmas(novoId, nome)
                Sistema.turmas[novoId] = novo_grupo
                print(f"Turma {nome} cadastrada. ID: {novoId}")

            #Adicionar/Transferir alunos entre grupos
            case 3:
                #Checagem para evitar erros
                try:
                    #Pegando as informações do aluno e do grupo desejado
                    alunoIdAsk = int(input("Digite o ID do aluno: > "))
                    turmaIdAsk = int(input("Digite o ID da turma: > "))
                #Prevenindo de quebra de codigo por inserir algo diferente de numeros
                except ValueError:
                    print("Digite um ID válido")
                    continue
                
                #Checa se o aluno e a turma existem no sistema
                if alunoIdAsk in Sistema.alunos and turmaIdAsk in Sistema.turmas:
                    #Identifica o aluno
                    aluno = Sistema.alunos[alunoIdAsk]
                    #Identifica a turma
                    turma = Sistema.turmas[turmaIdAsk]
                
                #Identificando a turma
                turma = Sistema.turma[turmaIdAsk]

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
                turma.alunos.append(aluno.ID_ALUNO)

                #Atualiza status automatico
                Sistema.AtualizarStatus()

                print(f"Aluno {aluno.nome} foi adicionado/transferido para turma {turma.nome}!")

            case 4:
                #menu das listas
                mostrarMenuList()
                #checagem para previnir erros
                try:
                    #Opção escolhida pelo usuario
                    listarAsk = int(input("> "))
                except ValueError:
                    print("Digite um número válido")
                    continue

                Sistema.ListarAlunos(listarAsk)

            case 5:
                print("Finalizado!")
                break
                
    
    
mostrarMenuLogin()

#login sistema
while True:

    try:
        menuAsk = int(input("> "))
    except ValueError:
        print("Digite um numero válido")
        continue

    match menuAsk:
        #Cadastrar Login
        case 1:
            email = input("Digite um email:  > ")
            senha = input("Digite uma senha: > ")
            Login.cadastrarLogin(email, senha)

        #Validar Login 
        case 2:
            email = input("Digite seu email:  > ")
            senha = input("Digite sua senha: > ")
            Login.validarLogin(email, senha)

            executarCadSystem()

        #Finalizar ação
        case 3:
            print("finalizado!")
            break
        
    mostrarMenuLogin()

