from django.db import models


class Disponibilidade(models.Model):
    data = models.DateField(blank=False, null=False)
    horarios = models.ManyToManyField(
        'horarios.Horario',
        related_name='disponibilidade_horario',
    )

    def __str__(self) -> str:
        return f'{self.data}'