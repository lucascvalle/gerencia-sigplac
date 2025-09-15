import django_filters
from .models import Demanda

class DemandaFilter(django_filters.FilterSet):
    data_insercao = django_filters.DateFromToRangeFilter(label='Período de Inserção')

    class Meta:
        model = Demanda
        fields = {
            'situacao': ['exact'],
            'responsavel': ['exact'],
            'supervisor': ['exact'],
            'categoria': ['exact'],
            'prioridade': ['exact'],
        }
