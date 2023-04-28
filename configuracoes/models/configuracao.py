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
        verbose_name='Enviar mensagens automaticas'
    )
    grupos_permissao = models.BooleanField(
        auto_created=True,
        default=False,
        verbose_name='Grupos de permissões padrão criados'
    )
    agendamento = models.BooleanField(
        auto_created=True,
        default=True,
        verbose_name='Disponível para agendamento'
    )
    fidelidade = models.BooleanField(
        auto_created=True,
        default=False,
        verbose_name='Plano fidelidade'
    )
    validade = models.IntegerField(
        default=0,
        verbose_name='Quantidade em dias para a valide da fidelização'
    )
    quantidade_fidelidade = models.IntegerField(
        default=0,
        verbose_name='Qntd de serviços concluidos para completar a fidelização'
    )
    endereco = models.CharField(max_length=200, blank=False, null=False)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=11, blank=False, null=False)
    celular = models.CharField(max_length=11, blank=False, null=False)
    gerar_disponibilidade = models.IntegerField(
        choices=DISPONIBILIDADES_CHOICES,
        default=1
    )
    horarios = models.ManyToManyField(
        'horarios.Horario',
        related_name='configuracao_horario'
    )
