from .models import Dietas
from django.db.models import  Q

class PacienteService():

    def get_dietas_by_paciente_and_data(self,paciente, data_especifica):
        filters=[None] * 7
        filters[0] = Q(refeicoes__refeicoes__icontains='Café da manhã') & Q(paciente__nome=paciente.nome)
        filters[1] = Q(refeicoes__refeicoes__icontains='Belisquete almoço') & Q(paciente__nome=paciente.nome)
        filters[2] = Q(refeicoes__refeicoes='Almoço') & Q(paciente__nome=paciente.nome)
        filters[3] = Q(refeicoes__refeicoes__icontains='Café da tarde') & Q(paciente__nome=paciente.nome)
        filters[4] = Q(refeicoes__refeicoes__icontains='Jantar') & Q(paciente__nome=paciente.nome)
        filters[5] = Q(refeicoes__refeicoes__icontains='Belisquete jantar') & Q(paciente__nome=paciente.nome)
        filters[6] = Q(refeicoes__refeicoes__icontains='Pernoite') & Q(paciente__nome=paciente.nome)
        if data_especifica:
            # Filtrando as datas manualmente, comparando apenas dia, mês e ano
            filterData = Q(criado__day=data_especifica.day) & Q(criado__month=data_especifica.month) & Q(criado__year=data_especifica.year)
            for contador in range(0,7):
                filters[contador] = filters[contador] & filterData

        cafe_manha = Dietas.objects.filter(filters[0])
        belisquete_almoco = Dietas.objects.filter(filters[1])
        almoco = Dietas.objects.filter(filters[2])
        cafe_tarde = Dietas.objects.filter(filters[3])
        jantar = Dietas.objects.filter(filters[4])
        belisquete_jantar = Dietas.objects.filter(filters[5])
        pernoite =Dietas.objects.filter(filters[6])

        ret = {}
        ret['cafe_manha'] = cafe_manha
        ret['belisquete_almoco'] = belisquete_almoco
        ret['almoco'] = almoco
        ret['cafe_tarde'] = cafe_tarde
        ret['jantar'] = jantar
        ret['belisquete_jantar'] = belisquete_jantar
        ret['pernoite'] = pernoite

        return ret

    def get_soma_proteinas(self, dictProteinas):

        total_proteina_cafe_manha = sum(d.alimento.proteina * d.quantidade for d in dictProteinas['cafe_manha'])
        total_proteina_cafe_manha = round(total_proteina_cafe_manha, 3) 

        total_proteina_belisquete_almoco = sum(d.alimento.proteina * d.quantidade for d in dictProteinas['belisquete_almoco'])
        total_proteina_belisquete_almoco = round(total_proteina_belisquete_almoco, 3) 
        
        total_proteina_almoco = sum(d.alimento.proteina * d.quantidade for d in dictProteinas['almoco'])
        total_proteina_almoco = round(total_proteina_almoco, 3) 

        total_proteina_cafe_tarde = sum(d.alimento.proteina * d.quantidade for d in dictProteinas['cafe_tarde'])
        total_proteina_cafe_tarde = round(total_proteina_cafe_tarde, 3)

        total_proteina_jantar = sum(d.alimento.proteina * d.quantidade for d in dictProteinas['jantar'])
        total_proteina_jantar = round(total_proteina_jantar, 3)

        total_proteina_belisquete_jantar = sum(d.alimento.proteina * d.quantidade for d in dictProteinas['belisquete_jantar'])
        total_proteina_belisquete_jantar = round(total_proteina_belisquete_jantar, 3)

        total_proteina_pernoite = sum(d.alimento.proteina * d.quantidade for d in dictProteinas['pernoite'])
        total_proteina_pernoite = round(total_proteina_pernoite, 3)

        ret = {}
        ret['total_proteina_cafe_manha'] = total_proteina_cafe_manha
        ret['total_proteina_belisquete_almoco'] = total_proteina_belisquete_almoco
        ret['total_proteina_almoco'] = total_proteina_almoco
        ret['total_proteina_cafe_tarde'] = total_proteina_cafe_tarde
        ret['total_proteina_jantar'] = total_proteina_jantar
        ret['total_proteina_belisquete_jantar'] = total_proteina_belisquete_jantar
        ret['total_proteina_pernoite'] = total_proteina_pernoite

        total_proteina = (total_proteina_cafe_manha + total_proteina_belisquete_almoco+total_proteina_almoco + total_proteina_cafe_tarde
    + total_proteina_jantar+ total_proteina_belisquete_jantar+ total_proteina_pernoite)
        
        ret['total_proteina'] = total_proteina

        return ret