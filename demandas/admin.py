from django.contrib import admin
from .models import Demanda

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = ('atividade', 'responsavel', 'data_insercao', 'situacao')
    list_filter = ('situacao', 'responsavel', 'data_insercao')
    search_fields = ('atividade', 'andamento_detalhado', 'responsavel__first_name', 'responsavel__last_name')
    date_hierarchy = 'data_insercao'
    autocomplete_fields = ['responsavel', 'supervisor']