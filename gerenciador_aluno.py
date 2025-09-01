
from alunos import Aluno

class Gerenciador_aluno:
    def __init__(self):
        self.lista_alunos = []

    def cadastrar_aluno(self):
        try:
            nome = input("Digite o nome do aluno: ")
            if not nome:
                print("Nome é obrigatorio")

            idade = input("Digite a idade do aluno: ")
            if idade < 5 or idade > 100:
                print("Idade tem que esta entre 5 a 100 anos. ")

            matricula = input("Digite a matrícula do aluno: ")
            if not matricula:
                print("Matricula é obrigatoria. ")

            novo_aluno = Aluno(nome, idade, matricula)
            self.lista_alunos.append(novo_aluno)
            return self

        except ValueError:
            print("A idade não é valida. ")

