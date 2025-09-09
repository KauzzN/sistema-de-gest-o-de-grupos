# alunos/models.py
from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,  # se a turma for deletada, aluno não some
        null=True,
        blank=True,
        related_name="alunos"
    )
    status = models.CharField(
        max_length=20,
        choices=[("ativo", "Ativo"), ("inativo", "Inativo"), ("nenhum", "Nenhum")],
        default="nenhum"
    )

    def __str__(self):
        return self.nome
