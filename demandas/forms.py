from django import forms
from .models import Demanda

class DemandaCreateForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['atividade', 'categoria', 'prioridade']

class DemandaUpdateForm(forms.ModelForm):
    data_inicio = forms.DateTimeField(
        label="Data de Início",
        required=False,
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y']
    )
    data_prevista = forms.DateTimeField(
        label="Data Prevista",
        required=False,
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Demanda
        fields = '__all__'
        exclude = ('data_insercao',)
