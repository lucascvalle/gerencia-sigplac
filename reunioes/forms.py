from django import forms
from .models import Reuniao, Topico, Ponto

class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = Reuniao
        fields = ['titulo', 'data', 'hora_inicio', 'hora_fim', 'local', 'participantes']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(
                attrs={'class': 'form-control datepicker', 'placeholder': 'DD/MM/AAAA'}
            ),
            'hora_inicio': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
            ),
            'hora_fim': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
            ),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'participantes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'ordem']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PontoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['demanda'].queryset = self.fields['demanda'].queryset.order_by('atividade')

    class Meta:
        model = Ponto
        fields = ['descricao', 'ordem', 'demanda']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control'}),
            'demanda': forms.Select(attrs={'class': 'form-select'}),
        }
