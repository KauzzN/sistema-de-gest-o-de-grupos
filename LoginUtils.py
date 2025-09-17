#Dependencias
from professores import Professor
from gestor import Gestor
from Sistema import Sistema

import json
import os

DBLfile = "DataBaseLogin.json"

class Login:    

    #Cadastrar o login do professor
    @staticmethod
    def cadastrarProfessor(nome, email, senha):
        #carrega os dados do "banco de dados"
        dados = Login.carregarLogins()

        #checa no banco de dados todos os logins cadastrados
        for prof in dados["professores"].values():
            #checa se existe um email ja cadastrado
            if prof["email"] == email:
                print("Email já está cadastrado!")
                return False
        
        #identifica o profesor por um ID
        novo_ID = Sistema.gerarIdProf()
        professor = Professor(novo_ID, email, senha, nome)

        #salva o professor no banco de dados
        dados ["professores"][str(novo_ID)] = professor.ToDict()
        Sistema.salvarLogin(dados)


        #adiciona o ID do professor ao dicionario Professores no sistema
        Sistema.professores[novo_ID] = professor
        print(f"Professor {nome} cadastrado com sucesso!")
        return True

    #Cadastra Login do gestor
    @staticmethod
    def cadastrarGestor(nome, email, senha):
       #Carrega o banco de dados
        dados = Sistema.carregarLogins()

        #identifica cada gestor no banco de dados
        for ges in dados["gestores"].values():
            #checa se existe um email ja cadastrado no banco de dados
            if ges["email"] == email:
                print("Email já cadastrado!")
                return False

        #identifica o gestor por um novo ID
        novo_ID = Sistema.gerarIdGestor()
        gestor = Gestor(novo_ID, nome, email, senha)

        #salva o login no banco de dados
        dados ["gestores"][str(novo_ID)] = gestor.ToDict()
        Sistema.salvarLogin(dados)

        #adiciona o ID do gestor ao dicionario Gestores no sistema
        Sistema.gestores[novo_ID] = gestor
        print(f"Gestor {nome} cadastrado com sucesso!")

    #Validar o usuario
    @staticmethod
    def validarLogin(email, senha):
        #Carrega o banco de dados
        dados = Sistema.carregarLogins()

        #Le todos os professores no banco de dados
        for prof_data in dados["professores"].values():
            #CHeca se o email e senha inseridos são válidos
            if prof_data["email"] == email and prof_data["senha"] ==senha:
                print(f"Login bem-sucedido! Bem-vindo Professor {prof_data['nome_professor']}")
                return Professor(**prof_data)
            
        #Le todos os gestores do banco de dados
        for gestor_data in dados["gestores"].values():
            #Checa se o email e senha inseridos são válidos
            if gestor_data["email"] == email and gestor_data["senha"] == senha:
                print(f"Login bem-sucedido! Bem-vindo Gestor {gestor_data['nome_gestor']}")
                return Gestor(**gestor_data)
        
        print("Usuario ou senha incorretos!")
        return None