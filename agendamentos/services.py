from django.shortcuts import get_object_or_404
from funcionarios.models import Funcionario


class AgendamentoService:
    def __init__(self, *args, **kwargs):
        self.data = kwargs.get('data')
        self.horario = kwargs.get('horario')
        self.funcionario = kwargs.get('funcionario')
        self.ativo = None

    def alterar_status_horario_funcionario(self):
        funcionairo = get_object_or_404(
            Funcionario,
            pk=self.funcionario
        )

        disponibilidade = funcionairo.disponibilidades.filter(
            data=self.data
        ).first()

        horario = disponibilidade.horarios.filter(
            horario=self.horario
        ).first()

        horario.ativo = self.ativo
        horario.save()

    def desativar_horario_data_funcionario(self):
        self.ativo = False

        self.alterar_status_horario_funcionario()

    def ativar_horario_data_funcionario(self):
        self.ativo = True

        self.alterar_status_horario_funcionario()