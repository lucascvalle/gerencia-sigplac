from django.db import models
from django.contrib.auth.models import User

class Demanda(models.Model):
    SITUACAO_CHOICES = [
        ('backlog', 'Backlog'),
        ('pendente', 'Pendente'),
        ('em_analise', 'Em Análise'),
        ('em_andamento', 'Em Andamento'),
        ('em_espera', 'Em Espera'),
        ('em_teste', 'Em Teste'),
        ('em_revisao', 'Em Revisão'),
        ('resolvido', 'Resolvido'),
        ('rejeitado_cancelado', 'Rejeitado/Cancelado'),
    ]

    CATEGORIA_CHOICES = [
        ('desenvolvimento', 'Desenvolvimento'),
        ('manutencao_correcao', 'Manutenção/Correção'),
        ('infraestrutura_devops', 'Infraestrutura/DevOps'),
        ('testes', 'Testes'),
        ('documentacao', 'Documentação'),
        ('administrativo', 'Administrativo'),
        ('outros', 'Outros'),
    ]

    PRIORIDADE_CHOICES = [
        ('critica', 'Crítica / P0'),
        ('alta', 'Alta / P1'),
        ('media', 'Média / P2'),
        ('baixa', 'Baixa / P3'),
    ]

    atividade = models.TextField(verbose_name="Atividade")
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='outros', verbose_name="Categoria")
    prioridade = models.CharField(max_length=50, choices=PRIORIDADE_CHOICES, default='baixa', verbose_name="Prioridade")
    data_insercao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Inserção")
    data_inicio = models.DateTimeField(null=True, blank=True, verbose_name="Data de Início")
    data_prevista = models.DateTimeField(null=True, blank=True, verbose_name="Data Prevista")
    andamento_detalhado = models.TextField(verbose_name="Andamento Detalhado", blank=True)
    responsavel = models.ForeignKey(User, related_name='demandas_responsaveis', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Responsável")
    supervisor = models.ForeignKey(User, related_name='demandas_supervisionadas', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Supervisor")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, default='backlog', verbose_name="Situação")
    horas_executadas = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Horas Executadas")

    def __str__(self):
        return self.atividade

    class Meta:
        verbose_name = "Demanda"
        verbose_name_plural = "Demandas"
