from django.db import models


class Servico(models.Model):
    titulo = models.CharField(max_length=400, verbose_name='Título')
    descricao = models.CharField(max_length=400, verbose_name='Descrição')
    valor = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Valor'
    )
    ativo = models.BooleanField(
        auto_created=True,
        default=True,
        verbose_name='Ativo'
    )

    def __str__(self) -> str:
        return self.titulo
