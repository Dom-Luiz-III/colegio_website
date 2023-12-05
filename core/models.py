from django.db import models


class Professor(models.Model):
    nome_professor = models.CharField('Nome do professor',max_length=100)
    disciplina = models.CharField('Disciplina do Professor', max_length=20, choices=[
        ('geografia', 'Geografia'), ('historia', 'História'), ('matematica', 'Matemática'), ('geometria', 'Geometria'), ('portugues', 'Português'), ('ingles', 'Inglês'), ('fisica', 'Física'), ('quimica', 'Química')])

    def __str__(self):
        return self.nome_professor


class Atividade(models.Model):
    nome_atividade = models.CharField('Nome da Atividade',max_length=100)
    descricao = models.TextField('Descrição da Atividade')
    pontos = models.IntegerField('Quantos pontos valem a atividade')
    data_entrega = models.DateField('Data de Entrega')

    def __str__(self):
        return self.nome_atividade


class Turma(models.Model):

    turma_codigo = models.CharField('Codigo da turma', max_length=100)
    aluno_quantidade = models.IntegerField('Quantidade de alunos')
    numero_sala_turma = models.IntegerField('Numero da sala da turma')
    turma_turno = models.CharField('Turno', max_length=20, choices=[
        ('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno')])
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    atividades = models.ManyToManyField(Atividade)

    def __str__(self):
        return f"Turma {self.turma_codigo}"
