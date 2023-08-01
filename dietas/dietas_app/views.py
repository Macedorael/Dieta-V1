from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .bdo import PacienteService
from .forms import PacienteForm, AlimentoForm, DietasForm
from .models import Paciente, Alimento,Medida,Dietas,Refeicao
from django.contrib import messages
from django.db.models import  Q
from django.utils.dateparse import parse_date
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


from django.shortcuts import render


def processar_formulario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        context = {
            'nome': nome,
            'sexo': sexo,
            'idade': idade,
            'peso': peso,
            'altura': altura,
        }

       
        return render(request, 'confirmacao.html', context)

    
    return render(request, 'vazio.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            return redirect('painel') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')


def cadastro(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('cadastro')
        else:
            messages.error(request, 'Erro ao cadastrar!')
    else:
        form = PacienteForm()
        
    
    return render(request, 'cadastro_paciente.html', {'form': form})


def painel(request):
    pacientes = Paciente.objects.all()
    context={
        'pacientes': pacientes
    }
    return render(request, 'painel.html',context)



def paciente(request, pk):
    paciente_form = Paciente.objects.get(id=pk)
    paciente = Paciente.objects.get(id=pk)
    data_especifica = None
    data_especifica_frm = None

    if request.method == 'POST':
        try:
            data_especifica = request.POST.get('data_especifica')
            data_especifica_frm = parse_date(data_especifica)
        except:
            pass

        form = DietasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente', pk=pk) 
    else:
        form = DietasForm(initial={'paciente': paciente})

    objPacienteService = PacienteService()
    retDietaPaciente = objPacienteService.get_dietas_by_paciente_and_data(paciente, data_especifica_frm)
    retSomaProteinas = objPacienteService.get_soma_proteinas(retDietaPaciente)

    context = {
        'paciente_form': paciente_form,
        'form': form,
        'paciente': paciente,
        'data_filtro' : data_especifica
    }
    context.update(retDietaPaciente)
    context.update(retSomaProteinas)
    
    return render(request, 'paciente.html', context)


def dieta(request, pk):
    paciente = Paciente.objects.get(id=pk)
    
    if request.method == 'POST':
        form = DietasForm(request.POST)
        
        if form.is_valid():
            form.instance.paciente = paciente 
            form.save()
            return redirect('paciente', pk=pk) 
    else:
        form = DietasForm(initial={'paciente': paciente})  
    return render(request, 'dieta.html', {'form': form})



