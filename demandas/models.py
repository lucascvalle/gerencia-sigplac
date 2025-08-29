from django.db import models
from django.contrib.auth.models import User

class Demanda(models.Model):
    SITUACAO_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    atividade = models.TextField(verbose_name="Atividade")
    data_insercao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Inserção")
    data_inicio = models.DateTimeField(null=True, blank=True, verbose_name="Data de Início")
    data_termino = models.DateTimeField(null=True, blank=True, verbose_name="Data de Término")
    andamento_detalhado = models.TextField(verbose_name="Andamento Detalhado", blank=True)
    responsavel = models.ForeignKey(User, related_name='demandas_responsaveis', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Responsável")
    supervisor = models.ForeignKey(User, related_name='demandas_supervisionadas', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Supervisor")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, default='pendente', verbose_name="Situação")

    def __str__(self):
        return self.atividade

    class Meta:
        verbose_name = "Demanda"
        verbose_name_plural = "Demandas"
