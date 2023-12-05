from django.utils.html import format_html
from django.contrib import admin

from .models import Professor, Atividade, Turma


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome_professor', 'disciplina')


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome_atividade', 'descricao', 'data_entrega')


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma_codigo', 'aluno_quantidade', 'numero_sala_turma', 'turma_turno', 'display_atividades')

    def display_atividades(self, obj):
        atividades = obj.atividades.all()
        return format_html(', '.join(a.nome_atividade for a in atividades))

    display_atividades.short_description = 'Atividades'


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(Turma, TurmaAdmin)