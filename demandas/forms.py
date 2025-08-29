from django import forms
from .models import Demanda

class DemandaCreateForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['atividade']

class DemandaUpdateForm(forms.ModelForm):
    data_inicio = forms.DateTimeField(
        label="Data de Início",
        required=False,
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y']
    )
    data_termino = forms.DateTimeField(
        label="Data de Término",
        required=False,
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Demanda
        fields = '__all__'
        exclude = ('data_insercao', 'data_inicio', 'data_termino')
