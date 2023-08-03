from django.urls import path
from .views import index,processar_formulario, login, logout, cadastro, painel,paciente,plano,medida

urlpatterns = [
    path('index', index, name='index'),
    path('processar_formulario', processar_formulario, name='processar_formulario'),
    path('', login , name='login'),
    path('logout/', logout , name='logout'),
    path('cadastro/',cadastro, name='cadastro'),
    path('painel/', painel, name = 'painel'),
    path('paciente/<int:pk>', paciente, name='paciente'),
    path('plano/<int:pk>', plano, name='plano'),
    path('medida/<int:pk>', medida, name='medida'),
]
