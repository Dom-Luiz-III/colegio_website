# Generated by Django 5.0 on 2023-12-05 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_carro_formas_pagamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_atividade', models.CharField(max_length=100, verbose_name='Nome da Atividade')),
                ('descricao', models.TextField(verbose_name='Descrição da Atividade')),
                ('pontos', models.IntegerField(verbose_name='Quantos pontos valem a atividade')),
                ('data_entrega', models.DateField(verbose_name='Data de Entrega')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_professor', models.CharField(max_length=100, verbose_name='Nome do professor')),
                ('disciplina', models.CharField(choices=[('geografia', 'Geografia'), ('historia', 'História'), ('matematica', 'Matemática'), ('geometria', 'Geometria'), ('portugues', 'Português'), ('ingles', 'Inglês'), ('fisica', 'Física'), ('quimica', 'Química')], max_length=20, verbose_name='Disciplina do Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma_codigo', models.CharField(max_length=100, verbose_name='Codigo da turma')),
                ('aluno_quantidade', models.IntegerField(verbose_name='Quantidade de alunos')),
                ('numero_sala_turma', models.IntegerField(verbose_name='Numero da sala da turma')),
                ('turma_turno', models.CharField(choices=[('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno')], max_length=20, verbose_name='Turno')),
                ('atividades', models.ManyToManyField(to='core.atividade')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor')),
            ],
        ),
        migrations.DeleteModel(
            name='Carro',
        ),
        migrations.DeleteModel(
            name='Moto',
        ),
    ]
