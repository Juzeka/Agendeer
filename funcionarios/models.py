from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    nome_full = models.CharField(max_length=200, blank=False, null=False)
    disponibilidades = models.ManyToManyField(
        'disponibilidades.Disponibilidade',
        related_name='funcionario_disponibilidade'
    )

    def __str__(self):
        return self.nome_full