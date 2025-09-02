from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    TemplateView
)
from .models import Demanda
from .forms import DemandaCreateForm, DemandaUpdateForm
from .filters import DemandaFilter
from reunioes.models import Reuniao

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'demandas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_demandas'] = Demanda.objects.count()
        context['demandas_pendentes'] = Demanda.objects.filter(situacao='pendente').count()
        context['demandas_em_andamento'] = Demanda.objects.filter(situacao='em_andamento').count()
        context['demandas_concluidas'] = Demanda.objects.filter(situacao='concluido').count()

        ultima_reuniao = Reuniao.objects.order_by('-data').first()
        context['ultima_reuniao_data'] = ultima_reuniao.data if ultima_reuniao else None

        return context

class DemandaListView(LoginRequiredMixin, ListView):
    model = Demanda
    template_name = 'demandas/demanda_list.html'
    context_object_name = 'demandas'
    ordering = ['-data_insercao']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = DemandaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

class DemandaDetailView(LoginRequiredMixin, DetailView):
    model = Demanda
    template_name = 'demandas/demanda_detail.html'

class DemandaCreateView(LoginRequiredMixin, CreateView):
    model = Demanda
    form_class = DemandaCreateForm
    template_name = 'demandas/demanda_form.html'
    success_url = reverse_lazy('demandas:demanda-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adicionar Nova Demanda'
        return context

class DemandaUpdateView(LoginRequiredMixin, UpdateView):
    model = Demanda
    form_class = DemandaUpdateForm
    template_name = 'demandas/demanda_form.html'
    success_url = reverse_lazy('demandas:demanda-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Demanda'
        return context

class DemandaDeleteView(LoginRequiredMixin, DeleteView):
    model = Demanda
    template_name = 'demandas/demanda_confirm_delete.html'
    success_url = reverse_lazy('demandas:demanda-list')