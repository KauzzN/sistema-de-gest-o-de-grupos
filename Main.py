 
#Dependencias
from alunos import Alunos, Turmas
from Sistema import Sistema
from Utils import Utils
from gestor import Gestor
from professores import Professor


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

    while True:
        mostrarMenuCad()
        
        #checagem pra previnir erros
        try:
            menuCadAsk = int(input("> "))
        except ValueError:
            print("Digite um numero válido")
            continue
        match menuCadAsk:

            #cadastrar Aluno
            case 1:
                Utils.cadastrarAluno()

            #Adicionar a uma turma
            case 2:
                Utils.criarTurma()

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
                
                Utils.transferirALuno(alunoIdAsk, turmaIdAsk)

            #Listar alunos
            case 4:
                Sistema.carregar()
                Sistema.AtualizarStatus()
                #menu das listas
                mostrarMenuList()


                #checagem para previnir erros
                try:
                    #Opção escolhida pelo usuario
                    listarAsk = int(input("> "))
                except ValueError:
                    print("Digite um número válido")
                    continue

                Utils.ListarAlunos(listarAsk)

            #Adicionar concluinte unico
            case 5:
                #Pergunta o id do aluno a ser enviado para a Concluintes
                alunoID = int(input("Digite o ID do aluno: "))

                #checa se o aluno existe
                if alunoID in Sistema.alunos:
                    concluinte = Sistema.alunos[alunoID]
                else:
                    print("ID aluno não encontrado")
                    continue
                
                Utils.adicionarConcluinte(concluinte)

            #Adicionar turma concluinte
            case 6:
                #Perguntar o ID da turma
                turmaID = int(input("Digite o ID da turma: "))

                #Checando se a turma existe
                if turmaID in Sistema.turmas:
                    turmaX = Sistema.turmas[turmaID]
                else:
                    print("ID turma não encontrado")
                    continue

                Utils.AdicionarConcluintes()

            case 7:
                print("Finalizado!")
                break
        
    mostrarMenuCad()

executarCadSystem()
    
 
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


