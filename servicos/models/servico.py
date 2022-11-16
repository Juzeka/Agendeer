from django.db import models


class Servico(models.Model):
    descricao = models.CharField(max_length=400, blank=False, null=False)
    valor = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False
    )
    ativo = models.BooleanField(
        auto_created=True,
        default=True,
    )