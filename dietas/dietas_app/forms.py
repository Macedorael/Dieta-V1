from django import forms
from .models import Paciente, Medida, Alimento, Dietas, Refeicao

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'telefone', 'email',]

class MedidaForm(forms.ModelForm):
    class Meta:
        model = Medida
        fields = ['nome', 'peso', 'altura']


class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ['nome', 'peso', 'proteina']

class DietasForm(forms.ModelForm):
    class Meta:
        model = Dietas
        fields = ['refeicoes','paciente', 'quantidade', 'alimento']

class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = ['id','refeicoes']