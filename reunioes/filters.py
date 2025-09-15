import django_filters
from .models import Reuniao

class ReuniaoFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains', label='Título')
    data = django_filters.DateFromToRangeFilter(label='Período')

    class Meta:
        model = Reuniao
        fields = ['titulo', 'data']
