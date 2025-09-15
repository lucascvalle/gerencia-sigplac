from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Reuniao, Topico, Ponto
from .forms import ReuniaoForm, TopicoForm, PontoForm
from .filters import ReuniaoFilter


class ReuniaoListView(ListView):
    model = Reuniao
    template_name = 'reunioes/reuniao_list.html'
    context_object_name = 'reunioes'
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = ReuniaoFilter(self.request.GET, queryset=queryset)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context


class ReuniaoDetailView(DetailView):
    model = Reuniao
    template_name = 'reunioes/reuniao_detail.html'
    context_object_name = 'reuniao'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topicos'] = self.object.topicos.all().prefetch_related('pontos__demanda')
        return context


class ReuniaoCreateView(CreateView):
    model = Reuniao
    form_class = ReuniaoForm
    template_name = 'reunioes/reuniao_form.html'
    success_url = reverse_lazy('reunioes:reuniao_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agendar Nova Reunião'
        return context


class ReuniaoUpdateView(UpdateView):
    model = Reuniao
    form_class = ReuniaoForm
    template_name = 'reunioes/reuniao_form.html'
    success_url = reverse_lazy('reunioes:reuniao_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Reunião'
        return context


class ReuniaoDeleteView(DeleteView):
    model = Reuniao
    template_name = 'reunioes/reuniao_confirm_delete.html'
    success_url = reverse_lazy('reunioes:reuniao_list')


# --- Views de Tópico ---

class TopicoCreateView(CreateView):
    model = Topico
    form_class = TopicoForm
    template_name = 'reunioes/topico_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adicionar Novo Tópico'
        context['reuniao'] = get_object_or_404(Reuniao, pk=self.kwargs['reuniao_pk'])
        return context

    def form_valid(self, form):
        form.instance.reuniao = get_object_or_404(Reuniao, pk=self.kwargs['reuniao_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reunioes:reuniao_detail', kwargs={'pk': self.kwargs['reuniao_pk']})


class TopicoUpdateView(UpdateView):
    model = Topico
    form_class = TopicoForm
    template_name = 'reunioes/topico_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Tópico'
        context['reuniao'] = self.object.reuniao
        return context

    def get_success_url(self):
        return reverse('reunioes:reuniao_detail', kwargs={'pk': self.object.reuniao.pk})


class TopicoDeleteView(DeleteView):
    model = Topico
    template_name = 'reunioes/topico_confirm_delete.html'

    def get_success_url(self):
        return reverse('reunioes:reuniao_detail', kwargs={'pk': self.object.reuniao.pk})


# --- Views de Ponto ---

class PontoCreateView(CreateView):
    model = Ponto
    form_class = PontoForm
    template_name = 'reunioes/ponto_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adicionar Novo Ponto'
        context['topico'] = get_object_or_404(Topico, pk=self.kwargs['topico_pk'])
        return context

    def form_valid(self, form):
        form.instance.topico = get_object_or_404(Topico, pk=self.kwargs['topico_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reunioes:reuniao_detail', kwargs={'pk': self.object.topico.reuniao.pk})


class PontoUpdateView(UpdateView):
    model = Ponto
    form_class = PontoForm
    template_name = 'reunioes/ponto_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Ponto'
        context['topico'] = self.object.topico
        return context

    def get_success_url(self):
        return reverse('reunioes:reuniao_detail', kwargs={'pk': self.object.topico.reuniao.pk})


class PontoDeleteView(DeleteView):
    model = Ponto
    template_name = 'reunioes/ponto_confirm_delete.html'

    def get_success_url(self):
        return reverse('reunioes:reuniao_detail', kwargs={'pk': self.object.topico.reuniao.pk})
