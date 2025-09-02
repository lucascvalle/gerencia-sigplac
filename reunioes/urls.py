from django.urls import path
from . import views

app_name = 'reunioes'

urlpatterns = [
    path('', views.ReuniaoListView.as_view(), name='reuniao_list'),
    path('<int:pk>/', views.ReuniaoDetailView.as_view(), name='reuniao_detail'),
]
