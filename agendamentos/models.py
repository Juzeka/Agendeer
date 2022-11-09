from django.db import models


class Agendamento(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT)
    funcionario = models.ForeignKey(
        'funcionarios.Funcionario',
        on_delete=models.PROTECT
    )
    servico = models.ForeignKey('servicos.Servico', on_delete=models.PROTECT)
    data = models.DateField(blank=False, null=False)
    horario = models.TimeField(blank=False, null=False)
    ativo = models.BooleanField(
        auto_created=True,
        default=True,
    )
    concluido = models.BooleanField(
        auto_created=True,
        default=False,
    )
    cancelado = models.BooleanField(
        auto_created=True,
        default=False,
    )

    def __str__(self) -> str:
        return f'{self.data} às {self.horario} - {self.funcionario}'