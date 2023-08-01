from django.contrib import admin
from .models import Paciente, Alimento, Medida, Dietas,Refeicao


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','email','criado','modificado','ativo')

class MedidaAdmin(admin.ModelAdmin):
    list_display = ('nome','peso','altura','modificado')


class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nome','peso', 'proteina', 'modificado')


class DietasAdmin(admin.ModelAdmin):
    list_display = ('refeicoes','paciente','quantidade', 'alimento', 'criado')

class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'refeicoes',) 




admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medida, MedidaAdmin)
admin.site.register(Alimento, AlimentoAdmin)
admin.site.register(Dietas, DietasAdmin)
admin.site.register(Refeicao, RefeicaoAdmin)
