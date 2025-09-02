from django.urls import path
from .views import (
    DemandaListView,
    DemandaDetailView,
    DemandaCreateView,
    DemandaUpdateView,
    DemandaDeleteView
)

app_name = 'demandas'

urlpatterns = [
    path('', DemandaListView.as_view(), name='demanda-list'),
    path('<int:pk>/', DemandaDetailView.as_view(), name='demanda-detail'),
    path('nova/', DemandaCreateView.as_view(), name='demanda-create'),
    path('<int:pk>/editar/', DemandaUpdateView.as_view(), name='demanda-update'),
    path('<int:pk>/deletar/', DemandaDeleteView.as_view(), name='demanda-delete'),
]
