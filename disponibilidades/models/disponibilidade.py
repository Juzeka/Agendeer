from django.db import models


class Disponibilidade(models.Model):
    data = models.DateField(blank=False, null=False)
    horarios = models.ManyToManyField(
        'horarios.Horario',
        related_name='disponibilidade_horario',
    )
    ativo = models.BooleanField(
        auto_created=True,
        default=True,
    )

    def __str__(self) -> str:
        return f'{self.data}'
