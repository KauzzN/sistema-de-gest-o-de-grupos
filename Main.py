 
#Dependencias
from LoginUtils import Login


#login System

def mostrarMenu():
    print("""
    Oque deseja fazer?
        1. Cadastrar usuario
        2. Efetuar login
        3. Finalizar
""")
    
mostrarMenu()

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

        #Finalizar ação
        case 3:
            print("finalizado!")
            break
        
    mostrarMenu()

