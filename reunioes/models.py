from django.db import models
from django.urls import reverse
from demandas.models import Demanda

class Reuniao(models.Model):
    """
    Modelo para representar uma reunião.
    """
    titulo = models.CharField(max_length=200, help_text="Título da reunião")
    data = models.DateField(help_text="Data da reunião")
    hora_inicio = models.TimeField(null=True, blank=True, help_text="Horário de início")
    hora_fim = models.TimeField(null=True, blank=True, help_text="Horário de término")
    local = models.CharField(max_length=200, blank=True, help_text="Local da reunião")
    participantes = models.TextField(blank=True, help_text="Lista de participantes")

    class Meta:
        verbose_name = "Reunião"
        verbose_name_plural = "Reuniões"
        ordering = ['-data']

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')} - {self.titulo}"

    def get_absolute_url(self):
        return reverse('reunioes:reuniao_detail', kwargs={'pk': self.pk})


class Topico(models.Model):
    """
    Modelo para representar um tópico (assunto) de uma reunião.
    """
    reuniao = models.ForeignKey(Reuniao, related_name='topicos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, help_text="Título do tópico")
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de apresentação do tópico")

    class Meta:
        verbose_name = "Tópico"
        verbose_name_plural = "Tópicos"
        ordering = ['ordem']

    def __str__(self):
        return self.titulo


class Ponto(models.Model):
    """
    Modelo para representar um ponto (item de discussão) dentro de um tópico.
    """
    topico = models.ForeignKey(Topico, related_name='pontos', on_delete=models.CASCADE)
    descricao = models.TextField(help_text="Descrição do ponto discutido")
    demanda = models.ForeignKey(Demanda, on_delete=models.SET_NULL, null=True, blank=True, related_name='pontos_reuniao', help_text="Demanda associada a este ponto")
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de apresentação do ponto")

    class Meta:
        verbose_name = "Ponto"
        verbose_name_plural = "Pontos"
        ordering = ['ordem']

    def __str__(self):
        return self.descricao[:80]

    @property
    def status(self):
        if self.demanda:
            return self.demanda.get_situacao_display()
        return "Não aplicável"