from django.views.generic import ListView, DetailView
from .models import Reuniao

class ReuniaoListView(ListView):
    model = Reuniao
    template_name = 'reunioes/reuniao_list.html'
    context_object_name = 'reunioes'
    paginate_by = 15

class ReuniaoDetailView(DetailView):
    model = Reuniao
    template_name = 'reunioes/reuniao_detail.html'
    context_object_name = 'reuniao'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Otimiza a consulta para buscar tópicos e pontos relacionados de uma só vez
        context['topicos'] = self.object.topicos.all().prefetch_related('pontos__demanda')
        return context