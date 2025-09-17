 
#Dependencias
from alunos import Alunos, Turmas
from LoginUtils import Login
from Sistema import Sistema
from Utils import Utils
from gestor import Gestor
from professores import Professor
from escolas import Escolas



#login sistema
while True:
    Utils.mostrarMenuLogin()
    menuAsk1 = int(input("> "))

    match menuAsk1:
        #Cadastrar gestor
        case 1:
            #Pegando as informações de cadastro
            nome = Sistema.input_nao_vazio("Digite seu nome: ").strip()
            email = Sistema.input_nao_vazio("Digite seu email: ").strip()
            senha = Sistema.input_nao_vazio("Digite sua senha: ").strip()

            #Salvando o cadastro no banco de dados
            Login.cadastrarGestor(nome, email, senha)

        #Validar Login 
        case 2:
            email = Sistema.input_nao_vazio("Digite seu email: ")
            senha = Sistema.input_nao_vazio("Digite sua senha: ")

            usuario = Login.validarLogin(email, senha)

            if usuario is None:
                print("Login inválido!")
                continue
            
            if usuario.__class__.__name__=="Gestor":
                Utils.PainelGestão()
            
            
        case 3:
            break