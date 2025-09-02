from django.urls import path
from . import views

app_name = 'reunioes'

urlpatterns = [
    path('', views.ReuniaoListView.as_view(), name='reuniao_list'),
    path('nova/', views.ReuniaoCreateView.as_view(), name='reuniao_create'),
    path('<int:pk>/', views.ReuniaoDetailView.as_view(), name='reuniao_detail'),
    path('<int:pk>/editar/', views.ReuniaoUpdateView.as_view(), name='reuniao_update'),
    path('<int:pk>/deletar/', views.ReuniaoDeleteView.as_view(), name='reuniao_delete'),

    # URLs de Tópico
    path('<int:reuniao_pk>/topicos/novo/', views.TopicoCreateView.as_view(), name='topico_create'),
    path('topicos/<int:pk>/editar/', views.TopicoUpdateView.as_view(), name='topico_update'),
    path('topicos/<int:pk>/deletar/', views.TopicoDeleteView.as_view(), name='topico_delete'),

    # URLs de Ponto
    path('topicos/<int:topico_pk>/pontos/novo/', views.PontoCreateView.as_view(), name='ponto_create'),
    path('pontos/<int:pk>/editar/', views.PontoUpdateView.as_view(), name='ponto_update'),
    path('pontos/<int:pk>/deletar/', views.PontoDeleteView.as_view(), name='ponto_delete'),
]
