from django.db import models


class Configuracao(models.Model):
    DISPONIBILIDADES_CHOICES = (
        (1, 'Um dia'),
        (3, 'Três dias'),
        (7, 'Uma semana dias'),
        (30, 'Um mês'),
    )

    enviar_msg = models.BooleanField(
        auto_created=True,
        default=True,
    )
    endereco = models.CharField(max_length=200, blank=False, null=False)
    gerar_disponibilidade = models.CharField(
        max_length=20,
        choices=DISPONIBILIDADES_CHOICES,
        default=1
    )
    horarios = models.ManyToManyField(
        'horarios.Horario',
        related_name='configuracao_horario'
    )