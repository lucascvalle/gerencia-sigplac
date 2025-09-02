from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Demanda

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = ('atividade', 'display_responsavel', 'data_insercao', 'situacao')
    list_filter = ('situacao', 'responsavel', 'data_insercao')
    search_fields = ('atividade', 'andamento_detalhado', 'responsavel__first_name', 'responsavel__last_name')
    date_hierarchy = 'data_insercao'
    autocomplete_fields = ['responsavel', 'supervisor']

    def display_responsavel(self, obj):
        return obj.responsavel.username if obj.responsavel else '-'
    display_responsavel.short_description = 'Responsável'

# Unregister the default UserAdmin
admin.site.unregister(User)

# Define a new UserAdmin with search_fields
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    search_fields = ('username', 'first_name', 'last_name', 'email')
