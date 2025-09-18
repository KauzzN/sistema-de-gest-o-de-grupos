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
        Sistema.carregar()

        #checa no banco de dados todos os logins cadastrados
        for prof in Sistema.professores.values():
            #checa se existe um email ja cadastrado
            if prof.email == email:
                print("Email já está cadastrado!")
                return False
        
        #identifica o profesor por um ID
        novo_ID = Sistema.gerarIdProf()
        professor = Professor(novo_ID, nome, email, senha)

        #adiciona o ID do professor ao dicionario Professores no sistema
        Sistema.professores[novo_ID] = professor

        #salva o professor no banco de dados
        Sistema.salvar()

        print(f"Professor {nome} cadastrado com sucesso!")
        return True

    #Cadastra Login do gestor
    @staticmethod
    def cadastrarGestor(nome, email, senha):
       #Carrega o banco de dados
        Sistema.carregar()

        #identifica cada gestor no banco de dados
        for ges in Sistema.gestores.values():
            #checa se existe um email ja cadastrado no banco de dados
            if ges.email == email:
                print("Email já cadastrado!")
                return False

        #identifica o gestor por um novo ID
        novo_ID = Sistema.gerarIdGestor()
        gestor = Gestor(novo_ID, nome, email, senha)

        Sistema.gestores[novo_ID] = gestor

        #salva o login no banco de dados
        Sistema.salvar()

        print(f"Gestor {nome} cadastrado com sucesso!")

    #Validar o usuario
    @staticmethod
    def validarLogin(email, senha):
        #Carrega o banco de dados
        Sistema.carregar()

        #Le todos os professores no banco de dados
        for prof in Sistema.professores.values():
            #CHeca se o email e senha inseridos são válidos
            if prof.email == email and prof.senha ==senha:
                print(f"Login bem-sucedido! Bem-vindo Professor {prof['nome_professor']}")
                return prof
            
        #Le todos os gestores do banco de dados
        for gestor in Sistema.gestores.values():
            #Checa se o email e senha inseridos são válidos
            if gestor.email == email and gestor.senha == senha:
                print(f"Login bem-sucedido! Bem-vindo Gestor {gestor.nome_gestor}")
                return gestor
        
        print("Usuario ou senha incorretos!")
        return None