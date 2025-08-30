import json

DBFile = "DataBase.json"

class Login:

    #Carregar o banco de dados
    @staticmethod
    def carregarLogins():
        
        try:
            with open(DBFile, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    #Salvar o login no banco de dados
    @staticmethod
    def salvarLogin(usuarios):

        with open(DBFile, "w") as file:
            json.dump(usuarios, file, indent=4)

    #Validar o usuario
    @staticmethod
    def validarLogin(email, senha):
        usuarios = Login.carregarLogins()
        if email in usuarios and usuarios[email] == senha:
            print("Login bem sucedido!")
            return True
        print("Usuario ou senha incorreto!")
        return False

    #Cadastrar Login
    @staticmethod
    def cadastrarLogin(email, senha):
        usuarios = Login.carregarLogins()
        if email in usuarios:
            print("Esse usuario ja existe!")
            return False
        usuarios[email] = senha
        Login.salvarLogin(usuarios)
        print("Cadastro realizado com sucesso!")
        return True