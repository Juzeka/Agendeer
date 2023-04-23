from django.db import models
from utils.choices import STATUS_AGENDAMENTO_CHOICES, ATIVO


class Agendamento(models.Model):
    protocolo = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Protocolo'
    )
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT)
    funcionario = models.ForeignKey(
        'funcionarios.Funcionario',
        on_delete=models.PROTECT
    )
    servico = models.ForeignKey(
        'servicos.Servico',
        on_delete=models.PROTECT,
        related_name='servico'
    )
    data = models.DateField(blank=False, null=False)
    horario = models.TimeField(blank=False, null=False)
    status = models.CharField(
        max_length=10,
        choices=STATUS_AGENDAMENTO_CHOICES,
        default=ATIVO
    )
    pago = models.BooleanField(auto_created=True, default=False)

    def __str__(self) -> str:
        return f'{self.data} às {self.horario} - {self.funcionario}'
