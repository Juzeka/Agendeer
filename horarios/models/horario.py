from django.db import models


class Horario(models.Model):
    horario = models.TimeField(blank=False, null=False)
    ativo = models.BooleanField(
        auto_created=True,
        default=True,
    )

    def __str__(self) -> str:
        return f'{self.horario} - {self.ativo}'
