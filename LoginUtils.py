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
    def cadastrarProfessor(nome_professor, email, senha, id_turma):

        #carrega os dados do "banco de dados"
        Sistema.carregar()

        turma = Sistema.turmas.get(id_turma)
        if turma is None:
            print("Turma não encontrada!")
            return

        #checa no banco de dados todos os logins cadastrados
        for prof in Sistema.professores.values():
            #checa se existe um email ja cadastrado
            if prof.email == email:
                print("Email já está cadastrado!")
                return False
        
        #identifica o profesor por um ID
        professor = Professor(nome_professor = nome_professor, email = email, senha = senha)

        #adiciona o ID do professor ao dicionario Professores no sistema
        Sistema.professores[professor.id_professor] = professor

        if not isinstance(turma.professores , list):
            turma.professores = []

        #adiciona o professor a uma turma
        if professor.id_professor not in turma.professores:
            turma.professores.append(professor.id_professor)

        #salva o professor no banco de dados
        Sistema.salvar()

        print(f"Professor {nome_professor} cadastrado com sucesso!")
        return True

    #Cadastra Login do gestor
    @staticmethod
    def cadastrarGestor(nome_gestor, email, senha):
       #Carrega o banco de dados
        Sistema.carregar()

        #identifica cada gestor no banco de dados
        for ges in Sistema.gestores.values():
            #checa se existe um email ja cadastrado no banco de dados
            if ges.email == email:
                print("Email já cadastrado!")
                return False

        #identifica o gestor por um novo ID
        gestor = Gestor(nome_gestor = nome_gestor, email = email, senha = senha)

        Sistema.gestores[gestor.id_gestor] = gestor

        #salva o login no banco de dados
        Sistema.salvar()

        print(f"Gestor {nome_gestor} cadastrado com sucesso!")
        return True

    #Validar o usuario
    @staticmethod
    def validarLogin(email, senha):
        #Carrega o banco de dados
        Sistema.carregar()

        #Le todos os professores no banco de dados
        for prof in Sistema.professores.values():
            #CHeca se o email e senha inseridos são válidos
            if prof.email == email and prof.senha ==senha:
                print(f"Login bem-sucedido! Bem-vindo Professor {prof.nome_professor}")
                return prof
            
        #Le todos os gestores do banco de dados
        for gestor in Sistema.gestores.values():
            #Checa se o email e senha inseridos são válidos
            if gestor.email == email and gestor.senha == senha:
                print(f"Login bem-sucedido! Bem-vindo Gestor {gestor.nome_gestor}")
                return gestor
        
        print("Usuario ou senha incorretos!")
        return None