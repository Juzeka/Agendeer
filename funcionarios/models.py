from django.db import models


class Funcionario(models.Model):
    # user = models.ForeignKey
    nome_full = models.CharField(max_length=200, blank=False, null=False)
    disponibilidades = models.ManyToManyField(
        'disponibilidades.Disponibilidade',
        related_name='funcionario_disponibilidade'
    )

    def __str__(self) -> str:
        return self.nome_full