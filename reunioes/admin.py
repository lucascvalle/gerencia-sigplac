from django.contrib import admin
from .models import Reuniao, Topico, Ponto


class PontoInline(admin.TabularInline):
    model = Ponto
    fields = ('ordem', 'descricao', 'demanda')
    extra = 1
    autocomplete_fields = ['demanda']


class TopicoInline(admin.TabularInline):
    model = Topico
    fields = ('ordem', 'titulo')
    extra = 1


@admin.register(Reuniao)
class ReuniaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'local')
    list_filter = ('data',)
    search_fields = ('titulo', 'participantes')
    inlines = [TopicoInline]


@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'reuniao', 'ordem')
    search_fields = ('titulo', 'reuniao__titulo')
    inlines = [PontoInline]


@admin.register(Ponto)
class PontoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'topico', 'demanda', 'status')
    list_filter = ('topico__reuniao__data',)
    search_fields = ('descricao', 'demanda__titulo')
    autocomplete_fields = ['demanda', 'topico']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('topico__reuniao', 'demanda')